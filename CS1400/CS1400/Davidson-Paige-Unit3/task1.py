# Paige Davidson
# CS1400 - MO1
# Assignment 3

# random number generated
import random
compNumber = random.randint(1, 10)


# user input
print("Welcome to the Guessing Game")
print("The Computer has picked a numer from 1 - 10. Try to match it.")
userNumber = int(input("What number do you choose (1 - 10): "))

# msg
msg = "You picked " + str(userNumber) + ", and the actual number was " + str(compNumber) + "."
msg += "\n"
if userNumber == compNumber:
    msg += "Honored to play with you, Master."
elif userNumber == compNumber + 1 or userNumber == compNumber - 1:
    msg += "You are a worthy opponent, Knight."
elif userNumber == compNumber + 2 or userNumber == compNumber - 2:
    msg += "You have much to learn, Padawan."
elif userNumber == compNumber + 3 or userNumber == compNumber - 3:
    msg += "Youngling, your time will come."
else:
    msg += "Keep working hard in the Service Corps."

# print
print(msg)
