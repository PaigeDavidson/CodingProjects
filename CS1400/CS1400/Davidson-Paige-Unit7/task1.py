# Paige Davidson
# CS1400 - MO1
# Assignment 7

from modules.gameboard import GameBoard
# This import gives some functionality if your run the program from the commandline. See the video in the assignment
# for instructions. Running in the terminal makes the game board play more like a game instead of scrolling and
# printing a new board every time.
# You'll need to comment a line down below in the printGameBoard() function if using PyCharm
# import os


def main():
    playerTurn = 0  # Keep track of whose turn it is
    print("Welcome to Memory\n")
    # Get the Board Size
    cols = int(input("Enter the number of columns on the board: "))
    rows = int(input("Enter the number of rows on the board: "))
    # Get the number of players
    playerCount = int(input("Enter the number of players: "))
    scores = [0] * playerCount
    # Create the MemoryBoard object
    memoryBoard = GameBoard(cols, rows)
    # Game loop
    winner = False
    while not winner:
        selectedCards = []  # Track the cards the current player selected
        printGameBoard(scores, memoryBoard.getBoard())
        # Each turn is two card flips

        for i in range(2):
            xPos, yPos = eval(input("Player " + str(playerTurn + 1) + " choose a card to flip: "))
            memoryBoard.flipCard(xPos, yPos)
            printGameBoard(scores, memoryBoard.getBoard())
            selectedCards.append((xPos, yPos))
        # Player goes again if they get a match
        if memoryBoard.isMatch(selectedCards[0], selectedCards[1]):
            print("You got a match!")
            scores[playerTurn] += 1
            winner = sum(scores) == cols * rows / 2

            # If the game is over show a different message
            if winner:
                print("Hit Enter to Continue")
            else:
                input("Player " + str(playerTurn) + " hit Enter to go again.")
                # you had to add a + 1 to player turn when you modified line 39
        else:
            memoryBoard.flipCard(selectedCards[0][0], selectedCards[0][1])
            memoryBoard.flipCard(selectedCards[1][0], selectedCards[1][1])
            print("No Match")
            if playerTurn == playerCount:
                playerTurn -= 1
            else:
                playerTurn += 1
            input("Hit Enter for Player " + str(playerTurn + 1))
    # Find the winning score value
    highScore = max(scores)
    # Check for a tie/winner
    if scores.count(highScore) > 1:
        print("The following players tied: ", end="")
        for i in range(len(scores)):
            if scores[i] == highScore:
                print(i, end=" ")
    else:
        print("The winner is player " + str(scores.index(highScore) + 1))
# Print the scoreboard and game-board


def printGameBoard(scores, board):
    # os.system('cls||clear')  # Comment this out if running in PyCharm
    for i in range(len(scores)):
        print("Player " + str(i + 1) + ": " + str(scores[i]))
    print()
    print(board)


main()
