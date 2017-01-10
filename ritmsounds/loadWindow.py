#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import jugador
import soundevents
import messagesManager as m
finalitem=False
ended=False


def loadEnded(obj):
    global finalitem, ended
    finalitem=obj
    ended=True




def startWindow( width, height, eventToWait):
    global ended, finalitem
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("ritmsounds:  Loading")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    eventToWait+=loadEnded

    



    pantalla.fill((134,230,120))
    
    soundevents.musicLoad("bgm/death.mp3")
    mensaje = m.getMessage("loadwindow:loading")
    
    
    pygame.display.flip()
    m.sayCustomMessage(mensaje,1)
    soundevents.musicPlay(-1)



    


    while (not ended):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)

                if  pressKey=='back':
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                    soundevents.musicFade(500)
                    ended=False
                    finalitem=False
                    eventToWait-=loadEnded
                    return False
                else:
                    m.sayCustomMessage(mensaje)
    soundevents.musicFade(500)
    backup = finalitem
    finalitem=False
    ended=False
    eventToWait-=loadEnded

    return(backup)