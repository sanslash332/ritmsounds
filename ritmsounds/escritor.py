#!/usr/bin/python
# -*- coding: latin-1 -*-
import os.path
import os
import datetime
import eventos
import jsonpickle
import song
import sys

flog = eventos.Event()

itemsLoaded = eventos.Event()
logoff=False
songsdir=""
logdir=""

def saveSong(song):
    """Método para escribir en un archivo rtms los pasos y ticks correspondientes de una cancion"""
    nombre = song.songpath

    if (os.path.isfile(os.path.join(logdir, song.songpath+".rtms")) == True):
        try:
            os.remove(os.path.join(logdir,song.songpath+".rtms"))
        except Exception:
            flog("no se pudo borrar el archivo antiguo, generando uno nuevo ")
            nombre = nombre+"new"

    archivo = open(os.path.join(logdir, nombre + ".rtms"), 'w')
    archivo.write(song.genJson())

    
    archivo.flush()
    archivo.close()


def escribirLog(datos):
    if logoff==False:

        archlog = open(os.path.join(logdir,"ritmsounds.log"), 'a')
        archlog.write(str(datetime.datetime.now()) +  ":" + datos + "\n")
        archlog.flush()
        archlog.close()

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
        flog("problemas al leer archivo ")
        flog(str(err))
        flog(err.__traceback__)
        return(None)
        
        


    escribirLog("cargada canción " + song.name )
    return song


def loadAllSongs():
    dir=songsdir
    escribirLog("cargando archivos desde: " + dir)

    
    songs=[]
    s=""

    if os.path.exists(dir)==False:
        escribirLog("No existe la carpeta.")
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
        escribirLog("no existe la carpeta")
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
