#!/usr/bin/python
# -*- coding: latin-1 -*-
import eventos
from pygame.locals import *
import escritor
import jsonpickle
import soundevents

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
    'r1': K_LEFT,
    'r2': K_UP,
    'r3': K_DOWN,
    'r4': K_RIGHT
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
    for k in keys.items():
        if k[1] == key:
            return(k[0])
    return('null')





def setKey(key, value):
    if key in keys:
        keys[key] = value
