#!/usr/bin/python
# -*- coding: latin-1 -*-
import eventos
from pygame.locals import *
import escritor
import jsonpickle
import soundevents
import speechManager

keys = {
    'left': K_LEFT,
    'right': K_RIGHT,
    'up': K_UP,
    'down': K_DOWN,
    'accept': K_RETURN,
    'back': K_ESCAPE,
    'l1': K_a,
    'l2': K_s,
    'l3': K_z,
    'l4': K_x,
    'r1': K_u,
    'r2': K_i,
    'r3': K_j,
    'r4': K_k
    }



def setKeys(newKeys):
    if keys.keys() == newKeys.keys():

        keys = newKeys

def saveKeys():
    j = jsonpickle.encode(keys)
    try:
        f=open('keys.ini', 'w')
        f.write(j)
        f.flush()
        f.close()
    except Exception:
        soundevents.playError()

def loadKeys():
    f = open('keys.ini', 'r')
    data = ""
    
    data=f.read()
    j = jsonpickle.decode(data)
    setKeys(j)



def getKey(key):
    if key==K_LCTRL or key==K_RCTRL:
        speechManager.stop()
        return("stop")


    for k in keys.items():
        if k[1] == key:
            escritor.flog("se detecto un:  "+k[0])
            return(k[0])
    return('null')



def getConfiguredKey(key):
    if key in keys.keys():
        return(keys[key])




def setKey(key, value):
    if key in keys:
        keys[key] = value
