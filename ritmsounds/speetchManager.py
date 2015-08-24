#!/usr/bin/python
# -*- coding: latin-1 -*-
import ctypes


srapi = ctypes.windll.98ScreenReaderAPI
sp = ctypes.windll.UniversalSpeech
speech = ctypes.windll.LoadLibrary("UniversalSpeech.dll")


def say(text):
    speech.speechSay(text,1)

def stop():
    speech.speechStop()


