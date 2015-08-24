#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import keyManager
import soundevents
from pygame.locals import *
import escritor
import time

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("RitmSounds: main menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("Iniciado menu principal")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    letras = pygame.font.Font(None, 14)
    letrasGrandes = pygame.font.Font(None, 20)
    menuitems=[]
    mensaje = "Jugar una cancion"
    mensaje2 = "Grabar una cancion"
    mensaje3 = "Provar teclas"
    mensaje4 = "Salir"
    mensajeTitulo = "bienvenido a ritmsounds!"

    menuitems.append(letras.render(mensaje,1,(255,255,255), (100,100,100)))
    menuitems.append(letras.render(mensaje2,1,(255,255,255), (100,100,100)))
    menuitems.append(letras.render(mensaje3,1,(255,255,255), (100,100,100)))
    menuitems.append(letras.render(mensaje4,1,(255,255,255), (100,100,100)))
    titulo = letrasGrandes.render(mensajeTitulo,1,(255,255,255), (100,100,100))
    pantalla.blit(titulo, (50,50))
    
    pygame.display.flip()
    estitulo =True
    
    soundevents.musicLoad("songs/rtms.ogg")
    soundevents.musicPlay(True)
    soundevents.musicSetVolume(0.3)

    
    option=0
    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        if estitulo:
            pantalla.blit(titulo, (400,250))
        else:
            pantalla.blit(menuitems[option], (400,300))
    
        pygame.display.flip()
        

        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                exit()
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey== 'accept':
                    
                    soundevents.playAccept()
                    if estitulo==True:
                        estitulo=False
                    else:
                        if option==3:
                            pygame.display.quit()
                            soundevents.musicFade(1500)
                            time.sleep(2)
                            

                            exit()
                        else:
                            pygame.display.quit()
                            end=True
                            soundevents.musicFade(1500)
                            return(option)
                elif pressKey == 'down':
                    if estitulo:
                        continue 

                    soundevents.playMove()
                    option+=1
                    if option>=4:
                        option=0


                elif pressKey == 'up':
                    if estitulo:
                        continue 

                    soundevents.playMove()
                    option -= 1 
                    if option<0:
                        option=3

                elif(pressKey=='back'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True

















