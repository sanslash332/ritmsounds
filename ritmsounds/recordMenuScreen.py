    #!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import keyManager
import soundevents
from pygame.locals import *
import escritor
import time
import messagesManager as m
import textInput
import recordWindow
import playWindow
import time
import loadWindow
import threading

mensage = m.getMessage("recordmenu:help")
mensage2 = m.getMessage("recordmenu:help2")
mensage3 = m.getMessage('recordmenu:help3',  pygame.key.name(keyManager.getConfiguredKey("l1")), pygame.key.name(keyManager.getConfiguredKey("l2")), pygame.key.name(keyManager.getConfiguredKey("l3")), pygame.key.name(keyManager.getConfiguredKey("l4")), pygame.key.name(keyManager.getConfiguredKey("r1")), pygame.key.name(keyManager.getConfiguredKey("r2")), pygame.key.name(keyManager.getConfiguredKey("r3")), pygame.key.name(keyManager.getConfiguredKey("r4")))
mensaje4= m.getMessage('recordmenu:existalert')
mensaje5= m.getMessage('recordmenu:existconfirm')
mensaje6= m.getMessage('recordmenu:confirmhelp')
res=("","")
def startWindow( width, height):
    global res
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("RitmSounds: record menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciada pantalla de seleccion")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    
    
    menuitems=[]
    tred = threading.Thread(target=escritor.loadAllTotalItems)
    tred.start()




    #songs = escritor.loadAllSongs()
    songs = loadWindow.startWindow(width,height,escritor.itemsLoaded)
    if(songs==False):

        return(None
)


    #songs = escritor.loadAllTotalItems()


    pygame.display.flip()
    

    
    option=0
    m.sayCustomMessage(mensage,1)
    repeat = mensage

    if len(songs) == 0:
        m.sayMessage("selectwindow:nosongs",1)
        return(None)

    soundevents.loadSong(songs[option].songpath)
    soundevents.musicPlay(-1)
    m.sayCustomMessage(songs[option].name,0)


    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        pygame.display.flip()
        #soundevents.musicSetVolume(0.4*soundevents.musicVolume)


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
                    

                    _selectDif(songs[option])
                    end=True
                    break
                elif pressKey == 'down':
                    
                    

                    soundevents.playMove()
                    option+=1
                    if option>=len(songs):
                        option=0
                    soundevents.loadSong(songs[option].songpath)
                    soundevents.musicPlay(-1)
                    m.sayCustomMessage(songs[option].name,1)


                elif pressKey == 'up':
                    
                    

                    soundevents.playMove()
                    option -= 1 
                    if option<0:
                        option=len(songs)-1
                    soundevents.loadSong(songs[option].songpath)
                    soundevents.musicPlay(-1)
                    m.sayCustomMessage(songs[option].name,1)


                    
                elif(pressKey=='back'):
                    

                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                
                else:
                    if pressKey!='stop':
                        m.sayCustomMessage(repeat)

