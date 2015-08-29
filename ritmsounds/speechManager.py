#!/usr/bin/python
# -*- coding: latin-1 -*-
import ctypes



speech = ctypes.cdll.UniversalSpeech



def say(text, interrupt):
    speech.speechSay(text,interrupt)
    

def stop():
    speech.speechStop()


