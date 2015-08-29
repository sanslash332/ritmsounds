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

mixer.set_num_channels(16)
twoHands = 1
__hitsounds = {'l1': mixer.Sound("sfx/hit0.wav"), 'l2': mixer.Sound("sfx/hit1.wav"), 'l3': mixer.Sound("sfx/hit2.wav"), 'l4': mixer.Sound("sfx/hit3.wav"),'r1': mixer.Sound("sfx/hit0.wav"), 'r2': mixer.Sound("sfx/hit1.wav"), 'r3': mixer.Sound("sfx/hit2.wav"), 'r4': mixer.Sound("sfx/hit3.wav")}
__startsound = mixer.Sound("sfx/start.wav")
__beepSound = mixer.Sound("sfx/beep.wav")
__errorSound = mixer.Sound("sfx/error.wav")

__acceptsound = mixer.Sound("sfx/accept.wav")
__moveSound = mixer.Sound("sfx/change.wav")
__backSound = mixer.Sound("sfx/back.wav")
__deathSound = mixer.Sound("sfx/death.wav")
__lowHpSound = mixer.Sound("sfx/lowhp.wav")
__damageSound = mixer.Sound("sfx/damage.wav")
__restoreHP = mixer.Sound("sfx/restorehp.wav")

def playDamage():
    __damageSound.play()

def playRestoreHP():
    __restoreHP.play()

def playLowHp():
    __lowHpSound.play()

def playError():
    __errorSound.play()

def __playHit(hitNum):
    if hitNum in __hitsounds:
        if twoHands==2:

            c=__hitsounds[hitNum].play()
            
            if hitNum.startswith("l"):
                c.set_volume(1.0,0.1)
            else:
                c.set_volume(0.1,1.0)


        else:
            
            __hitsounds[hitNum].play()



def playMove():
    __beepSound.play()

def playChange():
    __moveSound.play()


def playAccept():
    __acceptsound.play()

def playback():
    __backSound.play()

def playGoSound():
    __startsound.play()


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