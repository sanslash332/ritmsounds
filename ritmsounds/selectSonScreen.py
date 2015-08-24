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
    songs = escritor.loadAllSongs()

    mensaje = "Jugar una cancion"
    mensaje2 = "Grabar una cancion"
    mensaje3 = "Provar teclas"
    mensaje4 = "Salir"
    mensajeTitulo = "Seleccione la cancion que quiere jugar. Escoja con las flechas y acepte con enter"

    menuitems.append(letras.render(mensaje,1,(255,255,255), (100,100,100)))
    menuitems.append(letras.render(mensaje2,1,(255,255,255), (100,100,100)))
    menuitems.append(letras.render(mensaje3,1,(255,255,255), (100,100,100)))
    menuitems.append(letras.render(mensaje4,1,(255,255,255), (100,100,100)))
    titulo = letrasGrandes.render(mensajeTitulo,1,(255,255,255), (100,100,100))
    pantalla.blit(titulo, (50,50))
    
    pygame.display.flip()
    estitulo =True
    

    
    option=0
    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        if estitulo:
            pantalla.blit(titulo, (400,250))
        else:
            songname = letras.render(songs[option].name ,1,(255,255,255), (100,100,100))
            pantalla.blit(songname, (400,300))
    
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
                        soundevents.musicLoad(songs[option].songpath)
                        soundevents.musicPlay(True)


                    else:
                        pygame.display.quit()
                        end=True
                        soundevents.musicFade(1500)
                        return(songs[option])
                elif pressKey == 'down':
                    if estitulo:
                        continue 

                    soundevents.playMove()
                    option+=1
                    if option>=len(songs):
                        option=0
                    soundevents.musicLoad(songs[option].songpath)
                    soundevents.musicPlay(True)



                elif pressKey == 'up':
                    if estitulo:
                        continue 

                    soundevents.playMove()
                    option -= 1 
                    if option<0:
                        option=len(songs)-1
                    soundevents.musicLoad(songs[option].songpath)
                    soundevents.musicPlay(True)


                elif(pressKey=='back'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True

















