#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import soundevents
import messagesManager as m
import time

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("modo prueba de teclas")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    soundevents.twoHands=2
    mensage = m.getMessage("testwindow:help", pygame.key.name(keyManager.getConfiguredKey("l1")), pygame.key.name(keyManager.getConfiguredKey("l2")), pygame.key.name(keyManager.getConfiguredKey("l3")), pygame.key.name(keyManager.getConfiguredKey("l4")), pygame.key.name(keyManager.getConfiguredKey("r1")), pygame.key.name(keyManager.getConfiguredKey("r2")), pygame.key.name(keyManager.getConfiguredKey("r3")), pygame.key.name(keyManager.getConfiguredKey("r4")), pygame.key.name(keyManager.getConfiguredKey("back")))
    
    
    pygame.display.flip()
    time.sleep(1)
    m.sayCustomMessage(mensage,1)



    while (not end):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)

                if pressKey!= 'back' and pressKey!='null':
                    juego.hitEvent(pressKey)
                    escritor.flog("precionada la tecla  " + pressKey)

                elif(pressKey=='back'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                else:
                    m.sayCustomMessage(mensage,1)
