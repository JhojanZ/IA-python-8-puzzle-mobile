from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Welcome to the 8-Puzzle Solver'))
        
        start_button = Button(text='Start Solving')
        start_button.bind(on_press=self.go_to_algorithm_selection)
        layout.add_widget(start_button)
        
        self.add_widget(layout)

    def go_to_algorithm_selection(self, instance):
        self.manager.current = 'algorithm_selection'

class AlgorithmSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(AlgorithmSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Select an Algorithm'))
        
        dropdown = DropDown()
        algorithms = ['BFS', 'DFS', 'UCS', 'Greedy', 'A*']
        for algo in algorithms:
            btn = Button(text=algo, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        main_button = Button(text='Choose Algorithm')
        main_button.bind(on_release=dropdown.open)
        layout.add_widget(main_button)

        dropdown.bind(on_select=self.set_algorithm)
        self.add_widget(layout)

    def set_algorithm(self, instance, value):
        print(f'Selected algorithm: {value}')
        # Here you would typically transition to the puzzle visualization screen
        # self.manager.current = 'puzzle_visualization'

class PuzzleVisualizationScreen(Screen):
    def __init__(self, **kwargs):
        super(PuzzleVisualizationScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Puzzle Visualization'))
        # Add puzzle visualization logic here
        self.add_widget(layout)

class ScreenManagement(ScreenManager):
    pass