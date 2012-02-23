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

sequence_pic = os.path.join(os.path.dirname(__file__), 'sequence.pic')

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

def sumlExpr(spec):
    expr = []
    for part in splitYUML(spec):
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

def suml2pic(spec, options):
    uids = {}
    class Foo:
        count = 0
        def __init__(self, label):
            self.label = label
            self.uid = 'A%d' % (Foo.count)
            Foo.count += 1


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
            name = expr[0][1]
            if name not in uids:
                uids[name] = Foo(name)
                pic.append('object(%s,"%s");' % (uids[name].uid, uids[name].label))

        elif len(expr) == 3:
            assert expr[0][0] == 'record'
            assert expr[2][0] == 'record'

            name1 = expr[0][1]
            if name1 not in uids:
                uids[name1] = Foo(name1)
                pic.append('object(%s,"%s");' % (uids[name1].uid, uids[name1].label))
            name2 = expr[2][1]
            if name2 not in uids:
                uids[name2] = Foo(name2)
                pic.append('object(%s,"%s");' % (uids[name2].uid, uids[name2].label))
            
            msgType = expr[1][0]
            if msgType == '>':
                messages.append('message(%s,%s,"%s");' % (uids[name1].uid, uids[name2].uid, expr[1][1]))
            elif msgType == '<':
                messages.append('message(%s,%s,"%s");' % (uids[name2].uid, uids[name1].uid, expr[1][1]))

    pic.append('step();')
    for x in uids.values():
        pic.append('active(%s);' % (x.uid))

    pic.extend(messages)

    pic.append('step();')
    for x in uids.values():
        pic.append('complete(%s);' % (x.uid))

    pic.append('.PE')
    return '\n'.join(pic) + '\n'

def transform(expr, fout, options):
    pic = suml2pic(expr, options)

    if options.png or options.svg:
        import subprocess

        if options.scruffy:
            import StringIO
            import scruffy

            svg = subprocess.Popen(['pic2plot', '-Tsvg'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(input=pic)[0]
            scruffy.transform(StringIO.StringIO(svg), fout, options)
        elif options.png:
            subprocess.Popen(['pic2plot', '-Tpng'], stdin=subprocess.PIPE, stdout=fout).communicate(input=pic)
        elif options.svg:
            subprocess.Popen(['pic2plot', '-Tsvg'], stdin=subprocess.PIPE, stdout=fout).communicate(input=pic)
    else:
        fout.write(pic)

def main():
    import optparse

    parser = optparse.OptionParser(usage='usage: %prog [options] <yUML string>')
    parser.add_option('-p', '--png', action='store_true', dest='png',
                    help='create a png file')
    parser.add_option('-s', '--svg', action='store_true', dest='svg',
                    help='create a svg file')
    parser.add_option('--scruffy', action='store_true', dest='scruffy',
                    help='process result with scruffy (works for svg and png output)')
    parser.add_option('-o', '--output', action='store', dest='output',
                    help='output file name')
    parser.add_option('--font-family', action='store', dest='font',
                    help='set output font family')
    (options, args) = parser.parse_args()

    if len(args) > 1:
        parser.error('Too many arguments')

    fout = sys.stdout
    if options.output:
        fout = open(options.output, 'wb')

    if len(args) == 0:
        spec = sys.stdin.read()
        spec = spec.replace('\n', ',')
    else:
        spec = args[0]

    if options.scruffy and not options.font:
        import common
        options.font = common.defaultScruffyFont()

    transform(spec, fout, options)

if __name__ == '__main__':
    main()

