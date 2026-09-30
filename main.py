import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=30, spacing=20, **kwargs)

        # Counter variable
        self.count = 0

        # Title Label
        self.title_label = Label(
            text="Hello, Android!",
            font_size="28sp",
            bold=True,
            color=(0.2, 0.6, 1, 1),
        )

        # Status / Counter Label
        self.counter_label = Label(
            text="Button clicks: 0",
            font_size="20sp",
            color=(1, 1, 1, 1),
        )

        # Interactive Button
        self.action_btn = Button(
            text="Click Me!",
            font_size="18sp",
            size_hint=(1, 0.3),
            background_color=(0.2, 0.7, 0.3, 1),
        )
        self.action_btn.bind(on_release=self.on_button_click)

        # System Info Label
        python_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.info_label = Label(
            text=f"Running Python {python_ver}",
            font_size="14sp",
            color=(0.6, 0.6, 0.6, 1),
        )

        # Add all widgets to layout
        self.add_widget(self.title_label)
        self.add_widget(self.counter_label)
        self.add_widget(self.action_btn)
        self.add_widget(self.info_label)

    def on_button_click(self, instance):
        self.count += 1
        self.counter_label.text = f"Button clicks: {self.count}"


class MyApp(App):
    def build(self):
        # Optional: Set dark background color for desktop testing
        Window.clearcolor = (0.12, 0.12, 0.12, 1)
        self.title = "My Mobile App"
        return MainScreen()


if __name__ == "__main__":
    MyApp().run()
