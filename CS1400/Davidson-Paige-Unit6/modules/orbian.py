# Paige Davidson
# CS1400 - MO1
# Assignment 6

from math import pi
from random import shuffle  # Hint hint
from random import randint
import time

class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()
        # This is the only variable
        self.__adult = False

    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True
    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######

    def __getHeadRadius(self):
        return self.__HEAD_RADIUS

    def __getBodyRadius(self):
        return self.__BODY_RADIUS

    def __getBodyHeight(self):
        return self.__BODY_HEIGHT

    def getAge(self):
        return int(self.__BIRTH_TIME % 5)

    def getName(self):
        name = self.__NAME
        name = name.capitalize()
        return name

    def getVolume(self):
        return int(self.__getHeadVolume() + self.__getBodyVolume())

    def __len__(self):
        return int(self.__getBodyHeight() + (self.__getHeadRadius() * 2))

    def __add__(self, other):
        headRadius = (self.__getHeadRadius() + other.__getHeadRadius()) / 4
        bodyRadius = (self.__getBodyRadius() + other.__getBodyRadius()) / 4
        bodyHeight = (self.__getBodyHeight() + other.__getBodyHeight()) / 8
        length = int((len(self.getName()) + len(other.getName())) / 2)
        name = ""
        parent = []
        for i in self.getName():
            parent.append(i)
        for i in other.getName():
            parent.append(i)
        shuffle(parent)
        for i in range(0, length):
            name += parent[i]
        return Orbian(name, headRadius, bodyRadius, bodyHeight)

    def __gt__(self, other):
        if self.getVolume() > other.getVolume():
            return True
        else:
            return False


