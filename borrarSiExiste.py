#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Programa que calcula los md5 del directorio que pasa como primer parámetro y
# lo compara con los del fichero que se pasa como siguiente parámetro, si
# existe lo elimina..
#
# Autor: Felipe Maza (felipe @rroba felipem punt. com)
# Version: 160218
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#

import sys
import os
import os.path
import hashlib
from progressBar import progressBar
import fichero

def main():
    if len(sys.argv) != 3:
        print('ERROR Debe especificar 1 ruta, 2 fichero md5')
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print('ERROR El fichero o directorio no existe: ' + sys.argv[1])
        sys.exit(1)

    if not os.path.exists(sys.argv[2]):
        print('ERROR El fichero de md5 no existe: ' + sys.argv[2])
        sys.exit(2)

    # listado de ficheros que existen
    lineas = fichero.leeLineas(sys.argv[2])
    existen = []
    for l in lineas:
        existen.append(l[0:32])

    ficheros = []
    if os.path.isdir(sys.argv[1]):
        ficheros = fichero.ficherosEnDir(sys.argv[1])
    else:
        ficheros = [sys.argv[1]]

    print("Se van a calcular los MD5 de " + str(len(ficheros)) + " ficheros")

    iteracion = 0
    total = len(ficheros)
    borrados = 0
    errores = []
    for f in ficheros:

        iteracion += 1
        if fichero.md5sum(f) in existen:
            borrados += 1
            try:
                os.remove(f)
            except:
                print("Error borrando: " + f)
                errores.append(f)
            progressBar(iteracion,total, str(borrados) + " " + str(f))
        else:
            progressBar(iteracion,total)



    print("\nSe han borrado " + str(borrados) + " de " + str(total) + " ficheros")
    print("Errores: " + "\n".join(errores))
    return 0

if __name__ == '__main__':
    main()
