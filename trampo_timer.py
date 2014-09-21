from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from time import time

DUREE_PASSAGE = 60
INTER_PASSAGE = 5
INTER_TRAMPO = 10

class TimerContainer(BoxLayout):


    def __init__(self):
        def nope():
            pass
        self.timeout(DUREE_PASSAGE, nope)
        BoxLayout.__init__(self)
    
        
    def duree_formatee(self, duree_secondes):
        minutes = int(duree_secondes) / 60
        secondes =  int(duree_secondes) % 60
        return "{}' {}''".format(minutes, secondes)
    
    def tick(self, dt):
        restant = self.objectif-time()
        self.decompte.text = self.duree_formatee(restant)
        if restant <= 0:
            self.timeout_cb()

    def passage_termine(self):
        pass

    def saisie_nb_passages(self):
        nb_passages = int(self.nb_passages.text)
        print nb_passages
        self.timeout(DUREE_PASSAGE, nope)

    def saisie_total_passages(self):
        total_passages = int(self.total_passages.text)
        print total_passages

    def saisie_nb_trampolines(self):
        nb_trampolines = int(self.nb_trampolines.text)
        print nb_trampolines
        
    def timeout(self, duree, callback):
        self.objectif = time() + duree
        self.timeout_cb = callback

class TimerApp(App):
    def build(self):
        container = TimerContainer()
        Clock.schedule_interval(container.tick, 1.0)
        return container


if __name__ == '__main__':
    TimerApp().run()
