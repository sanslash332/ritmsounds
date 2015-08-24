#!/usr/bin/python
# -*- coding: latin-1 -*-
import os.path
import os
import datetime
import eventos
import jsonpickle

flog = eventos.Event()

def saveSong(song):
    """Método para escribir en un archivo rtms los pasos y ticks correspondientes de una cancion"""
    nombre = song.songpath

    if (os.path.isfile(song.songpath+".rtms") == True):
        try:
            os.remove(song.songpath+".rtms")
        except Exception:
            nombre = nombre+"new"



        


    archivo = open(nombre + ".rtms", 'w')
    archivo.write(song.genJson())

    
    archivo.flush()
    archivo.close()


def escribirLog(datos):
    archlog = open("log.log", 'a')
    archlog.write(str(datetime.datetime.now()) +  ":" + datos + "\n")
    archlog.flush()
    archlog.close()

flog+=escribirLog

def loadSong(cancion):
    arch = open(cancion + ".rtms")
    data = ""
    data = arch.read()
    song = jsonpickle.decode(data)


    escribirLog("cargada canción " + song.name )
    return song


def loadAllSongs():
    
    songs=[]
    s=""
    for s in os.listdir("songs/"):
        if s.endswith(".rtms"):
            sd = s[:s.index(".rtms")]
            songs.append(loadSong("songs/"+sd))
    return(songs)




