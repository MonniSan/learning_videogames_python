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
from random import randrange, random, Getrandom

print("Tu ex toxico y acosador intenta atacarte con sus falsas promesas de amor, \
  \n debes detenerlo con ataques verbales ofensivos para que se aleje y desaparezca \
  \n de tu vida. Tienes 3 oportunidades con tiros acertivos para derrotar a tu ex.")

def ask(msg):
  print(msg)
  return float (input("->"))

def getRandom(a,b):
  return a + (b-a)*random()

def getDistance (vx,vy):
  Gravity = 9.81
  t = vy/Gravity
  d = vx*2*t
  return d

def results(tx, dx, idx):
  print(f"D{idx}: {dx}")
  diff = abs(dx-targetX)
  print(f"Quedaste a {diff} mts")
  if (diff < 3):
    print ("*********************")
    print ("*******GANASTE*******")
    print ("*********************")

s1vx = ask("Velocidad del ataque en X")
s1vy = ask("Velocidad del ataque en Y")
s2vx = ask("Velocidad del ataque en X")
s2vy = ask("Velocidad del ataque en Y")
s3vx = ask("Velocidad del ataque en X")
s3vy = ask("Velocidad del ataque en Y")

targetX = getRandom(10,30)
results(targetX, getDistance(s1vx, s1vy),1)

r=getDistance(s1vx, s1vy)
print (f"D1:{r}")
print (f"D2:{r}")