#!/usr/bin/python

import pygame
import soundevents
import messagesManager as m
from pygame.locals import *
import keyManager
import escritor

def start(onlyNums=False):
    res=(1024,768)

    pygame.init()
    pantalla=pygame.display.set_mode(res)

    end=False
    simbols = "Z/X/C/V/B/N/M/A/S/D/F/G/H/J/K/L/Ñ/Q/W/E/R/T/Y/U/I/O/P/1/2/3/4/5/6/7/8/9/0/z/x/c/v/b/n/m/,/./-/;/:/_/a/s/d/f/g/h/j/k/l/ñ/q/w/e/r/t/y/u/i/o/p/'/¿/?/¡/!/#/$/%/&/(/)/=/+/*/[/]/{/}"
    numbersimbols = "1/2/3/4/5/6/7/8/9/0"
    if onlyNums:
        validSimbols = numbersimbols.split('/')
    else:


        validSimbols = simbols.split('/')
    text=""
    reloj = pygame.time.Clock()
    mensage= m.getMessage("text:help")
    m.sayCustomMessage(mensage,0)

    while(not end):
        reloj.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)

                if pressKey== 'accept':
                    if len(text) == 0:
                        m.sayMessage("text:empty")
                    else:
                        end=True
                        soundevents.playAccept()


                    

                elif(pressKey=='back'):
                    #pygame.display.quit()
                    soundevents.playback()
                    escritor.flog("cierre por escape")
                    end=True
                    return(None)
                elif event.key== K_BACKSPACE and len(text) >0:
                    m.sayMessage("text:delete",1,text[-1])
                    text = text[:-1]
                    soundevents.playChange()

                elif event.key == K_SPACE:
                    text+=" "
                    m.sayCustomMessage(text,1)
                    soundevents.playRestoreHP()

                else:
                    chara = pygame.key.name(event.key)
                    if chara in validSimbols:
                        m.sayCustomMessage(chara,1)
                        text+=chara
                        soundevents.playRestoreHP()
                    else:
                        m.sayCustomMessage(mensage,1)

    return(text)
