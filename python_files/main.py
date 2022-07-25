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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class GameBoard(Screen):
    # create_board() might only need this for backend logic purposes. or just make an array.
    # move()
    pass

class GameWindow(Screen):
    # game_board = ObjectProperty(None)
    pass

class MainWindow(Screen):
    pass

class WindowManger(ScreenManager):
    pass
#=====================================================================

kv = Builder.load_file("SixteenCounter.kv")
# kv = Builder.load_file("new_window.kv")

class SixteenCounterApp(App):
    # seems like this part will act as my 'main()'
    def build(self):
        return kv

SixteenCounterApp().run()