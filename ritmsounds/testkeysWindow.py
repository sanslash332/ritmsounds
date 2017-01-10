#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import soundevents
import messagesManager as m
import time

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("modo prueba de teclas")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    soundevents.twoHands=2
    mensage = m.getMessage("testwindow:help", pygame.key.name(keyManager.getConfiguredKey("l1")), pygame.key.name(keyManager.getConfiguredKey("l2")), pygame.key.name(keyManager.getConfiguredKey("l3")), pygame.key.name(keyManager.getConfiguredKey("l4")), pygame.key.name(keyManager.getConfiguredKey("r1")), pygame.key.name(keyManager.getConfiguredKey("r2")), pygame.key.name(keyManager.getConfiguredKey("r3")), pygame.key.name(keyManager.getConfiguredKey("r4")), pygame.key.name(keyManager.getConfiguredKey("down")), pygame.key.name(keyManager.getConfiguredKey("up")), pygame.key.name(keyManager.getConfiguredKey("accept")), pygame.key.name(keyManager.getConfiguredKey("back")))
    soundevents.musicLoad("bgm/test.ogg")
    soundevents.musicPlay(True)

    
    
    pygame.display.flip()
    time.sleep(1)
    m.sayCustomMessage(mensage,1)
    menu=buildMenu()
    option=0



    while (not end):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey=="up":
                    soundevents.playMove()
                    option-=1
                    if option<0:
                        option= len(menu)-1
                    m.sayCustomMessage(menu[option])

                elif pressKey=="down":
                    soundevents.playMove()
                    option+=1
                    if option >=len(menu):
                        option=0
                    m.sayCustomMessage(menu[option])

                elif pressKey=="accept":
                    activeOption(option)
                    
                elif pressKey!= 'back' and pressKey!='null':
                    juego.hitEvent(pressKey)
                    escritor.flog("precionada la tecla  " + pressKey)

                elif(pressKey=='back'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                else:
                    m.sayCustomMessage(mensage,1)

def buildMenu():
    menu=[]
    for x in range(0,8):
        menu.append(m.getMessage("testwindow:menuitem"+str(x)))
    return(menu)




def activeOption(option):
    if option==0:
        juego.hitEvent("l1")
        juego.hitEvent("r1")
    elif option ==1:
        juego.hitEvent("l2")
        juego.hitEvent("r2")
    elif option==2:
        juego.hitEvent("l3")
        juego.hitEvent("r3")
    elif option==3:
        juego.hitEvent("l4")
        juego.hitEvent("r4")
    elif option==4:
        soundevents.playLowHp()
    elif option==5:
        soundevents.playRestoreHP()
    elif option == 6:
        soundevents.playdeath()
    elif option ==7:
        juego.startEvent()



