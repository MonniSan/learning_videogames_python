"""
Hay un hechicero que tiene un caldero. El caldero se llama RGB,
El usuario debe indicar al hechicero la cantidad de cada uno de los componentes del hechizo que colocara
en el caldero RGB

0-> 255 Ml {Rooibos, Greenish, Boost} > 765 ml

indica Lts pocion:> Cuanto componente se crea de cada sustancia ingresada.

Cual es el color final lineal de acuerdo a cantidades posterior al hechizo:

Formula = ColorFinal  = (QtyR)/? + QtyG*255/?  + QtyB*255*255/?
"""

rooibos = int ( input ("indica la cantidad de rooibos [0-255]:"))
greenish = int ( input ("indica la cantidad de greenish[0-255]:"))
boost = int ( input ("indica la cantidad de boost[0-255]:"))

ML_Totales = rooibos + greenish + boost
ColorFinal = rooibos/ML_Totales + greenish/ML_Totales*255 + boost/ML_Totales*255*255
print (f"La pocion tiene {ML_Totales} ml y es de color {ColorFinal}")