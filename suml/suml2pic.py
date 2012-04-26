#!/usr/bin/env python
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

'''
[class]
[class]message>[class]
[class]<message[class]
'''

import os
import sys
import textwrap
import common

sequence_pic = os.path.join(os.path.dirname(__file__), 'sequence.pic')

def sumlExpr(spec):
    expr = []
    for part in common.splitYUML(spec):
        if not part: continue
        if part == ',':
            if expr: yield expr
            expr = []

        # [something like this]
        elif part[0] == '[' and part[-1] == ']':
            part = part[1:-1]
            expr.append(('record', part.strip()))
        # <message
        # >message
        elif part[0] in '<>':
            expr.append((part[0], part[1:].strip()))
        # message>
        # message<
        elif part[-1] in '<>':
            expr.append((part[-1], part[:-1].strip()))

    if expr: yield expr

def getFontWidth():
    return 0.13

def suml2pic(spec, options):
    exprs = list(sumlExpr(spec))

    pic = []
    pic.append('.PS')
    pic.append('copy "%s";' % (sequence_pic))
    pic.append('underline=0;')
    
    messages = []
    for expr in exprs:
        assert len(expr) in (1, 3)
        if len(expr) == 1:
            assert expr[0][0] == 'record'
            common.getBox(expr[0][1])

        elif len(expr) == 3:
            assert expr[0][0] == 'record'
            assert expr[2][0] == 'record'

            box1 = common.getBox(expr[0][1])
            box2 = common.getBox(expr[2][1])
            
            msgType = expr[1][0]
            if msgType == '>':
                messages.append('message(%s,%s,"%s");' % (box1.uid, box2.uid, expr[1][1]))
            elif msgType == '<':
                messages.append('message(%s,%s,"%s");' % (box2.uid, box1.uid, expr[1][1]))

    for box in common.getBoxes():
        #pic.append('object(%s,"%s");' % (box.uid, box.spec))
        pic.append('object3(%s,"%s",%f);' % (box.uid, box.spec, getFontWidth() * len(box.spec)))
    pic.append('step();')
    for box in common.getBoxes():
        pic.append('active(%s);' % (box.uid))

    pic.extend(messages)

    pic.append('step();')
    for box in common.getBoxes():
        pic.append('complete(%s);' % (box.uid))

    pic.append('.PE')
    return '\n'.join(pic) + '\n'

def transform(expr, fout, options):
    pic = suml2pic(expr, options)

    if options.png or options.svg:
        import subprocess
        import StringIO

        if options.scruffy:
            import scruffy

            svg = subprocess.Popen(['pic2plot', '-Tsvg'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(input=pic)[0]
            if options.png:
                tocrop = StringIO.StringIO()
                scruffy.transform(StringIO.StringIO(svg), tocrop, options)
                common.crop(StringIO.StringIO(tocrop.getvalue()), fout)
            else:
                scruffy.transform(StringIO.StringIO(svg), fout, options)
        elif options.png:
            png = subprocess.Popen(['pic2plot', '-Tpng'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(input=pic)[0]
            common.crop(StringIO.StringIO(png), fout)
        elif options.svg:
            subprocess.Popen(['pic2plot', '-Tsvg'], stdin=subprocess.PIPE, stdout=fout).communicate(input=pic)
    else:
        fout.write(pic)
