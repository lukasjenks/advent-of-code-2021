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
                solution = str(evaluateBoard(board, move))
    print("Part Two Solution Is:  " + solution)

# Takes all the 2D arrays representing the bingo sheets and the move to apply to each sheet
def makeMove(bingoSheet, move):
    for i in range (0, len(bingoSheet)):
        for j in range (0, len(bingoSheet[i])):
            if bingoSheet[i][j] == move:
                bingoSheet[i][j] = "-1"
                return True
    return False

# Takes a 2D array representing a bingo sheet and returns True if the sheet is a winner, False otherwise
def checkIfWinner(bingoSheet):
    # Any row or column with all -1's is a winner

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
    return False

# Takes a 2D array representing a bingo sheet and the move that was last made on said sheet, and returns the
# product of the sum of unmarked values and the value of the last move made
def evaluateBoard(bingoSheet, lastMove):
    sum = 0
    for i in range (0, len(bingoSheet)):
        for j in range (0, len(bingoSheet[i])):
            if bingoSheet[i][j] != "-1":
                sum = sum + int(bingoSheet[i][j])
    return sum * int(lastMove)

main()

# 4662 is answer for part one
# 12080 is answer for part two