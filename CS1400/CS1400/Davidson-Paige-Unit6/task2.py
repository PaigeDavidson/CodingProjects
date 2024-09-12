# Paige Davidson
# CS1400 - MO1
# Assignment 6

def big(lst1):
    didSwap = True
    while didSwap:
        didSwap = False
        count = 1
        for i in range(len(lst1) - count):
            if lst1[i] > lst1[i + 1]:
                lst1[i], lst1[i + 1] = lst1[i + 1], lst1[i]
            count += 1


def main():
    lst1 = []
    done = False
    while not done:
        numbers = input("Enter a Number: ")
        if numbers == "":
            done = True
        else:
            lst1.append(int(numbers))

    # number os values
    numValues = len(lst1)

    # max value
    big(lst1)
    maxVal = lst1[len(lst1) - 1]

    # min value
    # minVal = min(lst1)

    # Sum of all values
    total = 0
    for i in lst1:
        total += int(i)

    # average value
    average = total / numValues

    # print statements
    print("Number of values entered: " + str(numValues))
    print("Maximum value: " + str(maxVal))
    print("Minimum Value: " + str(min(lst1)))
    print("Sum of all values: " + str(total))
    print("Average Value: " + str(format(average, ".2f")))


main()
