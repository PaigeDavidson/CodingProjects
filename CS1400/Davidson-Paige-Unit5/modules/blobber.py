# Paige Davidson
# CS1400 - MO1
# Assignment 5

import time
from math import pi

class Blobber:
    def __init__(self, name, color, radius, height):
        self.__radius = radius
        self.__originalRadius = radius
        self.__height = height
        self.__color = color.lower()
        self.__name = name[0].upper() + name[1:].lower()
        self.__startTime = time.time()
        self.originalVolume = self.blobberVolume()


    def getcolor(self):
        return self.__color

    def setcolor(self, color):
        self.__color = color.lower()

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name[0].upper() + name[1:].lower()

    def blobberVolume(self):
        currentRadius = (self.__radius - ((time.time() - self.__startTime) * 0.002) * self.__originalRadius)
        self.__radius = currentRadius
        self.__startTime = time.time()
        blobberVolume = (pi * (currentRadius ** 2)) * self.__height
        return blobberVolume

    def blobberHappiness(self):
        happinessLevel = self.blobberVolume() / self.originalVolume
        return happinessLevel

    def feedBlobber(self, food):
        currentRadius = (self.__radius - (self.__originalRadius * (time.time() - self.__startTime) * 0.002))
        newRadius = (currentRadius + food)
        self.__radius = newRadius
        self.__startTime = time.time()
        return newRadius

    def vitalsOK(self):
        if .90 <= self.blobberHappiness() <= 1.10:
            return self.blobberHappiness(), True
        else:
            return self.blobberHappiness(), False

    def blobberSpeak(self):
        speak1 = "My name is " + str(self.getname()) + ", and I am " + str(self.getcolor())
        speak2 = "\nMy current Happiness level is " + str(format(self.blobberHappiness(), ".2%"))
        speak = speak1 + speak2
        return speak