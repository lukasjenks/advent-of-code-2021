import re

# Void Main Function
def main():
    puzzleInput = getPuzzleInput("./day4PuzzleInput.txt")
    getSolutionOne(puzzleInput)
    getSolutionTwo(puzzleInput)
    return

# Takes a file path and returns a string with the files contents
def getPuzzleInput(path):
    #Load contents of file into a string
    with open(path) as f:
        fileContent = f.read()
    f.close()
    return fileContent

# Takes a string containing the puzzle file input and returns the solution to part one
def getSolutionOne(puzzleInput):
    # First \n\n separates the moves from the bingo sheets
    movesAndBoards = puzzleInput.split("\n\n", 1)
    moves = movesAndBoards[0].split(",")
    # Each bingo sheet is separated by two newlines
    boards = movesAndBoards[1].split("\n\n")
    for i in range (0, len(boards)):
        boards[i] = boards[i].split("\n");
        for j in range(0, len(boards[i])):
            # If you give split no argument, it splits on any amount of whitespace,
            # which is exactly what we want to do here as whitepsace is inconsistent
            boards[i][j] = boards[i][j].split()

    # For each move in moves, make the move on each board in boards and check if the board is a winner after the move
    for move in moves:
        for board in boards:
            makeMove(board, move)
            if checkIfWinner(board):
                #for i in range(0, len(board)):
                    #print(board[i])
                #print("\n")
                #print(move)
                print("Part One Solution Is:  " + str(evaluateBoard(board, move)))
                return

# Takes a string containing the puzzle file input and returns the solution to part two
def getSolutionTwo(puzzleInput):
    # First \n\n separates the moves from the bingo sheets
    movesAndBoards = puzzleInput.split("\n\n", 1)
    moves = movesAndBoards[0].split(",")
    # Each bingo sheet is separated by two newlines
    boards = movesAndBoards[1].split("\n\n")
    for i in range (0, len(boards)):
        boards[i] = boards[i].split("\n");
        for j in range(0, len(boards[i])):
            # If you give split no argument, it splits on any amount of whitespace,
            # which is exactly what we want to do here as whitepsace is inconsistent
            boards[i][j] = boards[i][j].split()
    
    # For each move in moves, make the move on each board in boards and check if the board is a winner after the move
    wonBoards = {};
    for move in moves:
        for board in boards:
            makeMove(board, move)
            if checkIfWinner(board) and wonBoards.get(boards.index(board)) == None:
                wonBoards[boards.index(board)] = True
                print("Part Two Solution Is:  " + str(evaluateBoard(board, move)))

# Takes all the 2D arrays representing the bingo sheets and the move to apply to each sheet
def makeMove(bingoSheet, move):
    for i in range (0, len(bingoSheet)):
        for j in range (0, len(bingoSheet[i])):
            if bingoSheet[i][j] == move:
                bingoSheet[i][j] = "-1"
                return True
    return False

def checkIfWinner(bingoSheet):
    # Any row, column, or diagonal with all -1's is a winner

    # Check rows
    for i in range (0, len(bingoSheet)):
        if bingoSheet[i].count("-1") == len(bingoSheet[i]):
            return True

    # Check columns
    for i in range (0, len(bingoSheet)):
        column = []
        for j in range (0, len(bingoSheet)):
            column.append(bingoSheet[j][i])
        if column.count("-1") == len(column):
            return True

    # Check diagonals
    # Top left to bottom right
    #diagonal = []
    #for i in range (0, len(bingoSheet)):
    #    diagonal.append(bingoSheet[i][i])
    #if diagonal.count("-1") == len(diagonal):
    #    return True

    # Top right to bottom left
    #diagonal = []
    #for i in range (0, len(bingoSheet)):
    #    diagonal.append(bingoSheet[i][len(bingoSheet) - 1 - i])
    #if diagonal.count("-1") == len(diagonal):
    #    return True

    return False

def evaluateBoard(bingoSheet, lastMove):
    sum = 0
    for i in range (0, len(bingoSheet)):
        for j in range (0, len(bingoSheet[i])):
            if bingoSheet[i][j] != "-1":
                sum = sum + int(bingoSheet[i][j])
    return sum * int(lastMove)

main()

# 22554 is too high an answer for part 1
# 1125 is too low for part 2
# 4589 is too low for part 2
# 21576 is too high for part 2