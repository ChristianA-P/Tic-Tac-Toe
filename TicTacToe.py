# Christian Alves-Patterson
# Text-based tic-tac-toe game 

# Use of random number generator
import random
winner = None
gameRunning = True
board: list = ["   ","   ","   ",
        "   ","   ","   ",
        "   ","   ","   "]

# Ask user for name and symbol
Username: str = input("Name: ")
userSymbol: str = input("Please select your symbol, X or O: ")
currentPlayer = Username

# Welcome player to game
print("\n Welcome to single player tic-tac-toe,", Username)
print('==================================== \n')

# Print board for tictactoe game
def printBoard(board):
    print("\n" + board[0] + "|" + board[1] + "|" + board[2])
    print("---|---|---")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("---|---|---")
    print(board[6] + "|" + board[7] + "|" + board[8])

# User chooses symbol
while userSymbol != "X" and userSymbol != "O":
    print("Oops! You chose an invalid symbol...")
    userSymbol = input("Please try again. ")
if userSymbol == "X":
    cpuSymbol = "O"
else:
    cpuSymbol = "X"

# User inputs the position they wish to place their symbol
def userPosition(board):
    pos = int(input("\n Please select a position, 1-9: "))
    while pos < 1 or pos > 9:
        print("That is not a valid position...")
        pos = int(input("\n Please try again "))

    while board[pos - 1] != "   ":
        print("That position is taken")
        pos = int(input("\n Please try again "))
    board[pos - 1] = f" {userSymbol} "

# CPU decides where to place its symbol with RNG
def cpuPosition(board):
    while currentPlayer == "CPU":
        cpupos = random.randint(0,8)
        if board[cpupos] == "   ":
            board[cpupos] = f" {cpuSymbol} "
            switchPlayer()

# Checks if there is a victory in any row of the game board
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "   ":
        if board[0] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True
    elif board[3] == board[4] == board[5] and board[3] != "   ":
        if board[3] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True
    elif board[6] == board[7] == board[8] and board[6] != "   ":
        if board[6] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True

# Checks if there is a victory in any column of the game board
def checkCol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "   ":
        if board[0] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True
    elif board[1] == board[4] == board[7] and board[1] != "   ":
        if board[1] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True
    elif board[2] == board[5] == board[8] and board[2] != "   ":
        if board[2] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True

# Checks if there is a victory in any diagonal of the game board
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "   ":
        if board[0] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True
    elif board[2] == board[4] == board[6] and board[2] != "   ":
        if board[2] == f" {userSymbol} ":
            winner = Username
            return True
        else:
            winner = "CPU"
            return True

# Checks if there is a draw on the game board
def checkDraw(board):
    global gameRunning
    if "   " not in board:
        printBoard(board)
        print("Game Draw!")
        gameRunning = False

# Switches to player that goes next
def switchPlayer():
    global currentPlayer
    if currentPlayer == Username:
        currentPlayer = "CPU"
    else:
        currentPlayer = Username

# Checks for any wins on the board
def checkWin():
    global gameRunning
    if checkRow(board) or checkCol(board) or checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner} ")
        gameRunning = False

while gameRunning:
    printBoard(board)
    userPosition(board)
    checkWin()
    checkDraw(board)
    switchPlayer()
    cpuPosition(board)
    checkWin()
    checkDraw(board)


