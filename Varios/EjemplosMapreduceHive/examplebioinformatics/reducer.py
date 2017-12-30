#!/usr/bin/python
 
import sys
 
GSDTotal = 0
oldKey = None
GSDcounter = 0
GSDavg = 0
 
# Recorremos los datos de entrada, que estan en formato clave/valor
# donde la clave es el genetitle y valor es el de la columna gsd19026
 
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Algo ha pasado, nos saltamos esta linea
        continue
 
    thisKey, thisGSD = data_mapped
 
    GSDTotal += float(thisGSD)
    GSDcounter += 1
    print thisKey, "\t", thisGSD

    
GSDavg = GSDTotal/GSDcounter	
print "\nLa media de GSD19026 para las muestras cuyo GenTitle vale angiopoietin-like 4 es ... \t", GSDavg
