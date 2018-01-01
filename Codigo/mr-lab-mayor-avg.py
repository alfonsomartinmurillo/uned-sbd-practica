#!/usr/bin/python
# -*- encoding: utf-8 -*-
from mrjob.job import MRJob

import re

WORD_RE = re.compile(r"[\w']+")

class mrlabmayoravg(MRJob):

#funcion mapper

    def mapper(self, _, line): #Esta función actúa por cada una de las lineas de entrada.

# La función mapper se va a centrar en filtrar, y devolver únicamente los campos que nos interesen

	data = line.strip().split("\t") # Elimino espacios y separo campos por tabuladores

    	if len(data) == 16: # Mapeo de los 16 campos de entrada
		idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, 			NucleotideTitle, valormaximo, valorminimo,average = data
	
		# dispongo del average en formato float.
		tgsm19023=float(gsm19023)
		if tgsm19023>=100 and tgsm19023<=1000:
		# Imprimo el campo average, que utilizará el reduce
			yield(_,float(average))

# La función reducer se encarga de obtener la máxima media
    def reducer(self, _, average):
	yield ("Media Maxima", max(average))
	

if __name__ == '__main__':
    mrlabmayoravg.run()
