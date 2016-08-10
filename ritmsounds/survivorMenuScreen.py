#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import keyManager
import soundevents
from pygame.locals import *
import escritor
import time
import messagesManager as m
import survivorManager
import textInput

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("RitmSounds: Survivor")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("Iniciado menú de survivor ")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    svm = survivorManager.SurvivorManager()
    menuitems= _buildmenu(svm)
    
    escritor.flog("menú construido")
    titulo = "survivormenu:help"
    last= titulo
    menuhelp = "survivormenu:help"
    
    escritor.flog("refrescando pantalla")
    pygame.display.flip()
    escritor.flog("pantalla refrescada")
    
    
    soundevents.musicLoad("bgm/survivor.ogg")
    soundevents.musicPlay(True)
    #soundevents.musicSetVolume(0.6)

    
    option=0
    m.sayMessage(titulo)
    escritor.flog("iniciando menuloop")
    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))

        pygame.display.flip()
        

        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cerrando juego por evento de cierre. quit event")
                return(None)
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey== 'accept':
                    escritor.flog("detectado enter")
                    if option==-1:
                        soundevents.musicStop()

                        soundevents.playSurvivorStart()
                        time.sleep(2)

                        return(svm)
                        escritor.flog("survivor configurado")
                    elif option==0:
                        soundevents.playChange()
                        valure = int(textInput.start(True))
                        if valure>0 and valure<= 100:
                            svm.maxHP=valure
                        else:
                            soundevents.playError()
                            m.sayMessage("survivormenu:errorzero")
                            time.sleep(2)
                    elif option==1:
                        soundevents.playChange()
                        svm.pauseBetweenSongs= not svm.pauseBetweenSongs
                    elif option==2:
                        soundevents.playChange()
                        svm.restoreAllHp=  not svm.restoreAllHp
                    elif option ==3:
                        soundevents.playChange()
                        svm.restoreHpInSongs= not svm.restoreHpInSongs
                    elif option==4:
                        soundevents.playChange()
                        svm.HPRestoreRangeDeterminedBySong= not svm.HPRestoreRangeDeterminedBySong




                    menuitems=_buildmenu(svm)
                    m.sayCustomMessage(menuitems[option])


                elif pressKey == 'down':
                    
                    soundevents.playMove()
                    option+=1
                    escritor.flog("movida opción a %i " % option)
                    if option>=5:
                        option=-1
                        escritor.flog("movida opción a %i " % option)

                    m.sayCustomMessage(menuitems[option])



                elif pressKey == 'up':
                    
                    soundevents.playMove()
                    option -= 1
                    escritor.flog("movida opción a %i " % option)
                    if option< -1:
                        option=4
                        escritor.flog("movida opción a %i " % option)
                    m.sayCustomMessage(menuitems[option])

                elif(pressKey=='back'):
                    escritor.flog("presionado escape")
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                    return(None)

                else:
                    if pressKey!= "stop":
                        m.sayMessage(last)


def _buildmenu(svm):
    menuitems=[]
    menuitems.append(m.getMessage("survivormenu:option0", svm.maxHP))
    if svm.pauseBetweenSongs==True:
        menuitems.append(m.getMessage("survivormenu:option1", m.getMessage("confirm")))
    else:
        menuitems.append(m.getMessage("survivormenu:option1", m.getMessage("cancel")))
    if svm.restoreAllHp==True:
        menuitems.append(m.getMessage("survivormenu:option2", m.getMessage("confirm")))
    else:
        menuitems.append(m.getMessage("survivormenu:option2", m.getMessage("cancel")))
    
    if svm.restoreHpInSongs==True:
        menuitems.append(m.getMessage("survivormenu:option3", m.getMessage("confirm")))
    else:
        menuitems.append(m.getMessage("survivormenu:option3", m.getMessage("cancel")))
    
    
    

    
    if svm.HPRestoreRangeDeterminedBySong==True:
        menuitems.append(m.getMessage("survivormenu:option4", m.getMessage("confirm")))
    else:
        menuitems.append(m.getMessage("survivormenu:option4", m.getMessage("cancel")))
    
    
    menuitems.append(m.getMessage("survivormenu:optionconfirm"))
    return(menuitems)
    
