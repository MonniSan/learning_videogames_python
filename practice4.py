"""
En un juego de plataforma de laberintos hay que saber
si la celda en la que esta el player y el enemigo es la misma. 
Si lo están entraran a una batalla. para poder saber si esta 
cerca el mundo cuenta con una reticula. Movimientos solo 
pueden ser adelante, atras, arriba, abajo. 

El programa pregunta X y Y del playeer y se le indica la 
distancia Manhattan a la que se encuentran. 

"""
from math import sqrt 

x_player = int(input ("X player:"))
y_player = int(input ("Y player:"))

x_enemigo = int(input ("X enemigo:"))
y_enemigo = int(input ("Y enemigo:"))

a = (x_player - x_enemigo)
b = (y_player - y_enemigo)
d = abs(a) + abs(b)
print (f"el enemigo esta a {d} casillas")

