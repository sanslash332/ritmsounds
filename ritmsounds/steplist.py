#!/usr/bin/python
# -*- coding: latin-1 -*-

class steplist(object):
    """Clase que representa una colección de pasos para una canción """
    def __init__(self, name=None, steps = None, hands=1, pressSpeed = 20):
        super().__init__()
        self.hands=hands
        self.name= name
        self.pressSpeed = pressSpeed
        self.steps = list()
        if(steps is None==False):
            self.steps = steps



