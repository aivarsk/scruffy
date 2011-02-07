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

# Makes SVG shapes look hand-drawn like "scruffy" UML diagrams:
#   http://yuml.me/diagram/scruffy/class/samples
#
# Adds new points (with slight offsets) between existing points.
# Changes font to ..?
# Adds shadows to polygons
# Adds gradient

import sys
import math
import random
import xml.etree.ElementTree as etree

def parsePoints(points):
    points = points.split()
    return [(float(x), float(y)) for x, y in [point.split(',') for point in points]]

def lineLength(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.sqrt(dx * dx + dy * dy)

def splitLine(p1, p2, l):
    ''' find point on line l points away from p1 '''
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    lp = math.sqrt(dx * dx + dy * dy)
    ax = dx / lp
    ay = dy / lp
    return (p1[0] + l * ax, p1[1] + l * ay)

def frandrange(start, stop):
    ''' random.randrange for floats ''' 
    start, stop = int(start * 10.0), int(stop * 10.0)
    r = random.randrange(start, stop)
    return r / 10.0

SVG_NS = 'http://www.w3.org/2000/svg'
def ns(tag):
    return '{%s}%s' % (SVG_NS, tag)

def transformRect2Polygon(elem):
    pass

def transformLine2Polyline(elem):
    elem.tag = ns('polyline')
    elem.points = '%(x1)s,%(y1)s %(x2)s,%(y2)s' % elem.attrib
    for key in ('x1', 'x2', 'y1', 'y2'): del elem.attrib[key]

def transformPolyline(elem):
    points = parsePoints(elem.attrib['points'])
    newPoints = []
    for i in xrange(len(points) - 1):
        p1, p2 = points[i], points[i + 1]

        newPoints.append(p1)
        l = lineLength(p1, p2)
        if l > 10:
            p = splitLine(p1, p2, frandrange(4, l - 4))
            newPoints.append((
                p[0] + frandrange(0.5, 2) * random.choice([1, -1]),
                p[1] + frandrange(0.5, 2) * random.choice([1, -1])
            ))

    newPoints.append(points[-1])

    elem.attrib['points'] = ' '.join(['%f,%f' % p for p in newPoints])

_usedColors = {}

def transformPolygon(elem):
    transformPolyline(elem)
    fill = elem.get('fill', '')
    if fill == 'none':
        elem.attrib['fill'] = 'white'

def transformText(elem, font):
    elem.attrib['font-family'] = font

def transformAddShade(root, elem):
    if elem.get('fill', '') == 'white' and elem.get('stroke', '') == 'white':
        # Graphviz puts everything in one big polygon. Skip it!
        return

    # Need to prepend element of the same shape
    shade = root.makeelement(elem.tag, elem.attrib)
    for i, child in enumerate(root):
        if child == elem:
            root.insert(i, shade)
            break

    shade.attrib['fill'] = '#999999'
    shade.attrib['stroke'] = '#999999'
    shade.attrib['stroke-width'] = shade.attrib.get('stroke-width', '1')
    shade.attrib['transform'] = 'translate(4, 4)'
    shade.attrib['style'] = 'opacity:0.75;filter:url(#filterBlur)'

def transformAddGradient(elem):
    if elem.get('fill', '') == 'white' and elem.get('stroke', '') == 'white':
        # Graphviz puts everything in one big polygon. Skip it!
        return

    fill = elem.get('fill', '')
    if fill == 'none':
        elem.attrib['fill'] = 'white'
    elif fill != 'black':
        _usedColors[fill] = True
        elem.attrib['style'] = 'fill:url(#' + fill + ');' + elem.attrib.get('style', '')

def _transform(root, options, level=0):
    for child in root[:]:
        if child.tag == ns('rect'):
            transformRect2Polygon(child)
        elif child.tag == ns('line'):
            transformLine2Polyline(child)

        if child.tag == ns('polygon'):
            transformPolygon(child)
            transformAddShade(root, child)
            transformAddGradient(child)
        elif child.tag == ns('path'):
            #transformAddShade(root, child)
            pass
        elif child.tag == ns('polyline'):
            transformPolyline(child)
            #see class diagram - shade of inside line
            #transformAddShade(root, child)
        elif child.tag == ns('text'):
            if options.font:
                transformText(child, options.font)

        _transform(child, options, level + 1)

    if level == 0:
        defs = root.makeelement(ns('defs'), {})
        root.insert(0, defs)
        filterBlur = etree.SubElement(defs, ns('filter'), {'id': 'filterBlur'})
        etree.SubElement(filterBlur, ns('feGaussianBlur'), {'stdDeviation': '0.69', 'id':'feGaussianBlurBlur'})
        for name in _usedColors:
            gradient = etree.SubElement(defs, ns('linearGradient'), {'id': name, 'x1':"0%", 'xy':"0%", 'x2':"100%", 'y2':"100%"})
            etree.SubElement(gradient, ns('stop'), {'offset':'0%', 'style':'stop-color:white;stop-opacity:1'}) 
            etree.SubElement(gradient, ns('stop'), {'offset':'50%', 'style':'stop-color:%s;stop-opacity:1' % name}) 

def transform(fin, fout, options):
    '''
        Read svg from file object fin, write output to file object fout

        options.png (boolean)   Try to produce PNG output
        options.font (string)   Font family to use (Ubuntu: Purisa)
    '''
    root = etree.parse(fin).getroot()
    _transform(root, options)

    scruffySvg = etree.tostring(root) + '\n'

    if options.png:
        import subprocess
        subprocess.Popen(['rsvg-convert', '-f', 'png'], stdin=subprocess.PIPE, stdout=fout).communicate(input=scruffySvg)
    else:
        fout.write(scruffySvg)

def main():
    import optparse

    parser = optparse.OptionParser(usage='usage: %prog [options] [input file]')
    parser.add_option('-p', '--png', action='store_true', dest='png',
                    help='create a png file (requires rsvg-convert)')
    parser.add_option('-o', '--output', action='store', dest='output',
                    help='output file name')
    parser.add_option('--font-family', action='store', dest='font',
                    help='output file name')
    (options, args) = parser.parse_args()

    if len(args) > 1:
        parser.error('Too many arguments')

    fin, fout = sys.stdin, sys.stdout
    if options.output:
        fout = open(options.output, 'wb')

    if len(args) > 0:
        fin = open(args[0])

    transform(fin, fout, options)

if __name__ == '__main__':
    main()
