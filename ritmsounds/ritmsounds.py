import pygame as pg


mus = pg.mixer

mus.init()

sfx = mus.Sound("start.wav")


sfx.play()


a = raw_input()

while a != 'x':
    sfx.play()
    a= raw_input()
