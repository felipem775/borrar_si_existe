#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Módulo para mostrar una barra de progreso en nuestros scripts.
#
# Autor: Felipe Maza ( http://felipem.com/ )
# Autor: Iñaki Silanes ( http://isilanes.org/ )
#
# Versión: 120603


import sys
import time
import os
if sys.version_info < (3,):
    range = xrange

def progressBar(iteracion,total,mensajePrevio=None):
    # Get width of window:
    try:
        wwidth = int(os.popen('stty size', 'r').read().split()[1]) - 2
    except ValueError:
        wwidth = 78

    # Extra width:
    lst = len(str(total))
    xwidth = 2*lst + 9

    # Progress bar itself:
    barra = ''
    rango = int((wwidth - xwidth) * iteracion / total)
    for i in range(rango):
        barra += "="

    # Total status line:
    fmt = '[%%-%is] %%%ii/%%%ii %%3i%%%%' % (wwidth - xwidth, lst, lst)
    lineaEstado = fmt % (barra, iteracion, total, 100.0*iteracion/total)

    # Print message and status line:
    print('\r'),
    if mensajePrevio:
        fmt = '%%-%is' % (wwidth)
        print(fmt % (mensajePrevio))

    print(lineaEstado),
    sys.stdout.flush()

# Test
if __name__ == '__main__':
    maxi = 10
    print("test")
    for i in range(1,maxi+1):
        progressBar(i,maxi,"Mensaje %i" % (i))
        time.sleep(1)
