#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# entrada desde STDIN
for line in sys.stdin:
    # eliminamos espacios blancos al principio y final
    line = line.strip()

    # parseamos la entrada que hemos obtenido del mapper.py
    word, count = line.split('\t', 1)

    # pasamos el contador de string a int
    try:
        count = int(count)
    except ValueError:
        # si el contados no es un numero, descartamos la linea
        continue

    # este if solamente funciona porque Hadoop ordena la salida del map por la clave (aqui es word) antes de pasarsela al reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # escribir resultado a STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# escribimos la ultima palabra
if current_word == word:
    print '%s\t%s' % (current_word, current_count)

