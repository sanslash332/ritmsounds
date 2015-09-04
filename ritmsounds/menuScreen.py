#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import keyManager
import soundevents
from pygame.locals import *
import escritor
import time
import messagesManager as m

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("RitmSounds: main menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("Iniciado menu principal")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    menuitems=[]
    menuitems.append("menuwindow:option0")
    menuitems.append("menuwindow:option1")
    menuitems.append("menuwindow:option2")
    menuitems.append("menuwindow:option3")
    menuitems.append("menuwindow:optionexit")

    titulo = "menuwindow:title"
    last= titulo
    menuhelp = "menuwindow:help"
    
    pygame.display.flip()
    estitulo =True
    
    soundevents.musicLoad("songs/rtms.ogg")
    soundevents.musicPlay(True)
    soundevents.musicSetVolume(0.4)

    
    option=0
    m.sayMessage(titulo)

    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))

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
                        m.sayMessage(menuhelp)
                        last=menuhelp
                    else:
                        if option==4:
                            pygame.display.quit()
                            soundevents.musicFade(1500)
                            time.sleep(2)
                            

                            return(4)
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
                    if option>=5:
                        option=0
                    m.sayMessage(menuitems[option])



                elif pressKey == 'up':
                    if estitulo:
                        continue 

                    soundevents.playMove()
                    option -= 1 
                    if option<0:
                        option=4
                    m.sayMessage(menuitems[option])

                elif(pressKey=='back'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                    return(4)

                else:
                    if pressKey!= "stop":
                        m.sayMessage(last)
