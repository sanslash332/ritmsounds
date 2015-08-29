#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager

def endSong():
    global end
    end = True


def startWindow( width, height,cancion, modo=0):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("Modo juego!")
    escape = False
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de juego de la canción: " + cancion.name)
    
    jugo = juego.Juego(cancion,1,modo)
    reloj = pygame.time.Clock()
    global end
    end = False
    pantalla.fill((134,230,120))
    
    mensaje = "precione las teclas a, s, z y x al ritmo de la canción a medida que el sonido correspondiente suena!!!"
    mensaje2 = "Precione escape para retornar al menú y detener el juego"
    
    
    
    pygame.display.flip()
    
    jugo.start()
    juego.endSongEvent+=endSong

    while (not end):
        reloj.tick_busy_loop(60)
        
        juego.nextTickEvent()
        
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                jugo.stop()
                #del jugo
                escritor.flog("cierre modo juego por evento de salida")
                escape=True
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey!='back' and pressKey!='null':

                    juego.stepEvent(pressKey)
                    escritor.flog("precionada la tecla " + pressKey)

                elif(pressKey=='back'):
                    pygame.display.quit()
                    jugo.stop()
                    #del jugo
                    escape=True
                    return(None)

                    escritor.flog("cierre por escape")
                    end=True

    pygame.display.quit()
    if escape==False:

        jugo.stop()
    if (jugo is None) == False:

        return(jugo)















