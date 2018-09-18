#!/usr/bin/python

import os
import eventos
import pygame as PG
from pygame import mixer
import juego
import time
mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
import escritor

musicLoad = mixer.music.load
_musicPlay = mixer.music.play
musicStop = mixer.music.stop
musicPause = mixer.music.pause
musicUnpause = mixer.music.unpause
musicFade = mixer.music.fadeout
_musicSetVolume = mixer.music.set_volume
musicVolume=0.4
_musicVolume = mixer.music.get_volume
musicIsPlay = mixer.music.get_busy
musicSetPos = mixer.music.set_pos
musicPos = mixer.music.get_pos
sfxVolume = 0.6

def loadSong(s):
    escritor.flog("cargando cancion en: " + os.path.join(escritor.logdir,s))
    musicLoad(os.path.join(escritor.logdir,s))

def musicPlay(loop=False):
    _musicPlay(loop)
    _musicSetVolume(musicVolume)


def setSfxVolume(newvalue):
    global sfxVolume
    sfxVolume+=newvalue
    if sfxVolume <0.1:
        sfxVolume =0.1
    elif sfxVolume >1:
        sfxVolume =1

    
    escritor.flog("sfx volume changed: %s " % str(sfxVolume))


def applyVolumeMusicFactor(factor):
    global musicVolume
    if musicVolume*factor < 0.1:
        _musicSetVolume(0.1)
    else:
        _musicSetVolume(musicVolume*factor)


    
    

def unapplyVolumeMusicFactor(factor):
    global musicVolume
    
    _musicSetVolume(musicVolume)


def musicSetVolume(newvalue):
    global musicVolume
    musicVolume+=newvalue
    if musicVolume<0.2:
       musicVolume =0.2
    elif musicVolume >1:
        musicVolume =1



    _musicSetVolume(float(musicVolume))
    
    escritor.flog("music volume changed: %s " % str(musicVolume))
    

mixer.set_num_channels(16)
twoHands = 1
survivorJump = False
__hitsounds = {'l1': mixer.Sound("sfx/hit0.wav.ogg"), 'l2': mixer.Sound("sfx/hit1.wav.ogg"), 'l3': mixer.Sound("sfx/hit2.wav"), 'l4': mixer.Sound("sfx/hit3.wav"),'r1': mixer.Sound("sfx/hit0.wav.ogg"), 'r2': mixer.Sound("sfx/hit1.wav.ogg"), 'r3': mixer.Sound("sfx/hit2.wav"), 'r4': mixer.Sound("sfx/hit3.wav")}
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
__survivorStart = mixer.Sound("sfx/survivorstart.ogg")
__point = mixer.Sound("sfx/point.ogg")
__lastPoint = mixer.Sound("sfx/lastPoint.ogg")
__startPoints = mixer.Sound("sfx/startPoints.ogg")

def _loopPlay(sound, times=1, repeatTime=1):
    escritor.flog("Iniciado loop de sonido con %i veces y %i intervalo" % (times,repeatTime))
    if(times<0):
        times=1

    
    
    repeated = 0
    sound.play()
    sound.set_volume(sfxVolume)
    
    

    
    tickCount = 1
    reloj = PG.time.Clock()
    
    while(repeated!= times):
        reloj.tick_busy_loop(60)
        tickCount+=1

        if((tickCount%repeatTime)==0):
            repeated+=1
            if(repeated!=times):
                sound.play()
                sound.set_volume(sfxVolume)

def playSurvivorStart():
    __survivorStart.play()
    __survivorStart.set_volume(sfxVolume)
   
def playDamage():
    __damageSound.play()
    __damageSound.set_volume(sfxVolume)

def playRestoreHP():
    __restoreHP.play()
    __restoreHP.set_volume(sfxVolume)

def playLowHp():
    __lowHpSound.play()
    __lowHpSound.set_volume(sfxVolume)

def playError():
    __errorSound.play()
    __errorSound.set_volume(sfxVolume)

def __playHit(hitNum):
    if hitNum in __hitsounds:
        if twoHands==2:

            c=__hitsounds[hitNum].play()
            
            if hitNum.startswith("l"):
                c.set_volume(sfxVolume,0.1)
            else:
                c.set_volume(0.1,sfxVolume)


        else:
            
            __hitsounds[hitNum].play()
            __hitsounds[hitNum].set_volume(sfxVolume)



def playMove():
    __beepSound.play()
    __beepSound.set_volume(sfxVolume)

def playChange():
    __moveSound.play()
    __moveSound.set_volume(sfxVolume)


def playAccept():
    __acceptsound.play()
    __acceptsound.set_volume(sfxVolume)

def playback():
    __backSound.play()
    __backSound.set_volume(sfxVolume)

def playGoSound():
    __startsound.play()
    __startsound.set_volume(sfxVolume)


def __playStartSound():
    if survivorJump==True:
        return()

    _loopPlay(__beepSound, 2, 40)
    _loopPlay(__startsound,1,45)
    

    


def playResults(points):
        _loopPlay(__startPoints, 1, 20)
        _loopPlay(__point,points,7)
        _loopPlay(__lastPoint,1,40)


def playdeath():
    musicStop()
    _loopPlay(__deathSound,1,400)


juego.hitEvent+=__playHit
juego.startEvent+=__playStartSound
juego.deatEvent+=playdeath