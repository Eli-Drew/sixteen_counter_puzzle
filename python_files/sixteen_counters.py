"""
=======================================================================
Author:    Drew Rinker
Date:      04/25/19
IDE:       Python IDLE
Files:     sixteen_counters.py

Purpose:   This is a program that will develop a sequence to best
           solve the sixteen counter problem. It's purpose is to
           aid in finding an exact proof of the solution.
=======================================================================
"""
#=============================================================
def main():
    board = createBoard()
    displayBoard(board)
    board = singleMove(board)
    displayBoard(board)
#=============================================================
def createBoard():
    """This function creates our playing board.
        Values initialized to '0'."""
    rows = 4
    columns = 4
    playingBoard = []

    #for loop to create the board.
    for row in range(rows):
        playingBoard.append([0] * columns)

    return playingBoard
#=============================================================
def displayBoard(matrix):
    """This function displays a previously created matrix."""

    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[rowIndex])):
            print(matrix[rowIndex][colIndex], end = " ")
        print() #moving cursor to next line.
#=============================================================
def singleMove(matrix):
    """This function represents a single move on the board.
        It will take a 2x2 square on the board and flip all
        pieces to the other side. User defines a move by
        inputing the coordinates for top left corner of 2x2
        they want to flip."""
    
    #input will be in form (x,y)
    #input can be wrong but this is for me. 
    #so no complicated validation.
    try:
        x = int(input("Enter integer for x coordinate. "))
        y = int(input("Enter integer for y coordinate. "))
    except:
        print("Invalid input.")

    if matrix[x][y] == 0:
        matrix[x][y] = 1
    else:
        matrix[x][y] = 0
        
    if matrix[x][y+1] == 0:
        matrix[x][y+1] = 1
    else:
        matrix[x][y+1] = 0
        
    if matrix[x+1][y] == 0:
        matrix[x+1][y] = 1
    else:
        matrix[x+1][y] = 0
        
    if matrix[x+1][y+1] == 0:
        matrix[x+1][y+1] = 1
    else:
        matrix[x+1][y+1] = 0
    
    return matrix
#=============================================================

        
main()

    
