#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame as pg
import juego
import song
import eventos
import escritor
from pygame.locals import *
import soundevents
import testkeysWindow
import recordWindow
import playWindow
import os


screen_width = 640
screen_height =480
songs_dir = "songs/"

def desplegarResultados(acertados, fallados):
    print("lograste acertar " + str(acertados) + ", y fallaste " + str(fallados) + " steps. \n ¡felicidades")


def menu():
    option = ""
    print ("bienvenido a la primera verción de ritmsounds! \n Veamos si eres capaz de seguir el ritmo sólo oyendo las indicaciones")
    juego.resultsEvent+=desplegarResultados

    while (option != "0"):
        print ("menú principal: ¿qué deseas hacer? \n escribe 0 para salir \n escribe 1 para probar las teclas y conocer los sonidos asociados \n 2 para jugar una canción \n 3 para grabar tu propia secuencia de pasos para una canción")
        option = input()
        if option == "1":
            testkeysWindow.startWindow(screen_width, screen_height)
        elif option == "2":
            print("ingrese el nombre de la canción a la cual desea jugar, incluya la extención \n recuerde que la canción para ser jugable tiene que tener un archivo rtms creado previamente!")
            cancion = input()
            if os.path.isfile(songs_dir + cancion) == False or os.path.isfile(songs_dir+cancion+".rtms") == False:
                print("no existe esa cancion \n o no posee un archivo rtms creado.")
            else:
                print("preciona enter para iniciar a jugar \n ¡danse danse!")
                input()
                j = escritor.loadSong(songs_dir+cancion)
                j.selectSteplist(0)
                playWindow.startWindow(screen_width,screen_height,j)


        elif option == "3":
            print("ingrese el nombre completo de la canción a la cual crearle los pasos. \n recuerde que la canción debe de estar en la carpeta songs/  y tiene que escribir el nombre incluyendo la extención")
            cancion = input()
            if os.path.isfile(songs_dir + cancion) == False:
                print("no existe esa cancion")
            else:
                print("preciona enter para iniciar la grabación")
                input()

                j = song.Song(cancion,songs_dir+cancion)
                recordWindow.startWindow(screen_width,screen_height,j)


                






if(__name__ == "__main__"):
    menu()