def _selectDif(song):
    
    pygame.init()
    pygame.display.set_caption("RitmSounds: record menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciada pantalla de seleccion")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    
    if len(song.getAllStepslist()) == 0:
        _configureNewDif(song)
        return()
    pygame.display.flip()
    option=0
    m.sayCustomMessage(mensaje4,1)
    repeat = mensaje4

    m.sayMessage('recordmenu:existmenuitem0',0)
    esconfirm=False
    selectedDif =0


    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        pygame.display.flip()
        #soundevents.musicSetVolume(0.2)


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
                    if esconfirm==False and option!=0:
                        esconfirm=True
                        m.sayCustomMessage(mensaje5)
                        selectedDif=option-1
                        escritor.flog("la dificultad seleccionada es: "+str(selectedDif))
                        repeat=mensaje5
                        option=0
                        escritor.flog("la dificultad seleccionada es: "+str(selectedDif))
                    elif esconfirm == True:
                        if option==1:
                            song.deleteSteplist(selectedDif)
                            _configureNewDif(song)
                            end=True
                            break
                            

                        else:
                            option=0
                            esconfirm=False
                            m.sayCustomMessage(mensaje4)
                            repeat=mensaje4


                    else:
                        _configureNewDif(song)
                        end=True
                        break


                elif pressKey == 'down':
                    
                    

                    soundevents.playMove()
                    option+=1
                    if esconfirm:
                        if option>1:
                            option=0
                        if option==0:
                            m.sayMessage('cancel')
                        else:
                            m.sayMessage('confirm')


                    else:
                        if option >len(song.getAllStepslist()):
                            option=0
                        if option==0:
                            song.resetSteplist()
                            m.sayMessage('recordmenu:existmenuitem0')
                        else:
                            song.selectSteplist(option-1)
                            h = song.getHands()
                            if h ==2:
                                m.sayMessage('selectwindow:difdescription2', 1, song.getSteplistname(), song.getStartHp(), song.getPressSpeed())
                            else:
                                m.sayMessage('selectwindow:difdescription', 1, song.getSteplistname(), song.getStartHp(), song.getPressSpeed())






                elif pressKey == 'up':
                    
                    

                    soundevents.playMove()
                    option -= 1
                    if esconfirm:
                        if option<0:
                            option=1
                        if option==0:
                            m.sayMessage('cancel')
                        else:
                            m.sayMessage('confirm')

                    else:
                        if option < 0:
                            option=len(song.getAllStepslist())
                        if option==0:
                            song.resetSteplist()
                            m.sayMessage('recordmenu:existmenuitem0')
                        else:
                            song.selectSteplist(option-1)
                            h = song.getHands()
                            if h ==2:
                                m.sayMessage('selectwindow:difdescription2', 1, song.getSteplistname(), song.getStartHp(), song.getPressSpeed())
                            else:
                                m.sayMessage('selectwindow:difdescription', 1, song.getSteplistname(), song.getStartHp(), song.getPressSpeed())







                elif(pressKey=='back'):
                    

                    
                    escritor.flog("cierre por escape")
                    end=True
                    startWindow(1024,768)
                    end=True
                    break
                    


                
                else:
                    if pressKey!='stop':
                        m.sayCustomMessage(repeat)


def _configureNewDif(song):
    
    pygame.init()
    pygame.display.set_caption("RitmSounds: record menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciada pantalla de seleccion")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    
    
    menuitems=_buildConfigureDifMenu(song)
    
    pygame.display.flip()
    
    option=0
    m.sayCustomMessage(mensage2,1)
    repeat = mensage2

    m.sayCustomMessage(menuitems[option],0)
    esconfirm=False
    mensage3 = m.getMessage('recordmenu:help3',  pygame.key.name(keyManager.getConfiguredKey("l1")), pygame.key.name(keyManager.getConfiguredKey("l2")), pygame.key.name(keyManager.getConfiguredKey("l3")), pygame.key.name(keyManager.getConfiguredKey("l4")), pygame.key.name(keyManager.getConfiguredKey("r1")), pygame.key.name(keyManager.getConfiguredKey("r2")), pygame.key.name(keyManager.getConfiguredKey("r3")), pygame.key.name(keyManager.getConfiguredKey("r4")))

    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        pygame.display.flip()
        #soundevents.musicSetVolume(0.2)


        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                exit()
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                pressKey = keyManager.getKey(event.key)
                if pressKey== 'accept':
                    if option==len(menuitems)-1 or esconfirm==True:
                        soundevents.playAccept()
                        if esconfirm==False:
                            esconfirm=True
                            m.sayCustomMessage(mensage3,1)
                            repeat=mensage3
                        else:
                            end=True
                            soundevents.playGoSound()
                            #soundevents.musicSetVolume(soundevents.musicVolume/0.5)
                            soundevents.musicFade(1500)
                            time.sleep(1)
                            song.resetSteps()
                            j=recordWindow.startWindow(res[0],res[1],song)
                            if j is not None:
                                _confirmNewDif(j)
                            else:
                                startWindow(res[0],res[1])

                            break

                    else:
                        soundevents.playChange()
                        if option==0:
                            m.sayMessage('recordmenu:setdifname')
                            t= textInput.start()
                            if t is not None:
                                song.setSteplistname(t)
                        elif option ==1:
                            h=song.getHands()
                            if h==1:
                                song.setHands(2)
                            else:
                                song.setHands(1)
                        elif option==2:
                            m.sayMessage('recordmenu:setdifhp')
                            t= textInput.start(True)
                            if t is not None:
                                song.setStartHp(int(t))
                        elif option ==3:
                            m.sayMessage('recordmenu:setdifrestorehp')
                            t=textInput.start(True)
                            if t is not None:
                                song.setRestoreHp(int(t))
                        elif option ==4:
                            m.sayMessage('recordmenu:setdifpressspeed')
                            t=textInput.start(True)
                            if t is not None:
                                song.setPressSpeed(int(t))
                        elif option ==5:
                            m.sayMessage('recordmenu:setdifantisipationtime')
                            t=textInput.start(True)
                            if t is not None:
                                song.setAntisipateTime(int(t))

                        menuitems=_buildConfigureDifMenu(song)

                    
                    
                elif pressKey == 'down':
                    
                    
                    if esconfirm==False:

                        soundevents.playMove()
                        option+=1
                        if option>=len(menuitems):
                            option=0
                        m.sayCustomMessage(menuitems[option],1)
                    else:
                        continue

                elif pressKey == 'up':
                    
                    
                    if esconfirm==False:

                        soundevents.playMove()
                        option -= 1 
                        if option<0:
                            option=len(menuitems)-1
                        m.sayCustomMessage(menuitems[option],1)

                    else:
                        continue

                    
                elif(pressKey=='back'):
                    

                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                    startWindow(res[0],res[1])
                    return()
                
                else:
                    if pressKey!='stop':
                        m.sayCustomMessage(repeat)


