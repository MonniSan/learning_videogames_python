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
#coordenas del jugador 
def dogame(opt):
  player_x = float(input("Tiro 1 vx:"))
  player_y = float(input("Tiro 1 vy:"))


#coordenas del enemigo ex porque todos odiamos a nuestros ex 
ex = randrange(0,WIDTH,1)
print("ex:" + str(ex))
ey = 0

#coordenadas iniciales del disparo y velocidad 
dx = (player_y/9.81)*2*player_x

#distancia entre tu y el enemigo
distance_x = int(abs(ex-dx))
if (distance_x < 3):
  print ("Has ganado y tu ex jamas te molestará de nuevo")
else:
  if(opt == 2):
    print("Ups! Tu ex a logrado conquistarte de nuevo.. AMIG@ DATE CUENTA")
else:
  print("Fallaste! Tu ex te empieza a enamorar pero tienes otro tiro, animo")

dogame(0)
dogame(1)
dogame(2)