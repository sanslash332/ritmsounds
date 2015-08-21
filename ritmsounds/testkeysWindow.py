#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("modo prueba de teclas")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    letras = pygame.font.Font(None, 14)
    mensaje = "precione las teclas a, s, z y x para oír los sonidos a los que corresponden."
    mensaje2 = "Precione escape para retornar al menú"
    msj1 = letras.render(mensaje,1,(255,255,255), (100,100,100))
    msj2 = letras.render(mensaje2,1,(255,255,255))
    
    pantalla.blit(msj1, (50,10))
    pantalla.blit(msj2,(50,60))
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

                if pressKey!= 'back' and pressKey!='null':
                    juego.hitEvent(pressKey)
                    escritor.flog("precionada la tecla  " + pressKey)

                elif(pressKey=='back'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True

















