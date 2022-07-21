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
from sqlalchemy import false, true


def create_board():
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
def display_board(matrix):
    """This function displays a previously created matrix."""

    # this loop prints it prettier.
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            print(matrix[row_index][col_index], end = " ")
        print() #moving cursor to next line.

    # # this loop is a little uglier but faster.
    # for row in range(len(matrix)):
    #     print(matrix[row])
#=============================================================
def single_move(matrix):
    """This function represents a single move on the board.
        It will take a 2x2 square on the board and flip all
        pieces to either a 0 or 1 depending on what the current piece is.
        User defines a move by inputing the coordinates for top left corner 
        of 2x2 they want to flip."""
    
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
def check_if_won(board_matrix):

    break_out_of_loop_flag = False
    previous_piece = None

    for row in board_matrix:
        # print(row)
        if previous_piece == 1:
            previous_piece = 0
        elif previous_piece == 0:
            previous_piece = 1
        else: 
            previous_piece = previous_piece

        for space in row:
            # print(space)
            if space == previous_piece:
                print("Haven't won yet.")
                # break_out_of_loop_flag = True
                # break
                return False
            previous_piece = space

        if break_out_of_loop_flag == True:
            break
    return True


#=============================================================
def main():

    has_won = False
    board = create_board()

    while not has_won:
    
        display_board(board)
        board = single_move(board)
        display_board(board)
        has_won = check_if_won(board)

    print("Congrats!")



#=============================================================

# if __name__ == "__main__":
main()

    
