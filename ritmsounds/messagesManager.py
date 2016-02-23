#!/usr/bin/python
# -*- coding: latin-1 -*-
import speechManager as sp
import jsonpickle
import escritor
_defaultMessages = {
    'menuwindow:title': 'Bienvenido a ritmsounds! Presione enter.',
    'menuwindow:help': 'Menú principal. Utilice las flechas para moverse en el menú, y luego presione enter para seleccionar',
    'menuwindow:option0': 'jugar una canción',
    'menuwindow:option1': 'practicar una canción',
    'menuwindow:option2': 'aprender los sonidos de las teclas',
    'menuwindow:option3': '¡Supervivencia! ¡Baila hasta morir!',
    'menuwindow:option4': 'grabar las teclas de una canción',
    'menuwindow:optionexit': 'salir del juego',
    'selectwindow:help': 'Seleccione canción a jugar. utilice las flechas para seleccionar la canción que desea jugar, y luego precione enter para empezar',
    'selectwindow:help2': 'Selección de dificultad. Seleccione seleccione qué dificultad de esta canción desea jugar. luego precione enter',
    'selectwindow:help3': 'Recuerde: para jugar utilice las teclas %0, %1, %2 y  %3 en la mano izquierda, y %4, %5, %6 y %7, en la mano derecha, si es que está jugando una canción a dos manos. ¡buena suerte! Presione enter para proceder.',
    'selectwindow:nosongs': "lo sentimos, no posee ninguna canción con ritmos creada en la carpeta songs",
    'selectwindow:difdescription': '%0, a una  mano, vida inicial: %1, tiempo de reacción: %2',
    'selectwindow:difdescription2': '%0, a dos manos, vida inicial: %1, tiempo de reacción: %2',
    'resultswindow:congratulations': '¡felicitaciones! ¡has completado la canción! Optuviste un total de %0 puntos, con un total de %1 fallos. Has optenido una calificación de: %2',
    'resultswindow:death': '¡has perdido estrepitosamente! A penas optuviste un total de %0 puntos',
    'testwindow:help': 'Pantalla de prueba de sonidos. para conocer los sonidos que equivalen a cada una de las teclas, utilize %0, %1, %2 y  %3 en la mano izquierda, y %4, %5, %6 y %7, en la mano derecha. Para regresar al menú, presione %8.',
    'recordwindow:help': 'Presione las teclas al ritmo de la canción para ir grabándolas. Presione %0 para cancelar',
    'text:help': 'escriba el texto. para finalizar, presione enter, o escape para cancelar',
    'text:empty': 'El mensage que puso está vacío. por favor escriba algo primero antes de aceptar',
    'text:delete': '%0, borrado',
    'recordmenu:help': 'Seleccione la canción a la cual desea crearle un nuevo conjunto de pasos.',
    'recordmenu:help2': 'Complete las configuraciones de su nueva dificultad. Navegue con las flechas, y active las opciones con enter. Para finalizar, presione proceder.',
    'recordmenu:help3': 'Recuerde: para grabar utilice las teclas %0, %1, %2 y  %3 en la mano izquierda, y %4, %5, %6 y %7, en la mano derecha, si es que está grabando  una canción a dos manos. ¡vamos! Presione enter para proceder.',
    'recordmenu:existalert': 'La canción seleccionada ya posee un conjunto dificultades. Seleccione la que desea modificar, o presione nueva dificultad.',
    'recordmenu:existmenuitem0': 'crear nueva dificultad.',
    'recordmenu:existconfirm': '¿Está seguro que desea  sobreescribir esa dificultad?',
    'recordmenu:difmenu0': 'nombre de la dificultad: %0.',
    'recordmenu:difmenu1': 'manos: %0.',
    'recordmenu:difmenu2': 'HP inicial: %0.',
    'recordmenu:difmenu3': 'hits necesarios para recuperar vida: %0',
    'recordmenu:difmenu4': 'Velocidad de presionado: %0',
    'recordmenu:difmenu5': 'velocidad de antisipación: %0',
    'recordmenu:difmenuproseed': 'proseder con la grabación',
    'recordmenu:setdifname': 'Escriba el nombre de la dificultad y luego presione enter.',
    'recordmenu:setdifhp': 'Escriba la cantidad de hp inicial para esta dificultad.',
    'recordmenu:setdifrestorehp': 'Escriba cuantos hits correctos se necesitan para recuperar un punto de hp en esta dificultad.',
    'recordmenu:setdifpressspeed': 'Escriba la el tiempo de demora admitido para aceptar un punto.',
    'recordmenu:setdifantisipationtime': 'Escriba cuanto tiempo se puede antisipar un punto',
    'recordmenu:difmenudetails': 'La Dificultad contiene %0 pasos',
    'recordmenu:confirmhelp': 'Grabación completada. Se han grabado un total de %0 pasos. Desea guardar los pasos recién creados?',
    'confirm': 'Sí',
    'cancel': 'No',
    'test': 'provar pasos',
    'survivormenu:help': '¡bienvenido al modo supervivencia! Ajusta las opciones y luego presiona en proceder. Para desplasarte usa las flechas, y para ajustar valores presiona enter. ¿cuánto aguantarás? ',
    'survivormenu:option0': 'Cantidad máxima de vida (máximo 100): %0',
    'survivormenu:option1': '¿Colocar pausa e información entre canciones? %0',
    'survivormenu:option2': '¿Recuperar el total del máximo de vida entre cada canción? %0',
    'survivormenu:option3': '¿Permitir recuperar vida durante las canciones al ejecutar la cantidad de pasos correctos pre configurado en la dificultad de la canción? %0',
    'survivormenu:optionconfirm': '¡Vive! Si puedes',
    'survivormenu:errorzero': '¡La vida máxima no puede valer menos de cero ni más de 100!',
    'survivorpausewindow:message0': '¡felicidades! canción pasada! Tu vida restante es %0. Presiona enter para continuar. ',
    'survivorpausewindow:message1': '¡felicidades! canción pasada! Tu vida ha sido restaorada a %0. Presiona enter para continuar.',
    'survivorpausewindow:message2': 'La siguiente canción es %0 en dificultad %1. Presiona enter para iniciar. ¡buena suerte!',
    'survivorresultswindow:message0': '¡Vaya! ¡Parece que no pudiste sobrevivir más! Es una lástima. Lograste completar %0 canciones, opteniendo una colección total de %1 puntos entre todas ellas.',





    





}
_currentMessages = _defaultMessages


def getMessage(keyString="", *args):
    if keyString in _currentMessages.keys():
        return(_replaseArgs(_currentMessages[keyString],args))
    else:
        return("Missing message")





def sayMessage(keyString, interrupt=1, *args):
    mes = _replaseArgs(getMessage(keyString),args)
    sp.say(mes,interrupt)

def sayCustomMessage(message, interrupt = 1):
    sp.say(message,interrupt)

    
def loadLanguage(languageCode):
    pass

def saveLanguage(languageCode):
    pass


def _replaseArgs(mes, arreglo):
    #escritor.flog("reemplasando los siguientes argumentos : " + str(args) + " en el mensage " + mes)

    for a in range(0,len(arreglo)):
        mes= mes.replace("%"+str(a),str(arreglo[a]))
        escritor.flog("el mensage queda que va es: " + mes)

    return(mes)




