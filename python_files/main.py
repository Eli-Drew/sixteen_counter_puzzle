"""
=======================================================
Author:   Drew Rinker
Date:     07/20/2022

Main gui app portion of sixteen counter
*do more description here later.
=======================================================
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class GameBoard(GridLayout):
    # create_board() might only need this for backend logic purposes. or just make an array.
    # move()
    pass

class GameWindow(GridLayout):
    # game_board = ObjectProperty(None)
    pass

class SixteenCounterApp(App):
    # seems like this part will act as my 'main()'
    pass

SixteenCounterApp().run()