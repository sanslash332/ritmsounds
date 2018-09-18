#!/usr/bin/python

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


    def checkLife(self,hurt=False):
        if hurt:
            self.player.setHP(self.player.getHP()-1)
            #soundevents.playDamage()
            self.consecutivePoints=0
            HPpersent = int((self.player.getHP()*100)/self._maxHP)
            if HPpersent==50:
                soundevents.playLowHp()


        if self.consecutivePoints==self.__song.getRestoreHp():
            if self.player.getHP() < self.__song.getStartHp() and self.restoreHPInPlay==True:
                self.player.setHP(self.player.getHP()+1)
                soundevents.playRestoreHP()
            self.consecutivePoints=0
            


        if self.player.getHP() == 0 and self.__pointMode==0:
            deatEvent()
            endSongEvent()
        



    def hitStep(self,hit):
        if (self.__playMode==0):
            self.__song.addStep((self.__ticks,hit))
        elif self.__playMode==1:
            

            if len(self.__stepStack) > 0:
                if self.__stepStack[0][1] == hit:
                    self.player.sumarPuntos(1)
                    soundevents.unapplyVolumeMusicFactor(0.2)

                    self.__stepStack.pop(0)
                    self.consecutivePoints+=1
                    self.checkLife()

                else:
                    self.player.sumarMiss(1)
                    self.checkLife(True)
                    self.__stepStack.pop(0)
                    soundevents.applyVolumeMusicFactor(0.2)

            else:
                self.__prestep.append((self.__ticks,hit))


    def __nextTick(self):
        self.__ticks+=1
        #escritor.flog("transcurrido tik " + str(self.__ticks))
        

        if self.__playMode==1:
            step = self.__song.getStep(self.__ticks)
            #escritor.escribirLog("lo encontrado es " + str(step))
            self.__checkStepTime()
            

            if len(step) >0:

                self.__stepStack+=step
                #escritor.flog("añadido paso al stack" + str(step[1]) + " en el tiempo " + str(self.__ticks))
                for st in step:
                    hitEvent(st[1])
            


        if(soundevents.musicIsPlay() == False):
            if(self.__playMode == 0):
                #self.__song.saveSteplist()

                #escritor.saveSong(self.__song)
                pass

            elif self.__playMode==1:
                self.player.sumarMiss(len(self.__stepStack))
            endSongEvent()
            

    def __checkStepTime(self):
        """se remueven los steps que hayan estado por más del pressspeed  ticks en el stack"""
        
        for x in range(0, len(self.__prestep)):
            if self.__ticks - self.__prestep[x][0] >= self.__antisipateTime:
                self.__prestep.pop(x)
                self.player.sumarMiss(1)
                soundevents.applyVolumeMusicFactor(0.2)

                self.consecutivePoints=0
                
                self.checkLife(True)
                self.__checkStepTime()
                return()
            else:
                if len(self.__stepStack) >0:
                    step = self.__stepStack[0]
                    if step[1] == self.__prestep[x][1]:
                        self.__stepStack.pop(0)
                        self.__prestep.pop(x)
                        soundevents.unapplyVolumeMusicFactor(0.2)

                        self.player.sumarPuntos(1)
                        self.consecutivePoints+=1
                        self.checkLife()
                        self.__checkStepTime()
                        return()


                    else:
                        self.__prestep.pop(x)
                        self.__stepStack.pop(0)
                        
                        soundevents.applyVolumeMusicFactor(0.2)
                        self.consecutivePoints=0
                        self.checkLife(True)

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
                
                self.checkLife(True)
                soundevents.applyVolumeMusicFactor(0.2)
                self.__checkStepTime()
                
                
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


        

    def __init__(self, cancion, modo, tipo= 0, startHP =-1, restoreHpInPlay=True, maxHP = -1):
        object.__init__(self)
        self.player= jugador.Jugador()
        self.__ticks=0
        global hitEvent
        global nextTickEvent
        global stepEvent
        global deatEvent

        nextTickEvent+=self.__nextTick

        self.__song = cancion
        
        
        self.player.resetPoints()
        self.restoreHPInPlay = restoreHpInPlay
        
        if startHP!= -1:
            self.player.setHP(startHP)
            
            
        else:
            self.player.setHP(self.__song.getStartHp())

        if maxHP != -1:
            self._maxHP = maxHP
        else:
            self._maxHP=self.__song.getStartHp()
            
        #soundevents.musicSetVolume(1)
        soundevents.loadSong(self.__song.songpath)
        self.__pressSpeed = self.__song.getPressSpeed()
        #print(" este es el presspeed" + str(self.__pressSpeed))
        soundevents.twoHands=self.__song.getHands()
        self.__antisipateTime = self.__song.getAntisipateTime()

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
        

    def calculatePoints(self):
        points = self.player.getPuntos() - self.player.getMiss()
        totalpoints = len(self.__song.getAllSteps())
        percent = (points*100)/totalpoints
        return(int(percent))
        



    def calculateMark(self):
        points = self.player.getPuntos() - self.player.getMiss()
        totalpoints = len(self.__song.getAllSteps())

        
        
        escritor.flog("se consiguieron un total de: " + str(points) + " de un total de " + str(totalpoints) + " con : " + str(self.player.getMiss()) + " fallas ")
        if points <= 0:
            return("f")
        else:
            percent = (points*100)/totalpoints
            if percent>=95:
                return("s")
            elif percent >= 80 :
                return("a")
            elif percent>= 65:
                return("b")
            elif percent>= 50:
                return("c")
            elif percent>=35:
                return("d")
            elif percent>= 15:
                return("e")
            else:
                    return("f")

    def getSong(self):
        return(self.__song)
