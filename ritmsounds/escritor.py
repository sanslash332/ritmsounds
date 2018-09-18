#!/usr/bin/python

import os.path
import os
import datetime
import eventos
import jsonpickle
import song
import sys
import logging

flog = eventos.Event()
itemsLoaded = eventos.Event()
logoff=False
songsdir=""
logdir=""


def initLog():
    global _log
    logging.basicConfig(
        filename=os.path.join(logdir,"ritmsounds.log"),
        format="%(asctime)s (%(threadName)-12.12s, %(levelname)-5.5s) %(message)s",
        level=logging.WARNING
    )

    _log=logging.getLogger()

def getlog():
    return _log

def saveSong(song):
    """Método para escribir en un archivo rtms los pasos y ticks correspondientes de una cancion"""
    nombre = song.songpath

    if (os.path.isfile(os.path.join(logdir, song.songpath+".rtms")) == True):
        try:
            os.remove(os.path.join(logdir,song.songpath+".rtms"))
        except Exception:
            _log.warning("no se pudo borrar el archivo antiguo, generando uno nuevo ")
            nombre = nombre+"new"

    archivo = open(os.path.join(logdir, nombre + ".rtms"), 'w')
    archivo.write(song.genJson())

    
    archivo.flush()
    archivo.close()


def escribirLog(datos):
    _log.debug(datos)
    
flog+=escribirLog

def loadSong(cancion):
    flog("cargando cancion " +cancion)
    song=None
    try:

        arch = open(cancion + ".rtms")
        data = ""
        data = arch.read()
        song = jsonpickle.decode(data)
    except Exception as err:
        _log.warning("problemas al leer archivo ")
        _log.warning(str(err))
        _log.warning(err.__traceback__)
        return(None)
        
    escribirLog("cargada canción " + song.name )
    return song


def loadAllSongs():
    dir=songsdir
    escribirLog("cargando archivos desde: " + dir)

    
    songs=[]
    s=""

    if os.path.exists(dir)==False:
        _log.error("No existe la carpeta.")
        itemsLoaded("nosongs")
        return("nosongs")

    for s in os.listdir(dir):
        escribirLog("analizando archivo" + str(s))
        if s.endswith(".rtms"):
            sd = s[:s.index(".rtms")]
            songs.append(loadSong(os.path.join(dir,sd)))


    if len(songs) < 1:
        songs="nosongs"

    itemsLoaded(songs)
    return(songs)





def loadAllTotalItems():
    dir=songsdir
    songs=[]
    s=""
    escribirLog("cargando archivos desde: " + dir)
    if os.path.exists(dir)==False:
        _log.error("no existe la carpeta")
        itemsLoaded("nosongs")
        return("nosongs")


    for s in os.listdir(dir):
        escribirLog("analizando archivo" + str(s))
        if s.endswith(".rtms"):
            sd = s[:s.index(".rtms")]
            songs.append(loadSong(os.path.join(dir,sd)))

    for s in os.listdir(dir):
        if s.endswith(".ogg"):
            sd = s[:s.index(".ogg")]
            js= song.Song(sd,os.path.join("songs",s))
            ent=True
            for ss in songs:
                flog("comparando " + js.name + " con " + ss.name)
                if js.name==ss.name:
                    ent=False

            if ent:

                songs.append(js)


            
        
        if len(songs) <1:
            songs="nosongs"

    itemsLoaded(songs)
    return(songs)
