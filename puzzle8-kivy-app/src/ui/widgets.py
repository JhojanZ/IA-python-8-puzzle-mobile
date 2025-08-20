from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CustomButton(Button):
    def __init__(self, text, **kwargs):
        super().__init__(text=text, **kwargs)
        self.size_hint = (None, None)
        self.size = (200, 50)

class CustomLabel(Label):
    def __init__(self, text, **kwargs):
        super().__init__(text=text, **kwargs)
        self.font_size = 24

class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 50)
        self.multiline = False

class InputField(BoxLayout):
    def __init__(self, label_text, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.label = CustomLabel(text=label_text)
        self.text_input = CustomTextInput()
        self.add_widget(self.label)
        self.add_widget(self.text_input)