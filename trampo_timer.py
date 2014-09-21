from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TimerContainer(BoxLayout):
    pass


class TimerApp(App):
    def build(self):
        return TimerContainer()


if __name__ == '__main__':
    TimerApp().run()
