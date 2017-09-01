#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from time import time, localtime

DUREE_PASSAGE = 15
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
        self.nb_rotations = NB_TRAMPOS_DEFAUT
        self.maj_champs_saisie()
    
    def maj_champs_saisie(self):
        self.ti_nb_passages.text = str(self.nb_passages)
        self.ti_total_passages.text = str(self.total_passages)
        self.ti_nb_trampolines.text = str(self.nb_trampolines)
        self.ti_nb_rotations.text = str(self.nb_rotations)

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

    # Réactions au timer
    def passage_termine(self):
        print "passage_termine"
        if self.nb_passages > 0:
            # "Suivant !"
            # self.timeout(INTER_PASSAGE, self.prochain_passage)
            self.prochain_passage();
        else :
            # "On tourne !"
            self.timeout(INTER_TRAMPO, self.prochain_passage)

    def prochain_passage(self):
        print "prochain_passage"
        if self.nb_passages > 0:
            self.nb_passages = self.nb_passages - 1            
        else :
            if self.nb_trampolines > 0:
                self.nb_trampolines = self.nb_trampolines - 1
                self.nb_passages = self.total_passages - 1
                self.timeout(DUREE_PASSAGE, self.passage_termine)
            else:
                self.prochaine_rotation()
                return        
        self.maj_champs_saisie()
        self.timeout(DUREE_PASSAGE, self.passage_termine)

    def d_ici_la_fin_de_seance(self):
        loc_time = localtime()
        cur_h = loc_time[3]
        cur_m = loc_time[4]
        nb_min = 21 * 60 + 30 - (cur_h * 60 + cur_m)
        print "nb_min", nb_min
        return nb_min

    def prochaine_rotation(self):
        print "prochaine_rotation"
        if self.nb_rotations > 0:
            temps_rotation = self.d_ici_la_fin_de_seance() / self.nb_rotations
            self.nb_rotations = self.nb_rotations - 1
            self.timeout(temps_rotation, self.prochaine_rotation)

    # Réaction aux boutons
    def saisie_nb_passages(self, nb_passages_saisies):
        self.nb_passages = int(nb_passages_saisies)
        self.prochain_passage()
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
            self.prochain_passage()
        if self.pause:
            self.bt_play_pause.text = "Pause"
            self.tick(1.0)
            self.clock_event = Clock.schedule_interval(self.tick, 1.0)
            self.pause = False
        else:
            self.bt_play_pause.text = "Go !"
            Clock.unschedule(self.tick)
            self.pause = True
            

class TimerApp(App):
    def build(self):
        container = TimerContainer()
        return container


if __name__ == '__main__':
    TimerApp().run()
