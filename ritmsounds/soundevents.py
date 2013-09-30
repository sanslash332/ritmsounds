#!/usr/bin/python
# -*- coding: latin-1 -*-
import eventos
from pygame import mixer
import juego
import time
mixer.init(frequency=22050, size=-16, channels=2, buffer=128)

__hitsounds = [mixer.Sound("sfx/hit0.wav"), mixer.Sound("sfx/hit1.wav"), mixer.Sound("sfx/hit2.wav"), mixer.Sound("sfx/hit3.wav")]
__startsound = mixer.Sound("sfx/start.wav")
__beepSound = mixer.Sound("sfx/beep.wav")
def __playHit(hitNum):
    __hitsounds[hitNum].play()


def __playStartSound():
    __beepSound.play()
    time.sleep(1)
    __beepSound.play()
    time.sleep(1)

    __startsound.play()
    time.sleep(1)

    


juego.hitEvent+=__playHit
juego.startEvent+=__playStartSound