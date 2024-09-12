# Paige Davidson
# CS1400 - MO1
# Assignment 7

from modules.memorycard import MemoryCard
from random import shuffle


class GameBoard:
    def __init__(self, cols, rows):  # Gameboard(cols, rows)
        self.__columns = cols
        self.__rows = rows
        self.__board = []
        count = 0
        for row in range(rows):
            rowLst = []
            for col in range(cols):
                rowLst.append(MemoryCard(count))
                count += 1
            shuffle(rowLst)
            self.__board.append(rowLst)

    def getBoard(self):
        board = ""
        board += "\n"
        board += "  | "
        for i in range(self.__columns):
            board += str(i + 1) + " | "
        for i in range(self.__rows):
            board += "\n"
            board += "----" * self.__columns + "---"
            board += "\n"
            board += str(i + 1) + " | "
            for j in range(self.__columns):
                board += self.__board[i][j].displayCard()
                board += " | "
        board += "\n"
        board += "----" * self.__columns + "---"
        return board

    def flipCard(self, xPos, yPos):
        self.__board[yPos - 1][xPos - 1].toggleFlipped()

    def isCardFlipped(self, xPos, yPos):
        if self.__board[yPos - 1][xPos - 1].isFlipped():
            return True
        else:
            return False

    def isMatch(self, pos1, pos2):
        if self.__board[pos1[1] - 1][pos1[0] - 1].getValue() == self.__board[pos2[1] - 1][pos2[0] - 1].getValue():
            return True
        else:
            return False

