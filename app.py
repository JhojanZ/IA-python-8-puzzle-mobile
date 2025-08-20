from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from run import select_algorithm, Algorithm

class Puzzle8UI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.result_label = Label(text="Seleccione un algoritmo")
        self.add_widget(self.result_label)

        # Horizontal box for select and play button
        select_box = BoxLayout(orientation='horizontal', size_hint=(1, None), height=44, spacing=10)
        self.spinner = Spinner(
            text="Elige algoritmo",
            values=[algo.name for algo in Algorithm],
            size_hint=(0.7, 1)
        )
        select_box.add_widget(self.spinner)

        self.play_button = Button(text="Play", size_hint=(0.3, 1))
        self.play_button.bind(on_press=self.run_algo)
        select_box.add_widget(self.play_button)

        self.add_widget(select_box)

    def run_algo(self, instance):
        selected = self.spinner.text
        if selected == "Elige algoritmo":
            self.result_label.text = "Por favor, selecciona un algoritmo."
            return
        algo = Algorithm[selected]
        rows = select_algorithm(algo)
        if rows:
            text = "\n".join([f"{r[0]} | expandidos={r[1]} | profundidad={r[2]} | tiempo={r[3]:.3f}s" for r in rows])
        else:
            text = "No solucionable o sin resultados."
        self.result_label.text = text

class Puzzle8App(App):
    def build(self):
        return Puzzle8UI()

if __name__ == '__main__':
    Puzzle8App().run()