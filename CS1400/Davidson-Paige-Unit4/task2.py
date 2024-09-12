# Paige Davidson
# CS1400 - MO1
# Assignment ??

#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####


def main():
    #### Add Code to get input from user###
    startX = eval(input("Enter Starting Point X: "))
    startY = eval(input("Enter Starting Point Y: "))
    width = input("Enter Height: ")
    height = input("Enter Width: ")
    #### End Add Code to get input from user####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()
