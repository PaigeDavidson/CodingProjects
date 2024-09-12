# Paige Davidson
# CS1400 - MO1
# Assignment 3

from random import seed
from random import randint
import time

# start timer
sTime = time.time()
# variables for total loops and loop efficiency
totalLoops = 0
numberNumber = 0
# loops
for theNumber in range(1, 10001):
    facSum = 0
    for posFactor in range(1, int(theNumber ** (1/2)) + 1):
        totalLoops += 1
        if theNumber % posFactor == 0:
            facSum += posFactor
            if posFactor != theNumber / posFactor and posFactor != 1:
                facSum += theNumber / posFactor
        else:
            facSum += 0
    seed(facSum)
    result = randint(0, theNumber)
    if result == theNumber and facSum != 0:
        numberNumber += 1
        print("Fluky Number:" + str(theNumber))
    if numberNumber == 7:
        break
# end time
eTime = time.time()
totalTime = eTime - sTime
time = format(totalTime, ".2f")
time += " seconds"

# time and total loops
print("Total Time: " + time)
print("Total Loops: " + str(totalLoops))
