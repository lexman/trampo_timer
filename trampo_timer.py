from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty

class TimerContainer(BoxLayout):
    count_down = 100
    def tick(self, dt):
        self.decompte.text = str(self.count_down)
        self.count_down = self.count_down - 1

    #def saisie_nb_passages(

class TimerApp(App):
    def build(self):
        container = TimerContainer()
        Clock.schedule_interval(container.tick, 1.0)
        return container


if __name__ == '__main__':
    TimerApp().run()
