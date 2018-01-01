#!/usr/bin/python
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")



class MRWordFreqCount(MRJob):

# Aprendo a mostrar por pantalla los campos que me interesan.

    def mapper(self, _, line):

	data = line.strip().split("\t")
    	if len(data) == 26:
	idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, 
	NucleotideTitle, GI, GenBankAccession, PlatformCLONEID, PlatformORF, PlatformSPOTID, Chromosomelocation, Chromosomeannotation,
	GOFunction,GOProcess, GOComponent, GOFunctionID,  GOProcessID, GOComponentID = data

# imprimo los 13 primeros campos

    	print "{0}\t{1}".format(idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID,NucleotideTitle)


#        for word in WORD_RE.findall(line):
#            yield (word.lower(), 1)

#    def combiner(self, word, counts):
#        yield (word, sum(counts))

#    def reducer(self, word, counts):
#        yield (word, sum(counts))


if __name__ == '__main__':
    MRWordFreqCount.run()
