"""
=======================================================================
Author:     Drew Rinker
Date:       05/05/19
IDE:        IDLE
Files:      sixteen_counters_Class.py

Purpose:    This file just creates a gui for the logic game.
=======================================================================
"""
from tkinter import *
from sixteen_counters_Class import CounterBoard

class LogicGame(Frame):
    """This provides and event driven GUI for the game."""

    def __init__(self, game):
        """Constructs the window and its widgets."""
        Frame.__init__(self)
        self.master.title("Logic Game")
        self.grid()
        self.game = game

        #create canvas
        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = Canvas(self, width = self.canvas_width,
                             height = self.canvas_height, bg = "#00ffff")
        self.canvas.grid()

        #creating the playing tiles.
        self.ballDiameter = 20
        self.tile1x = ((self.canvas_width/2)/2- self.ballDiameter/2)
        self.tile1y = ((self.canvas_height/2)/2 - self.ballDiameter/2)

        self.canvas.create_oval(self.tile1x, self.tile1y,
                                self.tile1x + self.ballDiameter,
                                self.tile1y + self.ballDiameter,
                                fill = "#ffffff", tags = "tile_1")

def main():
    board = CounterBoard()
    game = LogicGame(board)
    game.mainloop()
    

main()
        
    
