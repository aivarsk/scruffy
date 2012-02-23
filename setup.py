#!/usr/bin/env python
import sys
from distutils.core import setup

def which(program):
    import os
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ['PATH'].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

if which('dot') is None:
    sys.exit('You need dot [graphviz] binary for this software to work')
if which('rsvg-convert') is None:
    sys.exit('You need rsvg-convert [librsvg2-bin] binary for this software to work')
if which('pic2plot') is None:
    sys.exit('You need pic2plot [plotutils] binary for this software to work')

setup(name='scruffy',
        version='0.1',
        description='Scruffy UML: Creates UML diagrams using yUML-like syntax',
        author='Aivars Kalvans',
        author_email='aivars.kalvans@gmail.com',
        url='https://github.com/aivarsk/scruffy',
        packages=['suml'],
        package_data={'suml': ['sequence.pic']},
        scripts=['bin/suml']
        )
