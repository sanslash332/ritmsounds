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


def startWindow( width, height,cancion):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("Modo grabación!")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de grabación de la canción: " + cancion.name)
    escape=False
    jugo = juego.Juego(cancion,0)
    reloj = pygame.time.Clock()
    global end
    end = False
    pantalla.fill((134,230,120))
    letras = pygame.font.Font(None, 14)
    mensaje = "precione las teclas a, s, z y x al ritmo de la canción y como quiera para grabar los pasos!"
    mensaje2 = "Precione escape para retornar al menú y abortar la grabación"
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
                escritor.flog("cierre modo prueba por evento de salida")
                escape=True
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey!='back' and pressKey!='null':
                    juego.hitEvent(pressKey)
                    escritor.flog("precionada la tecla " + pressKey)

                elif(pressKey== 'back' and pressKey!='null'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    
                    jugo.stop()
                    del jugo
                    end=True
                    escape=True

    pygame.display.quit()
    if escape == False:

        jugo.stop()















