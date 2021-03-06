#!/usr/bin/python
# -*- encoding: utf-8 -*-
from mrjob.job import MRJob

import re

WORD_RE = re.compile(r"[\w']+")



class mrlabgeo(MRJob):

#funcion mapper

    def mapper(self, _, line): #Esta función actúa por cada una de las lineas de entrada.

# Aprendo a mostrar por pantalla los campos que me interesan.
# mapeo de linea, y generacion de estructura de 26 campos

	data = line.strip().split("\t") # Elimino espacios y separo campos por tabuladores

    	if len(data) == 26: #Generación de los 26 campos de entrada
		idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, 			NucleotideTitle, GI, GenBankAccession, PlatformCLONEID, PlatformORF, PlatformSPOTID, Chromosomelocation, 				Chromosomeannotation,GOFunction,GOProcess, GOComponent, GOFunctionID,  GOProcessID, GOComponentID = data

		#Control de nulos
		if gsm19023 == "null": gsm19023=0
		if gsd19024 == "null": gsd19024=0
		if gsd19025 == "null": gsd19025=0
		if gsd19026 == "null": gsd19026=0

		#Generación de máximos, mínimos y medias
		valormaximo=max(float(gsm19023), float(gsd19024), float(gsd19025), float(gsd19026))
		valorminimo=min(float(gsm19023), float(gsd19024), float(gsd19025), float(gsd19026))
		average=(float(gsm19023)+ float(gsd19024)+ float(gsd19025)+ float(gsd19026))/4

		# imprimo los 13 primeros campos y los campus calculados de máximo, mínimo y media

		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}".format(idref,ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol,uniGeneID,NucleotideTitle,valormaximo,valorminimo,average)


#        for word in WORD_RE.findall(line):
#            yield (word.lower(), 1)

#    def combiner(self, word, counts):
#        yield (word, sum(counts))

#    def reducer(self, word, counts):
#        yield (word, sum(counts))


if __name__ == '__main__':
    mrlabgeo.run()
