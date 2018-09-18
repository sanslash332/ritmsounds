#!/usr/bin/python

import pygame as pg
from pygame.mixer import music
import escritor
import steplist
import jsonpickle

class Song(object):
    """Clase que representa a una canción del juego, tanto para reproducirla, como para interpretar / manejar sus pasos."""

    def __init__(self, name, songpath, steps = None):


        self.name = name
        self.songpath = songpath

        self.__steps = list()
        self.__currentSteplist = steplist.steplist()
        self.__currentStep=0

        if (steps is None == 	False):
            self.__steps = steps

    def restartSong(self):
        self.__currentStep=0

    def selectSteplist(self, index):
        self.__currentSteplist = self.__steps[index]

    def resetSteplist(self):
        self.__currentSteplist=steplist.steplist()

    def resetSteps(self):
        self.__currentSteplist.steps=[]

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

    def setAntisipateTime(self,anttime):
        self.__currentSteplist.antisipateTime=anttime

    def getAntisipateTime(self):
        return(self.__currentSteplist.antisipateTime)

    def setRestoreHp(self,hp):
        self.__currentSteplist.restoreHp=hp

    def getRestoreHp(self):
        return(self.__currentSteplist.restoreHp)

    def setSteplistname(self, name):
        self.__currentSteplist.name=name

    def getSteplistname(self):
        return(self.__currentSteplist.name)

    def setStartHp(self, hp):
        self.__currentSteplist.startHp=hp

    def getStartHp(self):
        return(self.__currentSteplist.startHp)

    def getStep(self,tick):
        retorner = []
        #escritor.escribirLog("buscando step en tick " + str(tick))

        for x in range(self.__currentStep,len(self.__currentSteplist.steps)):
            if self.__currentSteplist.steps[x][0] == tick:
                #escritor.escribirLog("tick encontrado")

                retorner.append(self.__currentSteplist.steps[x])
                self.__currentStep=x

        #escritor.escribirLog("se retornar� " + str(retorner))
        return retorner



    def loadSteps(self, steps):
        """método que sirve para cargar unos pasos a la dificultad actual de la canción actual"""
        self.__currentSteplist.steps= steps


    def saveSteplist(self):
        self.__steps.append(self.__currentSteplist)

    def deleteSteplist(self, index):
        if index < len(self.__steps):
            self.__steps.pop(index)


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

