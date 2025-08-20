from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from ui.screens import MainMenuScreen, AlgorithmSelectionScreen, PuzzleVisualizationScreen

class Puzzle8App(App):
    def build(self):
        self.title = "8-Puzzle Solver"
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(AlgorithmSelectionScreen(name='algorithm_selection'))
        sm.add_widget(PuzzleVisualizationScreen(name='puzzle_visualization'))
        return sm

if __name__ == '__main__':
    Puzzle8App().run()