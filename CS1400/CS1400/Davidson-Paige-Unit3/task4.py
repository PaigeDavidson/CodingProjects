# Paige Davidson
# CS1400 - MO1
# Assignment 3

import random

continueLoop = "yes" or "YES" or "Yes" or "yEs" or "yeS" or "YEs" or "YeS" or "yES"

# create probabilities
while continueLoop == "yes" or "YES" or "Yes" or "yEs" or "yeS" or "YEs" or "YeS" or "yES":
    oneElephant = 0
    twoElephant = 0
    for i in range(100000):
        elephant1 = random.randint(1, 6)
        elephant2 = random.randint(1, 6)
        zookeeper = random.randint(1, 6)
        if elephant2 == zookeeper or elephant1 == zookeeper:
            oneElephant += 1
            if elephant2 == zookeeper and elephant1 == zookeeper:
                twoElephant += 1
# calculate percentages
    onePen = (oneElephant / 100000) * 100
    twoPen = (twoElephant / oneElephant) * 100
    percentages = format(onePen, ".2f")
    percentages += "%"
    percentages += "\n"
    percentages += format(twoPen, ".2f")
    percentages += "%"
    print(percentages)

# who was right?
    if abs(onePen - (100/3)) < 2 and abs(twoPen - (100/6)) < 2:
        print("Zookeeper was correct")
    else:
        print("Custodian was correct")

    # end loop
    continueLoop = input("Run the simulation again? (yes or no): ")

# end message
print("Simulation Ended")
