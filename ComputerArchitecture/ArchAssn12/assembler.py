def main():
    # Defining the assembly file to read from
    filename = "sum_natural_numbers.asm"

    # Read all lines from the assembly file, and store them in a list
    with open(filename, "r") as infile:
        lines = infile.readlines()

    # Step 1: Preprocess the lines to remove comments and whitespace
    def preprocess_lines(lines):
        newList = []
        for line in lines:
            # Remove inline comments
            line = line.split('#')[0].strip()
            if line:  # Check if line is not empty after removing comments
                newList.append(line.strip())
        return newList
            
    lines = preprocess_lines(lines)

    # Step 2: Use the preprocessed program to build data table
    def build_data_table(lines):
        dataTable = {}
        dataList = []
        processedList = preprocess_lines(lines)

        # in the case of no header
        if ".data" not in lines and ".text" not in lines:
            return dataTable, dataList, processedList

        # if no .data tag
        elif ".data"  not in lines:
            mainIndex = processedList.index("main:")
            processedList = processedList[mainIndex:]
            return dataTable, dataList, processedList
        else:
            dataIndex = processedList.index(".data")
            mainIndex = processedList.index("main:")
            textIndex = processedList.index(".text")

            datas = processedList[dataIndex + 1:textIndex]
            for data in datas:
                split = data.split(":")

                dataTable.update({str(split[0]): str(datas.index(data))})

                dataList.append(split[1].strip())
            
            # get the instructions after main 
            processedList = processedList[mainIndex:]

            return dataTable, dataList, processedList
    
    data_table, data_list, lines = build_data_table(lines)
  

    # Step 3: Build a label table and strip out the labels from the code
    def build_label_table(lines):
        label_table = {}
        new_instructions = []
        line_index = 0  # Keep track of the instruction number

        for line in lines[:]:  # Iterate over a copy of the list
            if ":" in line:
                label, _ = line.split(":", 1)  # Split at the first occurrence of ":"
                label_table[label.strip()] = line_index
            else:
                instruction = line.strip()
                if instruction:  # Only add non-empty instructions
                    new_instructions.append(instruction)
                    line_index += 1  # Increment instruction number

        return label_table, new_instructions

    label_table, lines = build_label_table(lines)

    # Step 4: Encode the program into a list of binary strings
    def register_to_binary(reg):
        reg = reg.strip().strip("R")
        code = format(int(reg), "03b")
        return code
    
    def dec_to_bin(dec, numBits):
        if dec < 0:
            # Convert negative number to two's complement form
            binary_string = f"{(1 << numBits) + dec:0{numBits}b}"
        else:
            binary_string = bin(dec)[2:]
            # Pad with zeros to ensure the binary string has the specified number of bits
            binary_string = binary_string.zfill(numBits)
        return binary_string

    def encode_instruction(line_num, instruction, label_table, data_table):
            encodedLine = []
            split = instruction.split(" ", 1)

            splitAgain = split[1].split(",")

            def R(op, funct, output):
                if op == "":
                    op = "0000"
                rs = register_to_binary(splitAgain[1])
                rt = register_to_binary(splitAgain[2])
                rd = register_to_binary(splitAgain[0])
                output += [op," ", rs, " ",rt, " ",rd, " ",funct]

            def I(op, imm, output):
                rs = register_to_binary(splitAgain[1])
                rt = register_to_binary(splitAgain[0])
                if imm == "immediate":
                    immediateAdress = dec_to_bin(int(splitAgain[2]), 6)
                elif imm == "offset":
                    offset = label_table.get(splitAgain[2].strip()) - line_num
                    immediateAdress = dec_to_bin(offset, 6)
                output += [op, " ", rs, " ",rt, " ",immediateAdress]


            def J(op, output):
                index = label_table[splitAgain[0].strip()]
                output += [op, " ", dec_to_bin(index, 12)]

            match split[0]:
                case "add":
                    R("", "010", encodedLine)
                case "sub":
                    R("", "110", encodedLine)
                case "and":
                    R("", "000", encodedLine)
                case "or":
                    R("", "001", encodedLine)
                case "slt":
                    R("", "111", encodedLine)
                case "addi":
                    I("0101", "immediate", encodedLine)
                case "beq":
                    I("0011", "offset", encodedLine)
                case "bne":
                    I("0110", "offset", encodedLine)
                case "lw":
                    rt = register_to_binary(splitAgain[0])
                    if splitAgain[1].strip() in data_table:
                        rs = "000"
                        offset = dec_to_bin(int(data_table[splitAgain[1].strip()]), 6)
                    else:
                        reg = splitAgain[1].split("(")
                        rs = register_to_binary(reg[1].strip(")"))
                        offset = dec_to_bin(int(reg[0]), 6)
                    encodedLine += ["0001", " ", rs, " ", rt, " ", offset]
                case "sw":
                    rt = register_to_binary(splitAgain[0])
                    if splitAgain[1].strip() in data_table:
                        rs = "000"
                        offset = dec_to_bin(int(data_table[splitAgain[1].strip()]), 6)
                    else:
                        reg = splitAgain[1].split("(")
                        rs = register_to_binary(reg[1].strip(")"))
                        offset = dec_to_bin(int(reg[0]), 6)
                    encodedLine += ["0010", " ", rs, " ", rt, " ", offset]
                case "j":
                    J("0100", encodedLine)
                case "jr":
                    encodedLine += ["0111", " ", register_to_binary(splitAgain[0]), " ", "000"," ",  "000", " ","000"]
                case "jal":
                    J("1000", encodedLine)
                case _:
                    raise Exception("Invalid instruction: " + split[0])
            
            return "".join(encodedLine)
    
    def encode_program(lines, label_table, data_table):
        instructions = []
        for line in lines:
            instructions.append(encode_instruction(lines.index(line) + 1, line, label_table, data_table))
        return instructions 
    
    encoded_program = encode_program(lines, label_table, data_table)

    # Step 5: Convert the strings to hexadecimal and write them to a file
    def post_process(lines):
        hexStrings = ""
        for line in lines:
            line = line.replace(" ", "")
            dec = int(line, 2)
            hexStrings += format(dec, '04x')
            hexStrings += " "

        return hexStrings
    
    def post_process_data(lines):
        hexStrings = ""
        for line in lines:
            line = line.replace(" ", "")
            dec = int(line)
            hexStrings += format(dec, '04x')
            hexStrings += " "

        return hexStrings
    
    hex_program = post_process(encoded_program)

    hex_data = post_process_data(data_list)

    # program hex
    with open("program.hex", "w") as outfile:
        outfile.write("v3.0 hex words addressed\n00: ")
        outfile.writelines(hex_program)

    # Step 6: Convert the data list to hexadecimal and write it to a file
        # data hex
    with open("data.hex", "w") as outfile:
        outfile.write("v3.0 hex words addressed\n00: ")
        outfile.writelines(hex_data)

main()
