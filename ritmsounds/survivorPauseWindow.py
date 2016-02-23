#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import jugador
import soundevents
import messagesManager as m

def startWindow( width, height, cansion, hpactual, completadas, hprecuperado):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption(" Resultados")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    



    pantalla.fill((134,230,120))
    
    
    pygame.display.flip()
    soundevents.musicLoad(cansion.songpath)
    soundevents.musicPlay()
    messagestate=0
    message = ""
    if hprecuperado==False:
        message=m.getMessage('survivorpausewindow:message0', hpactual)
    else:
        message=m.getMessage('survivorpausewindow:message1', hpactual)




    last = message
    m.sayCustomMessage(message,1)

    while (not end):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
                return(-1)
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey=='back':
                    pygame.display.quit()
                    end=True
                    return(-1)

                if  pressKey=='accept':
                    if messagestate==2:

                        pygame.display.quit()
                        escritor.flog("cierre por escape")
                        end=True
                        soundevents.playSurvivorStart()
                        time.sleep(2)
                        return(0)

                    else:
                        soundevents.playAccept()
                        messagestate=2
                        message=m.getMessage('survivorpausewindow:message2', cansion.name, cansion.getSteplistname())
                        last=message
                        m.sayCustomMessage(message)

                else:
                    m.sayCustomMessage(message)




















