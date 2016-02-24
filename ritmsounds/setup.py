#!/usr/bin/python
# -*- coding: latin-1 -*-
from distutils.core import setup
import glob
import os
import os.path
import easy_install
import py2exe
import sys
import json
import simplejson


PYGAME_DIR = os.path.join(os.path.split(sys.executable)[0], "Lib\site-packages\pygame")

JSONPICKLE_DIR = os.path.join(os.path.split(sys.executable)[0], "Lib\site-packages\jsonpickle")


def data_files_from_tree(source_dir): # the installation directory must have the same name
    data_files = []
    for root, dirs, files in os.walk(source_dir):
        if ".svn" not in root:
            source_list = []
            for filename in files:
                source_list.append(os.path.join(root, filename))
            data_files.append((root, source_list))
    return data_files


setup(windows=["ritmsounds.py"],
      console=["ritmsoundsC.py"],
      data_files=[("", glob.glob(r"%s\*.dll" % PYGAME_DIR)+glob.glob(r"%s\*.ttf"%PYGAME_DIR)
                   #[r"%s\freesansbold.ttf" % PYGAME_DIR,
                        #r"%s\SDL.dll" % PYGAME_DIR,
                        #r"%s\SDL_ttf.dll" % PYGAME_DIR,
                        #r"%s\libfreetype-6.dll" % PYGAME_DIR,
                        #r"%s\libogg-0.dll" % PYGAME_DIR,
                        #r"%s\zlib1.dll" % PYGAME_DIR,
                        #]
##                   + glob.glob(r"%s/*.dll" % PYGAME_DIR)
                   ),
                  ("", glob.glob(r"*.dll")),
                  ("sfx", glob.glob(r"sfx\*.*")),
                  ("bgm", glob.glob(r"bgm\*.*")),
                  ("songs", glob.glob(r"songs\*.*")),
                  ],
      options = {'py2exe': {
      'bundle_files': 1,
      #'excludes': ['tkinter', '_tkinter', 'Tkinter', ], 
      'dll_excludes': ['libiomp5md.dll',],
      'includes': ['simplejson',],
} },
##      zipfile = None,
      )
