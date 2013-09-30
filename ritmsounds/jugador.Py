#!/usr/bin/python
# -*- coding: latin-1 -*-
class Jugador(object):
    """Clase que representa a un jugador"""
    def __init__(self,nombre="player"):
        object.__init__(self)
        self.__puntos =0
        self.__miss = 0
        self.__nombre=nombre

    def sumarPuntos(self,puntos):
        self.__puntos+=puntos

    def sumarMiss(self,miss):
        self.__miss+=miss

    def __str__(self):
        return self.__nombre + ": puntos = " + str(self.__puntos) + ", fallas = " + str(self.__miss)
