#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame as pg
import juego
import song
import eventos
import escritor
import resultsWindow
from pygame.locals import *
import soundevents
import testkeysWindow
import recordWindow
import playWindow
import menuScreen
import selectSonScreen
import os


screen_width = 640
screen_height =480
songs_dir = "songs/"
option = -1 

while option!=3:
    option = menuScreen.startWindow(screen_width,screen_height)
    escritor.flog("capturada la opcion: "+ str(option) + " en el menu ")
    if option==0:
        s = selectSonScreen.startWindow(screen_width,screen_height)
        if s is None:
            continue
        else:
            s.selectSteplist(0)

            j = playWindow.startWindow(screen_width,screen_height,s)
            if j is not None:
                resultsWindow.startWindow(screen_width,screen_height,j)









    elif option == 1:
        pass
    elif option == 2:
        testkeysWindow.startWindow(screen_width,screen_height)





