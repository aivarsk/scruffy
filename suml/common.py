# Copyright (C) 2011 by Aivars Kalvans <aivars.kalvans@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import subprocess
from PIL import Image, ImageChops
from operator import attrgetter

def hasFont(fname):
    stdout = subprocess.Popen(['fc-list', fname], shell=True, stdout=subprocess.PIPE).stdout
    return len(stdout.readlines()) > 0

def defaultScruffyFont():
    for fname in ('Purisa',):
        if hasFont(fname):
            return fname

    return None

class Box:
    n = 0
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec
        self.uid = 'A%03d' % Box.n
        Box.n += 1

    def update(self, spec):
        if len(self.spec) < len(spec):
            self.spec = spec
        return self

_boxes = {}
def getBox(spec):
    name = spec.split('|')[0].strip()
    if name not in _boxes:
        _boxes[name] = Box(name, spec)
    return _boxes[name].update(spec)

def getBoxes():
    x = _boxes.values()
    x.sort(key=attrgetter('uid'))
    return x

def splitYUML(spec):
    word = ''
    shapeDepth = 0
    for c in spec:
        if c == '[':
            shapeDepth += 1
        elif c == ']':
            shapeDepth -= 1

        if shapeDepth == 1 and c == '[':
            yield word.strip()
            word = c
            continue

        word += c
        if shapeDepth == 0 and c == ']':
            yield word.strip()
            word = ''
    if word:
        yield word.strip()

def crop(fin, fout):
    img = Image.open(fin)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    bg = Image.new('RGB', img.size, (255, 255, 255))
    diff = ImageChops.difference(img, bg)
    area = img.crop(diff.getbbox())
    area.save(fout, 'png')
