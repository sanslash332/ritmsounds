#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import eventos
import escritor
import song

nextTickEvent = eventos.Event()
hitEvent = eventos.Event()
endSongEvent = eventos.Event()
startEvent = eventos.Event()

class Juego(object):
    """clase que maneja al juego en general."""
    def __init__(self, cancion, modo):
        object.__init__(self)
        self.__ticks=0
        nextTickEvent+=self.__nextTick
        hitEvent+=self.__hitStep

        if (modo == 0):
            self.__song = song.Song(cancion)
            self.__playMode = 0

    def start(self):
        startEvent()
        self.__song.play()

    def __hitStep(self,hit):
        if (self.__playMode==0):
            self.__song.addStep((__ticks,hit))

    def __nextTick(self):
        self.__ticks+=1
        if(self.__song.isPlay() == False):
            if(self.__playMode == 0):
                escritor.escribirSteps(self.__song.str(), self.__song.getAllSteps())
            endSongEvent()






