"""
En un juego de plataforma de laberintos hay que saber
si la celda en la que esta el player y el enemigo es la misma. 
Si lo están entraran a una batalla. para poder saber si esta 
cerca el mundo cuenta con una reticula. Movimientos solo 
pueden ser adelante, atras, arriba, abajo. 

El programa pregunta X y Y del player y se le indica la 
distancia Manhattan a la que se encuentran.

__|__|__|__|__X
__|__|__|__|__|
__|__|__|__|__|
__|__|__|__|__|
Y_|__|__|__|__|

"""
from math import sqrt 

print("Debemos calcular la distancia del enemigo para entrar en combate. Introduce tus coordenas y las del enemigo")

x_player = int(input ("mi coordenada X:"))
y_player = int(input ("mi coordenada Y:"))

x_enemigo = int(input ("coordenada X del enemigo:"))
y_enemigo = int(input ("coordenada Y del enemigo:"))

a = (x_player - x_enemigo)
b = (y_player - y_enemigo)
d = abs(a) + abs(b)

print (f"el enemigo esta a {d} casillas, por lo tanto...")

if (d==0):
  print ("entran en combate")
else:
  print ("no entran en combate")
