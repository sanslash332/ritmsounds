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
import recordMenuScreen
import os


screen_width = 1024
screen_height =768
def start():
    songs_dir = "songs/"
    option = -1 
    pg.init()
    pg.display.set_caption("tiflojuegos")
    pg.display.set_mode((1024,768))

    soundevents.musicLoad("bgm/tiflojuegoslogo.ogg")
    soundevents.musicPlay()

    while soundevents.musicIsPlay():
        for ev in pg.event.get():
            if ev.type==pg.KEYDOWN:
                if ev.key==K_RETURN or ev.key==K_SPACE or ev.key==K_ESCAPE:
                    soundevents.musicStop()




    while option!=4:
        option = menuScreen.startWindow(screen_width,screen_height)
        escritor.flog("capturada la opcion: "+ str(option) + " en el menu ")
        if option==0 or option==1:
            s = selectSonScreen.startWindow(screen_width,screen_height)
            if s is None:
                continue
            else:
            

                j = playWindow.startWindow(screen_width,screen_height,s,option)
                if j is not None:
                    resultsWindow.startWindow(screen_width,screen_height,j)

        elif option == 2:
            testkeysWindow.startWindow(screen_width,screen_height)
        elif option == 3:
            recordMenuScreen.startWindow(1024,768)






if __name__=='__main__':
    start()