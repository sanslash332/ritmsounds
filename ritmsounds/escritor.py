#!/usr/bin/python
# -*- coding: latin-1 -*-
import os.path
import datetime
import eventos


flog = eventos.Event()

def escribirSteps(nombre, steps):
    """Método para escribir en un archivo rtms los pasos y ticks correspondientes de una cancion"""
    if (os.path.isfile(nombre+".rtms") == True):
        nombre += "new"
        escribirSteps(nombre,steps)
        return


    archivo = open(nombre + ".rtms", 'w')
    for s in steps:
        archivo.write(str(s[0]) + "|" + str(s[1]) + "\n")
    archivo.flush()
    archivo.close()

def escribirLog(datos):
    archlog = open("log.log", 'a')
    archlog.write(str(datetime.datetime.now()) +  ":" + datos + "\n")
    archlog.flush()
    archlog.close()

flog+=escribirLog

def cargarSteps(cancion):
    arch = open(cancion + ".rtms")
    steps = []
    for line in arch:
        partidos = line.split('|')
        if len(partidos) == 2:
            steps.append((int(partidos[0]),int(partidos[1])))

    escribirLog("cargada canción con " + str(len(steps)) + " pasos")
    return steps

