    #!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import keyManager
import soundevents
from pygame.locals import *
import escritor
import time
import messagesManager as m
import playWindow
import random
import song
import survivorPauseWindow
import survivorResultsWindow

class SurvivorManager:
    """ class for control the survivor mode, and the random chooce of the songs, etc"""
    def __init__(self,songs):
        self.maxHP = 30
        self.restoreAllHp = False
        self.restoreHpInSongs = True
        self.pauseBetweenSongs = False
        self.HPRestoreRangeDeterminedBySong = True
        self.songs=songs
        self.completedSongs = 0
        self.currentHP = -1
        self.lastGame=None
        self.totalPoints=0


    def surviveStart(self):
        self.currentHP=self.maxHP
        if self.pauseBetweenSongs==False:
            soundevents.survivorJump=True
        while self.currentHP>0:
            firstsong = self.completedSongs==0

            s = self.betweenSongs(firstsong)
            
            if s ==None:
                break

            self.lastGame= playWindow.startWindow(1024,768, s, 0, startHP=self.currentHP, restoreHpInPlay=self.restoreHpInSongs, maxHP= self.maxHP)
            if self.lastGame==None:
                break
            self.currentHP= self.lastGame.player.getHP()
            self.totalPoints+=self.lastGame.player.getPuntos()
            if self.currentHP>0:
                self.completedSongs+=1


        self.resultsOfSurvive()



    def betweenSongs(self,firstsong=False):
        if self.restoreAllHp==True:
            self.currentHP=self.maxHP
        
        ind = random.randint(0,len(self.songs)-1)
        currentSong=self.songs[ind]
        dificulti= random.randint(0,len(currentSong.getAllStepslist())-1)
        currentSong.selectSteplist(dificulti)
        currentSong.restartSong()
        if self.HPRestoreRangeDeterminedBySong==False:
            currentSong.setStartHp(self.maxHP)
        
        if self.pauseBetweenSongs==True and firstsong==False:
            o = survivorPauseWindow.startWindow(1024,768, currentSong,self.currentHP, self.completedSongs, self.restoreAllHp)
            if o == -1:
                return(None)
        else:
            
            soundevents.playSurvivorStart()
            time.sleep(2)






        return(currentSong)



        

    def resultsOfSurvive(self):
        soundevents.survivorJump=False
        survivorResultsWindow.startWindow(1024,768, self.completedSongs, self.totalPoints)



