from classes.faketimer import FakeTimer

def main():
    fakeTimer = FakeTimer()

    print("Welcome to the Fake Timer")

    done = False

    while not done:
        print("Menu")
        print("\t1) Seconds since timer reset")
        print("\t2) Reset timer")
        print("\t3) Quit")
        choice = eval(input("Make a selection: "))

        if choice == 1:
            print(format(fakeTimer.getElapsedTime(), ".2f") + " seconds since reset")
        elif choice == 2:
            print("Resetting Timer")
            fakeTimer.resetBaseTime()
        elif choice == 3:
            done == True

        print()

    print("Thanks for Playing!")


main()