def _confirmNewDif(song):
    pygame.init()
    pygame.display.set_caption("RitmSounds: record menu")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciada pantalla de seleccion")
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    
    
    menuitems=[]
    menuitems.append(m.getMessage('test'))
    menuitems.append(m.getMessage('cancel'))
    menuitems.append(m.getMessage('confirm'))
    pygame.display.flip()
    
    option=0
    mens=m.getMessage('recordmenu:confirmhelp', len(song.getAllSteps()))
    m.sayCustomMessage(mens,1)
    repeat = mensage

    
    soundevents.musicLoad("bgm/results.mp3")
    soundevents.musicPlay(True)
    #soundevents.musicSetVolume(0.2)
    m.sayCustomMessage(menuitems[option],0)


    while (not end):
        reloj.tick(60)
        pantalla.fill((134,230,120))
        pygame.display.flip()
        #soundevents.musicSetVolume(0.2)


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
                    if option==0:
                        song.restartSong()
                        playWindow.startWindow(res[0],res[1],song,1)
                        _confirmNewDif(song)
                        end=True
                        break

                    elif option==1:
                        end=True
                        song.resetSteplist()
                        startWindow(res[0],res[1])
                        break
                    else:
                        end=True
                        song.saveSteplist()
                        escritor.saveSong(song)
                        startWindow(res[0],res[1])
                        break





                    
                    break
                elif pressKey == 'down':
                    
                    

                    soundevents.playMove()
                    option+=1
                    if option>=len(menuitems):
                        option=0
                    m.sayCustomMessage(menuitems[option],1)


                elif pressKey == 'up':
                    
                    

                    soundevents.playMove()
                    option -= 1 
                    if option<0:
                        option=len(menuitems)-1
                    m.sayCustomMessage(menuitems[option],1)


                    
                elif(pressKey=='back'):
                    

                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True
                    startWindow(res[0],res[1])

                
                else:
                    if pressKey!='stop':
                        m.sayCustomMessage(repeat)



def _buildConfigureDifMenu(song):
    menu=[]
    menu.append(m.getMessage('recordmenu:difmenu0', song.getSteplistname()))
    menu.append(m.getMessage('recordmenu:difmenu1', song.getHands()))
    menu.append(m.getMessage('recordmenu:difmenu2', song.getStartHp()))
    menu.append(m.getMessage('recordmenu:difmenu3', song.getRestoreHp()))
    menu.append(m.getMessage('recordmenu:difmenu4', song.getPressSpeed()))
    menu.append(m.getMessage('recordmenu:difmenu5', song.getAntisipateTime()))
    menu.append(m.getMessage('recordmenu:difmenudetails', len(song.getAllSteps())))
    menu.append(m.getMessage('recordmenu:difmenuproseed'))
    return(menu)

    
