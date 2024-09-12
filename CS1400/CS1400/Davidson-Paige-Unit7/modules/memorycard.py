# Paige Davidson
# CS1400 - MO1
# Assignment 7

class MemoryCard:
    def __init__(self, idNumber):  # MemoryCard(idNumber)
        self.__idNumber = idNumber
        self.__faceUp = False

    def getValue(self):
        val = (self.__idNumber // 2) + 33
        return val

    def toggleFlipped(self):
        self.__faceUp = not self.__faceUp

    def isFlipped(self):
        return self.__faceUp

    def displayCard(self):
        if self.isFlipped():
            return chr(self.getValue())
        else:
            return " "
