from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class AnchorLayoutExample(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = GridLayout(cols=1)
        self.grid.bind(size=self._update_rect, pos=self._update_rect)
        self.grid.size_hint = (0.7, 0.7)
        self.grid.spacing = "20dp"
        self.grid.padding = "30dp"

        self.lower_grid = GridLayout(rows=1)
        self.lower_grid.spacing = "5dp"
        self.grid.padding = "20dp"

        self.logo = Image(source="images/logo3.png")
        self.login = Label(text="USER LOGIN", color=(0.6, 0, 0.6, 1), font_size=26, bold=True, size_hint=(1, None),
                           height="50dp")

        self.inner_grid = GridLayout(rows=2, cols=2)
        self.inner_grid.spacing = "5dp"

        self.verify = Label(text="", color=(0.6, 0, 0.6, 1), size_hint=(1, 0.2))
        self.name_label = Label(text="Username:", color=(0.6, 0, 0.6, 1), font_size=18, size_hint=(0.3, 0.3))
        self.name_field = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.3))
        self.password_label = Label(text="Password:", color=(0.6, 0, 0.6, 1), font_size=18, size_hint=(0.3, 0.3))
        self.password_field = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.3))

        self.submit = Button(text="LOGIN", background_color="#5f2483", bold=True, background_normal="",
                             size_hint=(1, None), height="40dp")
        self.submit.bind(on_press=self.on_submit)
        self.clear = Button(text="CLEAR", background_color="#5f2483", bold=True, background_normal="",
                            size_hint=(1, None), height="40dp")
        self.clear.bind(on_press=self.on_clear)

        with self.grid.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(size=self.grid.size, pos=self.grid.pos,
                                         radius=[(40, 40), (40, 40), (20, 20), (20, 20)])

        self.inner_grid.add_widget(self.name_label)
        self.inner_grid.add_widget(self.name_field)
        self.inner_grid.add_widget(self.password_label)
        self.inner_grid.add_widget(self.password_field)

        self.lower_grid.add_widget(self.submit)
        self.lower_grid.add_widget(self.clear)

        self.grid.add_widget(self.logo)
        self.grid.add_widget(self.login)
        self.grid.add_widget(self.verify)
        self.grid.add_widget(self.inner_grid)
        self.grid.add_widget(self.lower_grid)
        self.add_widget(self.grid)

    def on_submit(self, instance):
        if self.name_field.text == "Onyeka" and self.password_field.text == "chicken":
            self.verify.text = "Access Granted"
            self.verify.color = (0, 1, 0, 1)

        elif self.name_field.text == "" or self.password_field.text == "":
            self.verify.text = "Required: Fill both fields"
            self.verify.color = (1, 0, 0, 1)

        else:
            self.verify.text = "Incorrect Username or Password"
            self.verify.color = (1, 0, 0, 1)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_clear(self, instance):
        self.verify.text = ""
        self.name_field.text = ""
        self.password_field.text = ""


class DemoApp(App):
    def build(self):
        self.root = root = AnchorLayoutExample()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0.6, 0, 0.6, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == "__main__":
    DemoApp().run()
