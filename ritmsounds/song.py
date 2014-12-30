#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame as pg
from pygame.mixer import music
import escritor
class Song(object):
    """Clase que representa a una canción del juego, tanto para reproducirla, como para interpretar / manejar sus pasos."""

    def __init__(self, name, steps = None):

        music.load(name)
        self.__name = name

        self.__steps = list()
        self.__currentStep = 0
        self.play = music.play
        self.pause = music.pause()
        self.unpause = music.unpause
        self.stop = music.stop
        self.isPlay= music.get_busy
        self.setVolume = music.set_volume


        if (steps is None == False):
            self.__steps = steps
            self.__currentStep=0



    def addStep(self, step):
        self.__steps.append(step)

    def getStep(self,tick):
        retorner = None 
        #escritor.escribirLog("buscando step en tick " + str(tick))

        for x in range(self.__currentStep,len(self.__steps)):
            if self.__steps[x][0] == tick:
                #escritor.escribirLog("tick encontrado")

                retorner = self.__steps[x]
                self.__currentStep=x

        #escritor.escribirLog("se retornará " + str(retorner))
        return retorner



    def loadSteps(self, steps):
        """método que sirve para cargar unos pasos a la canción actual"""
        self.__steps = steps


    def str(self):
        return self.__name

    def getAllSteps(self):
        return self.__steps
    def clearSteps(self):
        del self.__steps