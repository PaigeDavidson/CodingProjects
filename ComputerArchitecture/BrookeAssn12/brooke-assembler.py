def preprocess_lines(lines):
    preprocessed_lines = []
    
    for line in lines:
        line_without_comment = line.split("#")[0]
        stripped_line = line_without_comment.strip()
        if stripped_line:
            preprocessed_lines.append(stripped_line)
    return preprocessed_lines
            

def build_data_table(lines):
    dataIndex = 0
    data = False
    dataTable = {}
    dataList = []
    newDataset = []

    for line in lines:
        if line.strip() == ".data":
            data = True
            continue

        if line.strip() == ".text":
            data = False
            continue

        if data:
            split_line = line.split(":")
            label = split_line[0].strip()
            value = split_line[1].strip()
            
            dataTable[label] = dataIndex
            
            dataList.append(int(value))
            
            dataIndex += 1
        else:
            newDataset.append(line.strip())

    return dataTable, dataList, newDataset


def create_label_table(lines):
    label_table = {}
    new_instructions = []
    instruction_number = 0

    for line in lines:
        # Check if the line ends with a colon, indicating a label
        if line.endswith(":"):
            label = line[:-1].strip()  # Remove the colon and any whitespace
            label_table[label] = instruction_number  # Map the label to the current instruction number
            continue  # Skip to the next iteration without counting this line as an instruction

        # If it's not a label, add the instruction to the new list of instructions
        new_instructions.append(line)
        instruction_number += 1

    return label_table, new_instructions


def encode_program(lines, label_table, data_table):
    opGloss = {"add": "0000", "sub": "0000", "and": "0000", "or": "0000",
                "slt": "0000", "lw": "0001", "sw": "0010", "beq": "0011",
                "addi": "0101", "j": "0100", "bne": "0110", "jr": "0111",
                "jal": "1000"}
        
    functGloss = {"add": "010", "sub": "110", "and": "000", "or": "001",
                  "slt": "111"}
        
    rGloss = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100",
              "R5": "101", "R6": "110", "R7": "111"}
    
    finalCode = ""
    
    for idx, line in enumerate(lines):
        op = ""
        rs = ""
        rt = ""
        rd = ""
        funct = ""
        address = ""
        target = ""
        splitLine = [part.strip() for part in line.replace(",", " ").split() if part.strip()]
        opperation = splitLine[0]
        lenLine = len(splitLine)
        
        if opperation in functGloss:
            op = opGloss[opperation]
            funct = functGloss[opperation]
            if lenLine == 4:
                rs = rGloss[splitLine[2]]
                rt = rGloss[splitLine[3]]
                rd = rGloss[splitLine[1]]    
            else:
                print("ERROR: ")
                print(line)
        else:
            op = opGloss[opperation]
            if opperation == "addi":
                rs = rGloss[splitLine[2]]
                rt = rGloss[splitLine[1]]
                bit_length = 6 
                # binary_string = format(int(splitLine[3]), f'0{bit_length}b')
                integer_value = int(splitLine[3])

                # Convert to two's complement representation
                twos_complement = integer_value & ((1 << bit_length) - 1)

                # Format as binary string with leading zeros
                binary_string = format(twos_complement, f'0{bit_length}b')
                address = binary_string
            elif lenLine == 3:
                rs = "000"
                splitCommand = splitLine[2].split("(")
                if len(splitCommand) == 2:
                    rs = rGloss[splitCommand[1][:-1]]
                    bit_length = 6 
                    # binary_string = format(int(splitCommand[0]), f'0{bit_length}b')
                    integer_value = int(splitCommand[0])

                    # Convert to two's complement representation
                    twos_complement = integer_value & ((1 << bit_length) - 1)

                    # Format as binary string with leading zeros
                    binary_string = format(twos_complement, f'0{bit_length}b')
                    address = binary_string
                    rt = rGloss[splitLine[1]]
                else:
                    rt = rGloss[splitLine[1]]
                    bit_length = 6 
                    # binary_string = format(data_table[splitLine[2]], f'0{bit_length}b')
                    integer_value = int(data_table[splitLine[2]])

                    # Convert to two's complement representation
                    twos_complement = integer_value & ((1 << bit_length) - 1)

                    # Format as binary string with leading zeros
                    binary_string = format(twos_complement, f'0{bit_length}b')
                    address = binary_string

            elif lenLine == 2:
                if opperation == "jr":
                    op = opGloss[opperation]
                    rs = rGloss[splitLine[1]]
                    rt = "000"
                    rd = "000"
                    funct = "000"
                else:
                    op = opGloss[opperation]
                    bit_length = 12
                    # binary_string = format(label_table[splitLine[1]], f'0{bit_length}b')
                    integer_value = int(label_table[splitLine[1]])

                    # Convert to two's complement representation
                    twos_complement = integer_value & ((1 << bit_length) - 1)

                    # Format as binary string with leading zeros
                    binary_string = format(twos_complement, f'0{bit_length}b')

                    target = binary_string
                   
            elif lenLine == 4:
                op = opGloss[opperation]
                rs = rGloss[splitLine[2]]
                rt = rGloss[splitLine[1]]
                bit_length = 6 
                # binary_string = format(int(label_table[splitLine[3]]), f'0{bit_length}b')
                # Assuming label_table[splitLine[3]] returns a signed integer value
                integer_value = int(label_table[splitLine[3]])

                # Convert to two's complement representation
                twos_complement = (integer_value-(idx+1)) & ((1 << bit_length) - 1)

                # Format as binary string with leading zeros
                binary_string = format(twos_complement, f'0{bit_length}b')

                address = binary_string


        # Create a list of non-empty strings
        parts = [part for part in [op, rs, rt, rd, funct, address, target] if part]

        # Join the non-empty strings with spaces
        myString = " ".join(parts)
        
        finalCode = finalCode + myString + "\n"
    return finalCode
            



def post_process(encoded_program):
    lines = encoded_program.split("\n")
    myList = []
    for line in lines[:-1]:
        binaryString = line.replace(" ", "")
        decimal_number = int(binaryString, 2)
        hex_string = hex(decimal_number)[2:].upper()
        hex_string = hex_string.zfill(4)
        myList.append(hex_string + " ")
    return myList