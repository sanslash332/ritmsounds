#!/usr/bin/python
# -*- coding: latin-1 -*-

class steplist(object):
    """Clase que representa una colección de pasos para una canción """
    def __init__(self, name="dificultad", steps = None, hands=1, pressSpeed = 20, antisipateTime = 10, description = "", startHP = 10, restoreHp = 10):
        super().__init__()
        self.hands=hands
        self.name= name
        self.pressSpeed = pressSpeed
        self.antisipateTime = antisipateTime
        self.description = description
        self.startHp = startHP
        self.restoreHp = restoreHp

        self.steps = list()
        if(steps is None==False):
            self.steps = steps



