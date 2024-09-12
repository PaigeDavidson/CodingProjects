# Paige Davidson
# CS1400 - MO1
# Assignment 3

import math

# user input
print("Welcome to the Social Situation Analyzer System")
print("Person One")
nameOne = input("    Enter your name: ")
posOne = posOneX, posOneY = eval(input("    Enter your position (x, y): "))
spaceOne = int(input("    Enter your personal space radius: "))
print("\nPerson Two")
nameTwo = input("    Enter your name: ")
posTwo = posTwoX, posTwoY = eval(input("    Enter your position (x, y): "))
spaceTwo = int(input("    Enter your personal space radius: "))

# distance variable
distance = math.sqrt((posOneX - posTwoX)**2 + (posOneY - posTwoY)**2)

# msg concatenation
msg = "\nSocial Situation Analysis Results \n"
# person test
msg += "    Person Test: "
if distance < spaceOne and distance < spaceTwo:
    msg += nameOne + " and " + nameTwo + " are in each other's personal space"
elif distance < spaceOne:
    msg += nameTwo + " is in " + nameOne + "'s personal space"
elif distance < spaceTwo:
    msg += nameOne + " is in " + nameTwo + "'s personal space"
else:
    msg += "Neither " + nameOne + " nor " + nameTwo + " is in the other's personal space"
msg += "\n"

# space test
msg += "    Space Test: "
if distance < (spaceOne + spaceTwo):
    msg += nameOne + " and " + nameTwo + "'s personal spaces overlap"
elif (distance + spaceTwo) < spaceOne:
    msg += nameTwo + "'s personal space is entirely inside " + nameOne + "'s personal space"
elif (distance + spaceOne) < spaceTwo:
    msg += nameOne + "'s personal space is entirely inside " + nameTwo + "'s personal space"
else:
    msg += nameTwo + " and " + nameOne + "'s personal spaces do not overlap"

# print statement
print(msg)
