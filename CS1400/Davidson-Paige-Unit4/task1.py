# Paige Davidson
# CS1400 - MO1
# Assignment 4

def makeNumberPyramid(number):
    message = ""
    for i in range(0, number + 1):
        rowOfText = ""
        width = (len(str(number)) + 1) * number
        center = "^" + str(width) + ""
        for j in range(0, i):
            if i != 0:
                rowOfText += str(i)
                rowOfText += " "
        message += format(rowOfText, str(center)) + "\n"
    return str(message)


def main():
    rowNumber = eval(input("Enter the number of rows: "))
    print(makeNumberPyramid(rowNumber))


main()
