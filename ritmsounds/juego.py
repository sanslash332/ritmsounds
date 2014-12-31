#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import eventos
import escritor
import song
import jugador

nextTickEvent = eventos.Event()
hitEvent = eventos.Event()
endSongEvent = eventos.Event()
startEvent = eventos.Event()
stepEvent = eventos.Event()
resultsEvent = eventos.Event()

class Juego(object):
    """clase que maneja al juego en general."""

    def start(self):
        startEvent()
        self.__song.play()

    def hitStep(self,hit):
        if (self.__playMode==0):
            self.__song.addStep((self.__ticks,hit))
        elif self.__playMode==1:
            if self.__pointMode== 0:

                if len(self.__stepStack) > 0:
                    if self.__stepStack[0][1] == hit:
                        self.player.sumarPuntos(1)
                        self.__song.setVolume(1)
                        self.__stepStack.pop(0)

                    else:
                        self.player.sumarMiss(1)
                    
                        self.__song.setVolume(0.3)
                else:
                    self.player.sumarMiss(1)
                    self.__song.setVolume(0.3)
            else:
                point = False
                for x in range(0,len(self.__stepPoints)):
                    if self.__stepPoints[x][0]-10 <= self.__ticks and self.__stepPoints[x][0]+30 > self.__ticks and self.__stepPoints[x][1] == hit and self.__stepPoints[x][2] == False:
                        self.__stepPoints[x] = (self.__stepPoints[x][0], self.__stepPoints[x][1], True)
                        self.player.sumarPuntos(1)
                        point=True
                        self.__song.setVolume(1)
                        if len(self.__stepStack) > 0  and self.__stepStack[0][0] == self.__stepPoints[x][0] and self.__stepStack[0][1] == self.__stepPoints[x][1]:
                            self.__stepStack.pop(0)

                if point == False:
                    self.__song.setVolume(0.3)
                    self.player.sumarMiss(1)


                        











    def __nextTick(self):
        self.__ticks+=1
        #escritor.flog("transcurrido tik " + str(self.__ticks))
        

        if self.__playMode==1:
            step = self.__song.getStep(self.__ticks)
            #escritor.escribirLog("lo encontrado es " + str(step))
            self.__checkStepTime()
            if (step is None) == False:
                enter = True
                if self.__playMode == 1:
                    for x in self.__stepPoints:
                        if x[0] == step[0] and x[1] == step[1] and x[2] == True:
                            enter = False




                if enter:

                    self.__stepStack.append(step)
                #escritor.flog("añadido paso al stack" + str(step[1]) + " en el tiempo " + str(self.__ticks))
                hitEvent(step[1])
            


        if(self.__song.isPlay() == False):
            if(self.__playMode == 0):
                escritor.escribirSteps(self.__song.str(), self.__song.getAllSteps())
            elif self.__playMode==1:
                self.player.sumarMiss(len(self.__stepStack))
            endSongEvent()
            

    def __checkStepTime(self):
        """se remueven los steps que hayan estado por más de 30 ticks en el stack"""
        
        for x in range(0,len(self.__stepStack)):
            if self.__ticks - self.__stepStack[x][0] >= 30:
                self.__stepStack.pop(x)
                #hitEvent(3)
                self.player.sumarMiss(1)
                self.__checkStepTime()
                self.__song.setVolume(0.3)
                break
        

            


    def stop(self):
        self.__song.stop()
        
        global stepEvent
        global startEvent
        global nextTickEvent
        global hitEvent
        nextTickEvent-=self.__nextTick
        if self.__playMode == 0:
            hitEvent-=self.hitStep
        elif self.__playMode  == 1:
            stepEvent-=self.hitStep


        

    def __init__(self, cancion, modo, tipo= 0 ):
        object.__init__(self)
        self.__ticks=0
        global hitEvent
        global nextTickEvent
        global stepEvent


        nextTickEvent+=self.__nextTick
        self.player=jugador.Jugador()
        if (modo == 0):
            self.__song = song.Song(cancion)
            self.__playMode = 0
            hitEvent+=self.hitStep
            self.__song.setVolume(1)
        elif modo == 1:
            self.__playMode=1
            stepEvent+=self.hitStep
            self.__stepStack=list()
            self.__song=song.Song(cancion)
            self.__song.loadSteps(escritor.cargarSteps(cancion))
            self.__song.setVolume(1)
            self.__pointMode=0
            if tipo == 1:
                self.__pointMode=1

                self.__stepPoints = list()
                for step in self.__song.getAllSteps():
                    self.__stepPoints.append((step[0], step[1],False))












