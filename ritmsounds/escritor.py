#!/usr/bin/python
# -*- coding: latin-1 -*-
import os.path
import datetime
import eventos

archlog = open("log.log", 'a')
flog = eventos.Event()
flog+=escribirLog
def escribirSteps(nombre, steps):
    """Método para escribir en un archivo rtms los pasos y ticks correspondientes de una cancion"""
    if (os.path.isfile(nombre+".rtms") == true):
        nombre += "new"
        escribirSteps(nombre,steps)
        return


    archivo = open(nombre + ".rtms", 'w')
    for s in steps:
        archivo.write(s[0] + "|" + s[1] + "\n")
    archivo.flush()
    archivo.close()

def escribirLog(datos):
    archlog.write(datetime.date.today() + ":" + datos)
    archlog.flush()