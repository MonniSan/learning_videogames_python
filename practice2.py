"""
Hay un hechicero que tiene un caldero. El caldero se llama RGB,
El usuario debe indicar al hechicero la cantidad de cada uno de los 
componentes del hechizo que colocara en el caldero RGB

0-> 255 Ml {Rooibos, Greenish, Boost} > 765 ml

indica Lts pocion:> Cuanto componente se crea de cada sustancia ingresada.

Cual es el color final lineal de acuerdo a cantidades posterior al hechizo:

Formula = ColorFinal  = (QtyR)/? + QtyG*255/?  + QtyB*255*255/?
"""
print ("Bienvenido, ayuda al Hechicero con su pocion.")
rooibos = int ( input ("Indica la cantidad de Rooibos [0-255]:"))
greenish = int ( input ("Indica la cantidad de Greenish[0-255]:"))
boost = int ( input ("Indica la cantidad de Boost[0-255]:"))

Ml_Totales = rooibos + greenish + boost
ColorFinal = rooibos/Ml_Totales + greenish/Ml_Totales*255 + boost/Ml_Totales*255*255
print (f"La pocion tiene {Ml_Totales} ml y es de color es {ColorFinal}")