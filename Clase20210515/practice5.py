"""
El usuario va a introducir las velocidades de 3 disparos. 
Cada disparo consta de una velocidad en Y y X. 

La computadora coloca aleatoriamente un objetivo en una 
posición x, y=0 Que es la misma altura del usuario. 

Despues de haber recibido la informacion el algoritmo 
debera indicar si el usuario dio en el blanco o no con una 
difrencia de hasta 3 unidades a la izquiera o derecha. 

vy/g = t
d = vx*2t vx = d/2(vy/g) = d/1 / 2vy/g = dg/2vy

"""
from os import system 
from time import sleep
from random import randrange, random

print("Tu ex toxico y acosador intenta atacarte con sus falsas promesas de amor, \
  \n debes detenerlo con ataques verbales ofensivos para que se aleje y desaparezca \
  \n de tu vida. Tienes 3 oportunidades con tiros acertivos para derrotar a tu ex.")

WIDTH = 5
HEIGHT = 10

#coordenas del jugador 
player_x = WIDTH/2
player_y = 0


#coordenas del enemigo ex porque todos odiamos a nuestros ex 
ex = randrange(0,WIDTH,1)
ey = 0
evx = ex + 1 #talvez esto no va 

#coordenadas iniciales del disparo y velocidad 
bullet_x = player_x
bullet_y = player_y

#distancia entre tu y el enemigo
distance_x = int(abs(player_x-ex))

def atack (vx,distancia):
  velocity = vx
  return velocity



if (distance_x == vx):
  print ("Has ganado y tu ex jamas te molestará de nuevo")
else:
  print ("No te preocupes tienes otra oprtunidad")

if (distance_x == vx):
  print ("Has ganado y tu ex jamas te molestará de nuevo")
else:
  print ("No te desanimes te queda una oprotunidad")

if (distance_x == vx):
  print ("Has ganado y tu ex jamas te molestará de nuevo")
else:
  print ("Ups tu ex a logrado conquistarte de nuevo.. AMIG@ DATE CUENTA")