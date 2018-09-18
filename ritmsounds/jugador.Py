#!/usr/bin/python

class Jugador(object):
    """Clase que representa a un jugador"""
    def __init__(self,nombre="player"):
        object.__init__(self)
        self.__puntos =0
        self.__miss = 0
        self.__nombre=nombre
        self.__hp=100 

    def sumarPuntos(self,puntos):
        self.__puntos+=puntos

    def sumarMiss(self,miss):
        self.__miss+=miss
    def setHP(self, hp):
        self.__hp=hp

    def getHP(self):
        return(self.__hp)

    def __str__(self):
        return self.__nombre + ": puntos = " + str(self.__puntos) + ", fallas = " + str(self.__miss)

    def getNombre(self):
        return(self.__nombre)

    def getPuntos(self):
        return(self.__puntos)

    def getMiss(self):
        return(self.__miss)
    def resetPoints(self):
        self.__puntos=0
        self.__miss=0



