#!/usr/bin/python
 
import sys
 
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) == 26:
	    idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, GI, GenBankAccession, PlatformCLONEID, PlatformORF, PlatformSPOTID, Chromosomelocation, Chromosomeannotation, GOFunction,GOProcess, GOComponent, GOFunctionID,  GOProcessID, GOComponentID = data

    if genetitle == "angiopoietin-like 4":
    	print "{0}\t{1}".format(genetitle, gsd19026)
