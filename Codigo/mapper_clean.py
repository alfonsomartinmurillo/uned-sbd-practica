#!/usr/bin/python
 
import sys
 
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) == 26:
	    idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, GI, GenBankAccession, PlatformCLONEID, PlatformORF, PlatformSPOTID, Chromosomelocation, Chromosomeannotation, GOFunction,GOProcess, GOComponent, GOFunctionID,  GOProcessID, GOComponentID = data

    
    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle)
