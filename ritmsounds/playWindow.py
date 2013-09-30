#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor

def endSong():
    global end
    end = True


def startWindow( width, height,cancion):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("Modo juego!")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de juego de la canción: " + cancion)
    
    jugo = juego.Juego(cancion,1)
    teclas = {}
    teclas[K_a] = 0
    teclas[K_s] = 1
    teclas[K_z] = 2
    teclas[K_x] = 3
    reloj = pygame.time.Clock()
    global end
    end = False
    pantalla.fill((134,230,120))
    letras = pygame.font.Font(None, 14)
    mensaje = "precione las teclas a, s, z y x al ritmo de la canción y como quiera para grabar los pasos!"
    mensaje2 = "Precione escape para retornar al menú y detener el juego"
    msj1 = letras.render(mensaje,1,(255,255,255), (100,100,100))
    msj2 = letras.render(mensaje2,1,(255,255,255))
    
    pantalla.blit(msj1, (50,10))
    pantalla.blit(msj2,(50,60))
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
                del jugo
                escritor.flog("cierre modo juego por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                if event.key == K_s or event.key == K_a or event.key == K_x or event.key == K_z:
                    juego.stepEvent(teclas[event.key])
                    escritor.flog("precionada la tecla número " + str(teclas[event.key]))

                elif(event.key == K_ESCAPE):
                    pygame.display.quit()
                    jugo.stop()
                    del jugo

                    escritor.flog("cierre por escape")
                    end=True

    pygame.display.quit()
    print ("los resultados fueron " + str(jugo.player))















