#!/usr/bin/python
# -*- coding: latin-1 -*-
import eventos
from pygame import mixer
import juego

mixer.init()
__hitsounds = [mixer.Sound("sfx\\hit0.wav"), mixer.Sound("sfx\\hit1.wav"), mixer.Sound("sfx\\hit2.wav"), mixer.Sound("sfx\\hit3.wav")]
__startsound = mixer.Sound("sfx\\start.wav")

def __playHit(hitNum):
    __hitsounds[hitNum].play()


def __playStartSound():
    __startsound.play()
    


juego.hitEvent+=__playHit
juego.startEvent+=__playStartSound