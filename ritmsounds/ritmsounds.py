#!/usr/bin/python
# -*- coding: latin-1 -*-

import pygame as pg
import song
import eventos
from pygame.locals import *
mus = pg.mixer

mus.init()
print("iniciando test")

sfx = mus.Sound("sfx\\start.wav")

bgm = song.Song("songs\\fire.mp3")


sfx.play()


bgm.play()
print("reproducción iniciada")

a = raw_input()

while a != 'x':
    sfx.play()
    a= raw_input()
