#!/usr/bin/python
# -*- encoding: utf-8 -*-
from mrjob.job import MRJob

import re

WORD_RE = re.compile(r"[\w']+")

class mrlabmayoravg(MRJob):

#funcion mapper

    def mapper(self, _, line): #Esta función actúa por cada una de las lineas de entrada.

# La función mapper se va a centrar en devolver únicamente los campos que nos interesen

	data = line.strip().split("\t") # Elimino espacios y separo campos por tabuladores

    	if len(data) == 16: # Mapeo de los 16 campos de entrada
		idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, 			NucleotideTitle, valormaximo, valorminimo,average = data
	
		# me quedo con el campo gsd19025 y un 1, para realizar sumatorio de todos los elementos
		yield(gsd19025,1)
		print "{0}\t{1}".format(gsd19025,"1")


# La función reducer se encarga de obtener la media de todos los elementos
    def reducer(self, gsd19025, idunitario):
	yield ("Suma Total",max(gsd19025))
	

if __name__ == '__main__':
    mrlabmayoravg.run()
