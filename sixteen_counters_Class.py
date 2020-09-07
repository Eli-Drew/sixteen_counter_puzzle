"""
=======================================================================
Author:    Drew Rinker
Date:      04/25/19
IDE:       Python IDLE
Files:     sixteen_counters.py

Purpose:   This is a program that will develop a sequence to best
           solve the sixteen counter problem. It's purpose is to
           aid in finding an exact proof of the solution. Right now
           it's just a user input game with no algorithm to solve it.

           Right now, I'm working find the fewest amount of moves
           required to win. 
=======================================================================
"""

class CounterBoard(object):
    """Creates a 4x4 game board. Various methods with a
        single move function for playing the game."""
    
    def __init__(self):
        self.x = 4
        self.y = 4
        self.board = self.createBoard(4,4)

    def getX(self):
        """Returns x coordinate."""
        return self.x

    def getY(self):
        """Returns y coordinate."""
        return self.y

    def __len__(self):
        """Returns the amount of board elements."""
        count = 0
        for rowIndex in range(len(self.board)):
            for colIndex in range(len(self.board[rowIndex])):
                count += 1
        return count
                

    def createBoard(self,x,y):
        """Creates a gameboard with the x and y parameters."""
        rows = self.x
        columns = self.y
        board = []
        for row in range(rows):
            board.append([0] * columns)

        return board

    def displayBoard(self,count):
        """Displays the game board."""
        print(" " *7 + "Column    Moves: " + str(count))
        print(" " *7 + "0 1 2 3\n")
        matrix = self.board
        for rowIndex in range(len(matrix)):
            print("Row:" + str(rowIndex)+ " ", end = " ")
            for colIndex in range(len(matrix[rowIndex])):
                print(matrix[rowIndex][colIndex], end = " ")
            print() # move cursor to next line.


    def isGameWonOption1(self):
        """Compares the gameboard to a correct version of the gameboard."""
        correctBoard1 = [[0,1,0,1],
                         [1,0,1,0],
                         [0,1,0,1],
                         [1,0,1,0]]

        board = self.board
        gameWon = True
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[rowIndex])):
                if board[rowIndex][colIndex] != \
                   correctBoard1[rowIndex][colIndex]:
                    return False
                
        return gameWon

    def isGameWonOption2(self):
        """Compares the gameboard to a correct version of the gameboard."""
        correctBoard2 = [[1,0,1,0],
                         [0,1,0,1],
                         [1,0,1,0],
                         [0,1,0,1]]

        board = self.board
        gameWon = True
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[rowIndex])):
                if board[rowIndex][colIndex] != \
                   correctBoard2[rowIndex][colIndex]:
                    return False

        return True

    def singleMove(self, x, y):
        """This function represents a single move on the board.
            It will take a 2x2 square on the board and flip all
            pieces to the other side. User defines a move by
            inputing the coordinates for top left corner of 2x2
            they want to flip."""

        if self.board[x][y] == 0:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0
            
        if self.board[x][y+1] == 0:
            self.board[x][y+1] = 1
        else:
            self.board[x][y+1] = 0
            
        if self.board[x+1][y] == 0:
            self.board[x+1][y] = 1
        else:
            self.board[x+1][y] = 0
            
        if self.board[x+1][y+1] == 0:
            self.board[x+1][y+1] = 1
        else:
            self.board[x+1][y+1] = 0
        
        return self.board

       
def main():
    """I'm thinking about moving the 'playing' functionality to
        a method in the CounterBoard Class so I can create several
        objects and 'play' those objects when I create a CounterBoard
        object in the shell. (Seems like it would help with the GUI
        too."""
    valid_input = [0,1,2]
    count = 0 
    gameOver = False
    game = CounterBoard()
    game.displayBoard(count)

    while (not gameOver):
        while True:
            print()
            x = int(input("Enter Row Number: "))
            y = int(input("Enter Column Number: "))
            if x in valid_input and y in valid_input:
                break
            else:
                print("Out of range or invalid input.")
                continue

        print("=" * 25)
        
        game.singleMove(x,y)
        count += 1
        game.displayBoard(count)
        
        gameOver1 = game.isGameWonOption1()
        gameOver2 = game.isGameWonOption2()

        if gameOver1 or gameOver2:
            print("\n" + "You Won in " + str(count) + " moves!!")
            break
        else:
            continue

if __name__ == "__main__":
    main()     
    
