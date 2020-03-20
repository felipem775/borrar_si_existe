#!/usr/bin/python
# -*- coding: utf-8 -*-

# Autor: Felipe Maza ( http://felipem.com/ )

import os.path

# Obtener un listado de los ficheros que se encuentran en un directorio y sus subdirectorios
def ficherosEnDir(ruta):
  listado = []
  for raiz, subcarpetas, ficheros in os.walk(ruta):
    for fichero in ficheros:
      listado.append(os.path.join(raiz,fichero))
  return listado

# Guardar texto en un fichero
def escribirFichero(rutaFichero, texto):
  f = open(rutaFichero,'w')
  f.write(texto)
  f.close()

# Guardar texto al final de un fichero
def escribirFicheroAlFinal(rutaFichero, texto):
  f = open(rutaFichero,'a')
  f.write(texto)
  f.close()

# Devuelve array con las líneas del fichero
def leeLineas(rutaFichero):
  f = open(rutaFichero,'r')
  lineas = f.readlines()
  f.close()
  return lineas


# http://stackoverflow.com/a/600612/2428230
def mkdir_p(path):
    import errno
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

  
# calcula el md5,sha256
def hash(rutaFichero):
  import hashlib
  m = hashlib.md5()
  s256 = hashlib.sha256()
  try:
    fo = open(rutaFichero,"rb")
    while 1:
      d = fo.read(8192)
      if not d:
        break
      m.update(d)
      s256.update(d)
  except IOError:
    print("ERROR No se puede abrir el fichero: " + rutaFichero)
    return
  fo.close()
  return [m.hexdigest(), s256.hexdigest()]

# Calcular el MD5 de un fichero
def md5sum(rutaFichero):
    return hash(rutaFichero)[0]

def sha256sum(rutaFichero):
    return hash(rutaFichero)[1]

if __name__ == '__main__':
    print("funciones ficheros")
