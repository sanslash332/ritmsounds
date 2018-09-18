#!/usr/bin/python

import juego
import pygame
from pygame.locals import *
import escritor
import keyManager
import messagesManager as m

def endSong():
    global end
    end = True


def startWindow( width, height,cancion):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("Modo grabaci�n!")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de grabaci�n de la canci�n: " + cancion.name)
    escape=False
    jugo = juego.Juego(cancion,0)
    reloj = pygame.time.Clock()
    global end
    end = False
    pantalla.fill((134,230,120))
    
    
    mensaje = m.getMessage('recordwindow:help', pygame.key.name(keyManager.getConfiguredKey("back")))
    
    pygame.display.flip()
    m.sayCustomMessage(mensaje,1)
    
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
                
                escritor.flog("cierre modo prueba por evento de salida")
                escape=True
                return(None)
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey!='back' and pressKey!='null':
                    juego.hitEvent(pressKey)
                    #escritor.flog("precionada la tecla " + pressKey)

                elif(pressKey== 'back' and pressKey!='null'):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    
                    jugo.stop()
                    
                    end=True
                    escape=True
                    return(None)

    pygame.display.quit()
    if escape == False:

        jugo.stop()
        return(jugo.getSong())