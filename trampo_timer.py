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
        self.nb_passages = NB_PERS_PAR_TRAMPO_DEFAUT
        self.nb_trampolines = NB_TRAMPOS_DEFAUT
        self.total_passages = NB_PERS_PAR_TRAMPO_DEFAUT
        self.saisie_nb_passages(4)
        BoxLayout.__init__(self)
    
    def update_input_values(self):
        self.ti_nb_passages.text = str(self.nb_passages)
        self.ti_total_passages.text = str(self.total_passages)
        self.ti_nb_trampolines.text = str(self.nb_trampolines)

        
    def duree_formatee(self, duree_secondes):
        minutes = int(duree_secondes) / 60
        secondes =  int(duree_secondes) % 60
        return "{}' {}''".format(minutes, secondes)
    
    def tick(self, dt):
        restant = self.objectif-time()
        self.decompte.text = self.duree_formatee(restant)
        if restant <= 0:
            cb = self.timeout_cb
            #self.timeout_cb = None
            cb()

    def passage_termine(self):
        print "passage_termine"
        if self.nb_passages > 0:
            self.nb_passages = self.nb_passages - 1            
        else :
            self.nb_trampolines = self.nb_trampolines - 1
            if self.nb_trampolines > 0:
                self.nb_passages = self.total_passages - 1
                self.timeout(DUREE_PASSAGE, self.passage_termine)
            else:
                pass            
        self.update_input_values()
            

    def saisie_nb_passages(self, nb_passages_saisies):
        self.nb_passages = int(nb_passages_saisies)
        print self.nb_passages
        self.timeout(DUREE_PASSAGE, self.passage_termine)

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
