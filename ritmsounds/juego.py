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
deatEvent = eventos.Event()

import soundevents

class Juego(object):
    """clase que maneja al juego en general."""

    def start(self):
        startEvent()
        soundevents.musicPlay()


    def checkLife(self):
        if self.consecutivePoints==10:
            self.player.setHP(self.player.getHP()+1)
            self.consecutivePoints=0


        if self.player.getHP() == 0:
            deatEvent()
            endSongEvent()
        elif self.player.getHP() >= self.__song.getStartHp():
            self.player.setHP(getStartHp())




    def hitStep(self,hit):
        if (self.__playMode==0):
            self.__song.addStep((self.__ticks,hit))
        elif self.__playMode==1:
            

            if len(self.__stepStack) > 0:
                if self.__stepStack[0][1] == hit:
                    self.player.sumarPuntos(1)
                    soundevents.musicSetVolume(1)

                    self.__stepStack.pop(0)
                    self.consecutivePoints+=1
                    self.checkLife()





                else:
                    self.player.sumarMiss(1)
                    self.player.setHP(self.player.getHP()-1)
                    self.consecutivePoints=0
                    self.checkLife()
                    
                    soundevents.musicSetVolume(0.3)

            else:
                self.__prestep.append((self.__ticks,hit))


    def __nextTick(self):
        self.__ticks+=1
        #escritor.flog("transcurrido tik " + str(self.__ticks))
        

        if self.__playMode==1:
            step = self.__song.getStep(self.__ticks)
            #escritor.escribirLog("lo encontrado es " + str(step))
            self.__checkStepTime()
            

            if (step is None) == False:

                self.__stepStack.append(step)
                #escritor.flog("a�adido paso al stack" + str(step[1]) + " en el tiempo " + str(self.__ticks))
                hitEvent(step[1])
            


        if(soundevents.musicIsPlay() == False):
            if(self.__playMode == 0):
                self.__song.saveSteplist()

                escritor.saveSong(self.__song)
            elif self.__playMode==1:
                self.player.sumarMiss(len(self.__stepStack))
            endSongEvent()
            

    def __checkStepTime(self):
        """se remueven los steps que hayan estado por m�s del pressspeed  ticks en el stack"""
        
        for x in range(0, len(self.__prestep)):
            if self.__ticks - self.__prestep[x][0] >= 20:
                self.__prestep.pop(x)
                self.player.sumarMiss(1)
                soundevents.musicSetvolume(0.3)
                self.consecutivePoints=0
                self.player.setHP(self.player.getHP()-1)
                self.checkLife()
                self.__checkStepTime()
                return()
            else:
                if len(self.__stepStack) >0:
                    step = self.__stepStack[0]
                    if step[1] == self.__prestep[x][1]:
                        self.__stepStack.pop(0)
                        self.__prestep.pop(x)
                        soundevents.musicSetVolume(1)

                        self.player.sumarPuntos(1)
                        self.consecutivePoints+=1
                        self.checkLife()

                    else:
                        self.__prestep.pop(x)
                        self.player.setHP(self.player.getHP() -1)
                        soundevents.musicSetVolume(0.3)
                        self.consecutivePoints=0
                        self.checkLife()

                        self.__checkStepTime()
                        return()

        for x in range(0,len(self.__stepStack)):
            #escritor.flog("los valores a comparar son: pressSpeed: " + str(self.__pressSpeed))
            #escritor.flog(" lost ticks: " + str(self.__ticks))
            #escritor.flog(" tick actual:  " + str(self.__stepStack))

            if (self.__ticks - self.__stepStack[x][0]) >= self.__pressSpeed:
                self.__stepStack.pop(x)
                #hitEvent(3)
                self.player.sumarMiss(1)
                self.consecutivePoints=0
                self.player.setHP(self.player.getHP()-1)
                self.checkLife()
                self.__checkStepTime()
                
                soundevents.musicSetVolume(0.3)
                break
        

            


    def stop(self):
        soundevents.musicStop()
        
        global stepEvent
        global startEvent
        global nextTickEvent
        global hitEvent
        global endSongEvent
        endSongEvent()

        nextTickEvent-=self.__nextTick
        if self.__playMode == 0:
            hitEvent-=self.hitStep
        elif self.__playMode  == 1:
            stepEvent-=self.hitStep


        

    def __init__(self, cancion, modo, tipo= 0, jpugador = jugador.Jugador()):
        object.__init__(self)
        self.__ticks=0
        global hitEvent
        global nextTickEvent
        global stepEvent
        global deatEvent

        nextTickEvent+=self.__nextTick

        self.__song = cancion
        
        self.player=jpugador
        self.player.resetPoints()

        self.player.setHP(self.__song.getStartHp())
        soundevents.musicSetVolume(1)
        soundevents.musicLoad(self.__song.songpath)
        self.__pressSpeed = self.__song.getPressSpeed()
        #print(" este es el presspeed" + str(self.__pressSpeed))



        if (modo == 0):
            
            self.__playMode = 0
            hitEvent+=self.hitStep
            
        elif modo == 1:
            self.__playMode=1
            stepEvent+=self.hitStep
            self.__stepStack=list()
            self.consecutivePoints = 0

            
            self.__pointMode=tipo
            self.__prestep = []
        



