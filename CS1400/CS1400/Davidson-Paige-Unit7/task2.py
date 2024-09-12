# Paige Davidson
# CS1400 - MO1
# Assignment 7

from random import randint

# Remember how to use this kind of variable?
count = 0


def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)

    numPos = binarySearch(numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))


def aggienacci(value):
    if value == 0:
        return 0  # base case
    if value == 1:
        return 1  # base case
    if value == 2:
        return 2
    else:
        return (aggienacci(value - 3) + aggienacci(value - 2)) / aggienacci(value - 1)


def binarySearch(numList, key):
    low = 0
    high = len(numList) - 1
    return binarySearchRecursive(numList, key, low, high)


def binarySearchRecursive(numList, key, low, high):
    global count
    count += 1
    if low > high:  # base case
        return -1
    mid = (low + high) // 2
    if key == numList[mid]:
        return mid
    elif key < numList[mid]:
        return binarySearchRecursive(numList, key, low, mid - 1)
    else:
        return binarySearchRecursive(numList, key, mid + 1, high)


main()
