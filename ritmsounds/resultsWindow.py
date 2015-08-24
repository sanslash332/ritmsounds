#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import jugador
import soundevents

def startWindow( width, height, jg):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption(" Resultados")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    



    pantalla.fill((134,230,120))
    letras = pygame.font.Font(None, 14)
    if jg.player.getHP() == 0:
        soundevents.musicLoad("songs/death.mp3")
        soundevents.musicPlay()
        mensaje = "¡Moriste! No pudiste terminar la cancion. A penas conseguiste " + str(jg.player.getPuntos()) + " con " + str(jg.player.getMiss()) + " fallas."
    else:
        soundevents.musicLoad("songs/results.mp3")
        soundevents.musicSetVolume(0.5)
        soundevents.musicPlay()
        mensaje = "¡felicidades! optuviste un total de: " + str(jg.player.getPuntos()) + " aciertos, y un total de: " + str(jg.player.getMiss()) + " fallas. " 

    
    mensaje2 = "Presione cualquier tecla para continuar"
    msj1 = letras.render(mensaje,1,(255,255,255), (100,100,100))
    msj2 = letras.render(mensaje2,1,(255,255,255))
    
    pantalla.blit(msj1, (200,10))
    pantalla.blit(msj2,(200,300))
    pygame.display.flip()


    


    while (not end):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)

                if  pressKey!='null':
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True


















