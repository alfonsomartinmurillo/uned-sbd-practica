#!/usr/bin/env python

import sys

# entrada de la entrada estandar STDIN
for line in sys.stdin:
    # eliminamos espacios blancos al principio y final
    line = line.strip()
    # dividimos la linea en palabras
    words = line.split()
    # incrementamos los contadores
    for word in words:
        # escribimos los resultados a la salida estandard STDOUT. 
        # Esta salida sera la entrada para el reduce, es decir, para reducer01.py
        #
        # delimiado por tab, para cada palabra ponemos 1 ocurrencia
        print '%s\t%s' % (word, 1)

