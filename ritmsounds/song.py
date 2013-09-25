#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame as pg
from pygame.mixer import music
class Song(object):
    """Clase que representa a una canción del juego, tanto para reproducirla, como para interpretar / manejar sus pasos."""

    def __init__(self, name, steps = None):
        music.load(name)
        self.__name = name

        self.__steps = list()
        self.__currentStep = None
        self.play = music.play
        self.pause = music.pause()
        self.unpause = music.unpause
        self.stop = music.stop


        if (steps is None == False):
            self.__steps = steps
            self.__currentStep=0



    def addStep(self, step):
        self.__steps.append(step)

    def getStep(self):
        if (self.__currentStep is None):
            return -1

        auxiliar = self.__currentStep
        self.__currentStep += 1
        if (self.__currentStep >= len(self.__steps)):
            self.__currentStep = auxiliar

        return self.__steps[auxiliar]


    def loadSteps(self, steps):
        """método que sirve para cargar unos pasos a la canción actual"""
        self.__steps = steps


    def str(self):
        return self.__name
