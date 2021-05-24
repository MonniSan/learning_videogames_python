"""
El juego se trata de desarmar bombas
Si la bomba es de tipo AB101 entonces los cables que hay 
que cortar son el rojo y el azul. 
Si la bomba es de tipo IU12 el cable rojo se debe cortar
y el azul se debe mantener 
Si la bobmba es de tipo MAA089 el verde se debe conectar 
al la terminal negra y el cable rojo a la amarilla
Si la bomba es de tipo T78 solo hay que quitar la bateria 

KABOOM -> perder
UFF -> ganar

"""
from os import system
from time import sleep
import random
system ("clear")

print("Hola amante de los perros y experto en bombas! Recuerda las siguiente intrucciones: \
\n 1. Si la bomba es de tipo AB101 entonces los cables que hay que cortar son el rojo y el azul. \
\n 2. Si la bomba es de tipo IU12 el cable rojo se debe cortar y el azul se debe mantener \
\n 3. Si la bobmba es de tipo MAA089 el verde se debe conectar \
\n al la terminal negra y el cable rojo a la amarilla \
\n 4. Si la bomba es de tipo T78 solo hay que quitar la bateria ")

#No hacer nada
Normal = 0
#Cortar 
Cut = 1
#Reconectar a terminales: negra amarilla
To_black = 2
To_yellow = 3
#bateria
#cables: rojo verde y azul

print ("Estas por desactivar la bomba para salvar a la asociacion de rescate canina. \
\n Es necesario desactivar la bomba para salvar a todos los perros, \
\n favor de darnos las instrucciones para lograrlo, los perros cuentan contigo")

def getBomb():
  num = random.random()
  if (num <= 0.25):
    return "AB101"
  elif (0.25 < num <= 0.5):
    return "IU12"
  elif ( 0.5 < num <= 0.75):
    return "MAA089"
  else:
    return "T78"


bomba = getBomb() 
print (f"La bomba es de tipo {bomba}")


def ask(msg):
  print(msg)
  pr = int(input("Selecciona:"))
  return pr


red = ask("Que deseas hacer con el cable rojo: \
  \n 0.Dejarlo \
  \n 1.Cortarlo \
  \n 2.Conectarlo a la terminal negra \
  \n 3.Conectarlo a la terminal amarilla")
  
blue = ask("Que deseas hacer con el cable azul: \
  \n 0.Dejarlo \
  \n 1.Cortarlo \
  \n 2.Conectarlo a la terminal negra \
  \n 3.Conectarlo a la terminal amarilla")

green = ask("Que deseas hacer con el cable verde:\
  \n 0.Dejarlo \
  \n 1.Cortarlo \
  \n 2.Conectarlo a la terminal negra \
  \n 3.Conectarlo a la terminal amarilla")

battery = ask("Que deseas hacer con la bateria: \
  \n 0.Dejarla \
  \n 1.Quitarla")

success = False


#si la bomba es de tipo AB101 entonces se deben cortar los cables rojo y azul. 
if bomba == "AB101" and red==Cut and blue==Cut and green==Normal and battery==Normal:
  success = True

#si la bomba es de tipo IUI2 el cable rojo se corta.  
if bomba == "IU12" and red==Cut and blue==Normal and green==Normal and battery==Normal:
  success = True

#si la bomba es de tipo MAA089 entonces el verde se conecta a la terminal negra y el rojo a la terminal amarilla
if bomba == "MAA089" and red==To_yellow and blue==Normal and green==To_black and battery==Normal:
  success = True

#si la bomba es de tipo T78 solo hay que quitar la bateria
if bomba == "T78" and red==Normal and blue==Normal and green==Normal and battery==Cut:
  success = True

i=50
while(i>=0):
  i-=1
  sleep (0.01)
  system ("clear")
  s = "-"*i + "*"
  print(s)

system("clear")

if success:
  print("UFFF lo lograste, has salvado el día. En hora buena \
    \n los perritos estan a salvo")
else:
  print("K-A-B-0-0-M. Fallaste, los perritos te mandan saludos \
    \n desde el cielo canino")
