from modules.gronkyutil import TITLE, GANG

class Card:
    def __init__(self, id):
        self.__id = id

    def getTitle(self):
        return TITLE[self.__id % 17] # Do not use a numeric literal

    def getGang(self):
        return GANG[self.__id // 17] # Do not use a numeric literal

    def getID(self):
        return self.__id

    # Add two dunder methods below to meet assignment requirements
    def __repr__(self):
        return self.getTitle() + " of " + self.getGang()

    def __lt__(self, other):
        if self.__id > other.__id:
            return True
        else:
            return False
