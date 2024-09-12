# Paige Davidson
# CS1400 - MO1
# Assignment 6

from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(Deck.draw(deck))  # Single line

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            playerHand = sortByTitle(playerHand)  # Single line
        elif choice == 3:
            playerHand = sortByGang(playerHand)  # Single line
        elif choice == 4:
            search(playerHand)  # Single line
        elif choice == 5:
            done = True  # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    print("Your Hand")
    for i in hand:
        print(i)  # Not a single line. The entire function body

# Add other functions you need below
def sortByTitle(hand):
    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(0, len(hand) - 1):
            if TITLE.index(hand[i].getTitle()) > TITLE.index(hand[i + 1].getTitle()):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True
    print("Bubble sort by title", end="")
    thinking()
    return hand

def sortByGang(hand):
    for i in range(len(hand) - 1):
        currentMinIndex = i
        for j in range(i + 1, len(hand)):
            if hand[currentMinIndex] < hand[j]:
                currentMinIndex = j
        if currentMinIndex != i:
            hand[i], hand[currentMinIndex] = hand[currentMinIndex], hand[i]

    print("Selection sort by gang", end="")
    thinking()
    return hand

def search(hand):
    # title list
    print("Titles")
    print("\t(1) One")
    print("\t(2) Two")
    print("\t(3) Three")
    print("\t(4) Four")
    print("\t(5) five")
    print("\t(6) Six")
    print("\t(7) Seven")
    print("\t(8) Eight")
    print("\t(9) Nine")
    print("\t(10) Ten")
    print("\t(11) Baker")
    print("\t(12) Jester")
    print("\t(13) Page")
    print("\t(14) Scribe")
    print("\t(15) Squire")
    print("\t(16) Armorer")
    print("\t(17) Marshal")
    title = eval(input("Choose a Title: "))
    titleKey = TITLE[title-1]

    # gang list
    # print()
    print("Gang")
    print("\t(1) Jets")
    print("\t(2) Pollos")
    print("\t(3) Slugs")
    print("\t(4) Yokels")
    print("\t(5) Keiths")
    print("\t(6) Elbows")
    gang = eval(input("Choose a Gang: "))
    gangKey = GANG[gang-1]

    # list = convertCardToId(title, gang)

    # sort hand
    sortByTitle(hand)

    # binary search for card in hand
    print("Binary search for " + titleKey + " of " + gangKey, end="")
    thinking()
    key = convertCardToId(titleKey, gangKey)
    low = 0
    high = len(hand)
    present = False
    for i in range(len(hand)):
        if key == hand[i].getID():
            present = True
            break

    # message indicating whether the card is in the hand
    if present:
        print("Congrats! You have that card")
    else:
        print("Sorry. You do not have that card")


main()
