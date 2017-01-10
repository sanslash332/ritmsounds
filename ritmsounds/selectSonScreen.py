#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import keyManager
import soundevents
from pygame.locals import *
import escritor
import time
import messagesManager as m
import loadWindow
import threading


def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("RitmSounds: main menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciada pantalla de seleccion")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    
    
    menuitems=[]
    tred = threading.Thread(target=escritor.loadAllSongs)
    tred.start()




    #songs = escritor.loadAllSongs()
    songs = loadWindow.startWindow(width,height,escritor.itemsLoaded)
    if(songs==False):

        return(None
)



    mensage = m.getMessage("selectwindow:help")
    mensage2 = m.getMessage("selectwindow:help2")
    mensage3 = m.getMessage("selectwindow:help3", pygame.key.name(keyManager.getConfiguredKey("l1")), pygame.key.name(keyManager.getConfiguredKey("l2")), pygame.key.name(keyManager.getConfiguredKey("l3")), pygame.key.name(keyManager.getConfiguredKey("l4")), pygame.key.name(keyManager.getConfiguredKey("r1")), pygame.key.name(keyManager.getConfiguredKey("r2")), pygame.key.name(keyManager.getConfiguredKey("r3")), pygame.key.name(keyManager.getConfiguredKey("r4")))


    pygame.display.flip()
    estitulo =True
    esayuda=False
    

    
    option=0
    m.sayCustomMessage(mensage,1)
    repeat = mensage
    dificultad = 0 

    if len(songs) == 0:
        m.sayMessage("selectwindow:nosongs",1)
        return(None)

    soundevents.musicLoad(songs[option].songpath)
    soundevents.musicPlay(True)
    m.sayCustomMessage(songs[option].name,0)


    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        pygame.display.flip()
        #soundevents.musicSetVolume(soundevents.musicVolume*0.5)


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
                    if estitulo==True and esayuda== False:
                        estitulo=False
                        m.sayCustomMessage(mensage2,1)
                        repeat=mensage2
                        songs[option].selectSteplist(dificultad)
                        h = songs[option].getHands()
                        if h ==2:
                            m.sayMessage('selectwindow:difdescription2', 0, songs[option].getSteplistname(), songs[option].getStartHp(), songs[option].getPressSpeed())
                        else:
                            m.sayMessage('selectwindow:difdescription', 0, songs[option].getSteplistname(), songs[option].getStartHp(), songs[option].getPressSpeed())

                        
                    elif estitulo==False and esayuda == False:
                        esayuda = True
                        m.sayCustomMessage(mensage3,1)
                        repeat = mensage3


                    else:
                        soundevents.playGoSound()
                        pygame.display.quit()
                        end=True
                        #soundevents.musicSetVolume(soundevents.musicVolume/0.5)

                        soundevents.musicFade(1500)
                        return(songs[option])
                elif pressKey == 'down':
                    if estitulo:
                        

                        soundevents.playMove()
                        option+=1
                        if option>=len(songs):
                            option=0
                        soundevents.musicLoad(songs[option].songpath)
                        soundevents.musicPlay(-1)
                        m.sayCustomMessage(songs[option].name,1)


                    elif estitulo == False and esayuda:
                        continue
                    else:
                        soundevents.playChange()
                        dificultad+=1
                        if dificultad>= len(songs[option].getAllStepslist()):
                            dificultad=0
                        songs[option].selectSteplist(dificultad)
                        h = songs[option].getHands()
                        if h ==2:
                            m.sayMessage('selectwindow:difdescription2', 1, songs[option].getSteplistname(), songs[option].getStartHp(), songs[option].getPressSpeed())
                        else:
                            m.sayMessage('selectwindow:difdescription', 1, songs[option].getSteplistname(), songs[option].getStartHp(), songs[option].getPressSpeed())

                elif pressKey == 'up':
                    if estitulo:
                        

                        soundevents.playMove()
                        option -= 1 
                        if option<0:
                            option=len(songs)-1
                        soundevents.musicLoad(songs[option].songpath)
                        soundevents.musicPlay(-1)
                        m.sayCustomMessage(songs[option].name,1)


                    elif esayuda:
                        continue
                    else:
                        soundevents.playChange()
                        dificultad-=1
                        if dificultad< 0:
                            dificultad=len(songs[option].getAllStepslist())-1
                        songs[option].selectSteplist(dificultad)
                        h = songs[option].getHands()
                        if h ==2:
                            m.sayMessage('selectwindow:difdescription2', 1, songs[option].getSteplistname(), songs[option].getStartHp(), songs[option].getPressSpeed())
                        else:
                            m.sayMessage('selectwindow:difdescription', 1, songs[option].getSteplistname(), songs[option].getStartHp(), songs[option].getPressSpeed())

                        


                elif(pressKey=='back'):
                    if estitulo:

                        pygame.display.quit()
                        escritor.flog("cierre por escape")
                        end=True
                    else:
                        estitulo=True
                        esayuda=False
                        option=0
                        dificultad=0
                        repeat= mensage
                        m.sayCustomMessage(mensage,1)
                        soundevents.musicLoad(songs[option].songpath)
                        soundevents.musicPlay()
                        m.sayCustomMessage(songs[option].name,0)



                else:
                    if pressKey!="stop":
                        m.sayCustomMessage(repeat)
