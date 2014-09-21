from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from time import time

DUREE_PASSAGE = 10
INTER_PASSAGE = 5
INTER_TRAMPO = 10

NB_TRAMPOS_DEFAUT = 4
NB_PERS_PAR_TRAMPO_DEFAUT = 4

class TimerContainer(BoxLayout):


    def __init__(self):
        BoxLayout.__init__(self)
        self.pause = True
        self.clock_event = None
        self.nb_passages = 0
        self.nb_trampolines = NB_TRAMPOS_DEFAUT
        self.total_passages = NB_PERS_PAR_TRAMPO_DEFAUT
        self.update_input_values()

        #self.saisie_nb_passages(4)
    
    def update_input_values(self):
        self.ti_nb_passages.text = str(self.nb_passages)
        self.ti_total_passages.text = str(self.total_passages)
        self.ti_nb_trampolines.text = str(self.nb_trampolines)

        
    def duree_formatee(self, duree_secondes):
        minutes = int(duree_secondes) / 60
        secondes =  int(duree_secondes) % 60
        return "{}' {}''".format(minutes, secondes)
    
    def tick(self, dt):
        self.restant = self.restant - 1
        self.decompte.text = self.duree_formatee(self.restant)
        if self.restant <= 0:
            cb = self.timeout_cb
            self.timeout_cb = None
            cb()

    def passage_termine(self):
        print "passage_termine"
        if self.nb_passages > 0:
            self.nb_passages = self.nb_passages - 1            
        else :
            if self.nb_trampolines > 0:
                self.nb_trampolines = self.nb_trampolines - 1
                self.nb_passages = self.total_passages - 1
                self.timeout(DUREE_PASSAGE, self.passage_termine)
            else:
                pass            
        self.update_input_values()
        self.timeout(DUREE_PASSAGE, self.passage_termine)
            

    def saisie_nb_passages(self, nb_passages_saisies):
        self.nb_passages = int(nb_passages_saisies)
        self.passage_termine()
        self.timeout(DUREE_PASSAGE, self.passage_termine)

    def saisie_total_passages(self):
        total_passages = int(self.total_passages.text)
        print total_passages

    def saisie_nb_trampolines(self):
        nb_trampolines = int(self.nb_trampolines.text)
        print nb_trampolines
        
    def timeout(self, duree, callback):
        self.restant = duree
        self.timeout_cb = callback
        
    def play_pause(self):
        if self.clock_event == None:
            # Tout premier appui sur le bouton pour lancer le chrono
            self.passage_termine()
        if self.pause:
            self.bt_play_pause.text = "Pause"
            self.tick(1.0)
            self.clock_event = Clock.schedule_interval(self.tick, 1.0)
            self.pause = False
        else:
            self.bt_play_pause.text = "Go !"
            print(self.clock_event)
            print(dir(self.clock_event))
            Clock.unschedule(self.tick)
            self.pause = True
            

class TimerApp(App):
    def build(self):
        container = TimerContainer()
        return container


if __name__ == '__main__':
    TimerApp().run()
