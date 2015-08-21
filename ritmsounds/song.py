#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame as pg
from pygame.mixer import music
import escritor
import steplist
import jsonpickle

class Song(object):
    """Clase que representa a una canci�n del juego, tanto para reproducirla, como para interpretar / manejar sus pasos."""

    def __init__(self, name, songpath, steps = None):


        self.name = name
        self.songpath = songpath

        self.__steps = list()
        self.__currentSteplist = steplist.steplist()
        self.__currentStep=0

        if (steps is None == 	False):
            self.__steps = steps

    def selectSteplist(self, index):
        self.__currentSteplist = self.__steps[index]




    def addStep(self, step):
        self.__currentSteplist.steps.append(step)

    def setHands(self, hands):
        self.__currentSteplist.hands = hands

    def getHands(self):
        return(self.__currentSteplist.hands)


    def setPressSpeed(self, speed):
            self.__currentSteplist.pressSpeed = speed

    def getPressSpeed(self):
        return(self.__currentSteplist.pressSpeed)


    def setSteplistname(self, name):
        self.__currentSteplist.name=name

    def getSteplistname(self):
        return(self.__currentSteplist.name)

    def getStartHp(self):
        return(self.__currentSteplist.startHp)

    def getStep(self,tick):
        retorner = None 
        #escritor.escribirLog("buscando step en tick " + str(tick))

        for x in range(self.__currentStep,len(self.__currentSteplist.steps)):
            if self.__currentSteplist.steps[x][0] == tick:
                #escritor.escribirLog("tick encontrado")

                retorner = self.__currentSteplist.steps[x]
                self.__currentStep=x

        #escritor.escribirLog("se retornar� " + str(retorner))
        return retorner



    def loadSteps(self, steps):
        """m�todo que sirve para cargar unos pasos a la dificultad actual de la canci�n actual"""
        self.__currentSteplist.steps= steps


    def saveSteplist(self):
        self.__steps.append(self.__currentSteplist)

    def str(self):
        return self.__name

    def getAllStepslist(self):
        return self.__steps
    def getAllSteps(self):
        return(self.__currentSteplist.steps)



    def clearSteps(self):
        del self.__steps

    def genJson(self):
        self.__currentStep=0
        self.__currentSteplist= steplist.steplist()
        r = jsonpickle.encode(self)
        self.__currentStep=0
        self.__currentSteplist=steplist.steplist()
        return(r)

