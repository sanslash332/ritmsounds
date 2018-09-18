#!/usr/bin/python

import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import jugador
import soundevents
import messagesManager as m

def startWindow( width, height, jg):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption(" Resultados")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    



    pantalla.fill((134,230,120))
    aciertos = jg.player.getPuntos()
    fallos = jg.player.getMiss()
    nota=jg.calculateMark()
    

    puntos=jg.calculatePoints()
    
    
    
    
    if jg.player.getHP() == 0:
        soundevents.musicLoad("bgm/death.mp3")
        m.sayMessage('resultswindow:start')
        soundevents.playResults(int(puntos/5))

        
        mensaje = m.getMessage("resultswindow:death", puntos, aciertos)
    else:
        soundevents.musicLoad("bgm/results.mp3")
        #soundevents.musicSetVolume(0.5)
        
        m.sayMessage('resultswindow:start')

        soundevents.playResults(int(puntos/5))

        mensaje = m.getMessage('resultswindow:congratulations', puntos, aciertos, fallos, nota)

    
    pygame.display.flip()
    m.sayCustomMessage(mensaje,1)
    soundevents.musicPlay(-1)



    


    while (not end):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)

                if  pressKey=='accept':
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                else:
                    m.sayCustomMessage(mensaje)
