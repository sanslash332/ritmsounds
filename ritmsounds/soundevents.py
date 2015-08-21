#!/usr/bin/python
# -*- coding: latin-1 -*-
import eventos
from pygame import mixer
import juego
import time
mixer.init(frequency=22050, size=-16, channels=2, buffer=128)


musicLoad = mixer.music.load
musicPlay = mixer.music.play
musicStop = mixer.music.stop
musicPause = mixer.music.pause
musicUnpause = mixer.music.unpause
musicFade = mixer.music.fadeout
musicSetVolume = mixer.music.set_volume
musivVolume = mixer.music.get_volume
musicIsPlay = mixer.music.get_busy
musicSetPos = mixer.music.set_pos
musicPos = mixer.music.get_pos

twoHands= False
__hitsounds = {'l1': mixer.Sound("sfx/hit0.wav"), 'l2': mixer.Sound("sfx/hit1.wav"), 'l3': mixer.Sound("sfx/hit2.wav"), 'l4': mixer.Sound("sfx/hit3.wav"),'r1': mixer.Sound("sfx/hit0.wav"), 'r2': mixer.Sound("sfx/hit1.wav"), 'r3': mixer.Sound("sfx/hit2.wav"), 'r4': mixer.Sound("sfx/hit3.wav")}
__startsound = mixer.Sound("sfx/start.wav")
__beepSound = mixer.Sound("sfx/beep.wav")
__errorSound = mixer.Sound("sfx/error.wav")

__acceptsound = mixer.Sound("sfx/accept.wav")
__moveSound = mixer.Sound("sfx/beep.wav")
__backSound = mixer.Sound("sfx/back.wav")
__deathSound = mixer.Sound("sfx/death.wav")

def playError():
    __errorSound.play()

def __playHit(hitNum):
    if hitNum in __hitsounds:

        __hitsounds[hitNum].play()


def playMove():
    __moveSound.play()

def playAccept():
    __acceptsound.play()

def playback():
    __backSound.play()

def __playStartSound():
    __beepSound.play()
    
    time.sleep(1)
    __beepSound.play()
    time.sleep(1)

    __startsound.play()
    time.sleep(1)

    


def playdeath():
    __deathSound.play()


juego.hitEvent+=__playHit
juego.startEvent+=__playStartSound
juego.deatEvent+=playdeath