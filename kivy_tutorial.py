from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


# class BoxLayoutExample(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "vertical"
#         b1 = Button(text="Button1", size_hint=(.8, .5))
#         b2 = Button(text="Button2")
#         self.add_widget(b1)     # Order of the add widgets tells the order of the elements
#         self.add_widget(b2)
#
#
# class OnyekaApp(App):
#     pass
#
#
# OnyekaApp().run()
from kivy.uix.textinput import TextInput


class GridLayoutExample(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.size_hint = (1, 0.3)

        self.l1 = Label(text="Student Name", size_hint=(.1, .2))
        self.student_name = TextInput(size_hint=(.1, .2))

        self.l2 = Label(text="Student Age", size_hint=(.1, .2))
        self.student_age = TextInput(size_hint=(.1, .2))

        self.l3 = Label(text="Student Marks", size_hint=(.1, .2))
        self.student_gender = TextInput(size_hint=(.1, .2))

        self.press = Button(text="Enter", size_hint=(.1, .2))
        self.press.bind(on_press=self.okay)
        self.press = Button(text="Next", size_hint=(.1, .2))
        self.press.bind(on_press=self.Next)

        self.add_widget(self.l1)
        self.add_widget(self.student_name)
        self.add_widget(self.l2)
        self.add_widget(self.student_age)
        self.add_widget(self.l3)
        self.add_widget(self.student_gender)
        self.add_widget(self.press)

    def okay(self, instance):
        print(f"Student name: {self.student_name.text}")
        print(f"Student name: {self.student_age.text}")
        print(f"Student name: {self.student_gender.text}")
        print("")

    def next(self, instance):

from kivy.uix.popup import Popup

from kivy.uix.textinput import TextInput


class GridLayoutExample(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.l1 = Label(text="Student Name", size_hint=(.1, .2))
        self.s_name = TextInput(size_hint=(.1, .2))
        self.add_widget(self.l1)
        self.add_widget(self.s_name)

        self.press = Button(text="Enter", size_hint=(.1, .2))
        self.press.bind(on_press=self.onButtonPress)
        self.add_widget(self.press)

    def onButtonPress(self, button):
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(text=f"Student name: {self.s_name.text}\nName saved")
        closeButton = Button(text="Okay")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        popup = Popup(title='Demo Popup',
                      content=layout)
        popup.size_hint = (0.4, 0.4)
        popup.open()

        closeButton.bind(on_press=popup.dismiss)


class DemoApp(App):
    def build(self):
        return GridLayoutExample()


if __name__ == "__main__":
    DemoApp().run()
