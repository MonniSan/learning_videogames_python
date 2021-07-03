from random import random, randint
from math import sin, cos

"""
********************************************************************************
Vamos a definier la clase padre de creaturas y sus clases hijas:
>Orcos 
>Elfos 
>Troles
Vamos a poner varios comentarios y si tal vez sea un archivo
extenso <mala practica> pero así le entiendo u.u
********************************************************************************
"""
#Clase Padre CREATURE
class Creature:
  MIN_SPEED = 2 #constante de velocidad minima

  #se definen las priopiedades de la Clase:
  def __init__(self,px,py, max_speed = 1):
    self.__px = px
    self.__py = py
    self.__strength = 0 
    self.__magic = 0 
    self.__life = 0
    self.__percent_strength = 0 
    self.__percent_magic = 0
    self.changeDirection(max_speed) #max_speed se usa para sacar hipotenusa

  #posición inicial, cambia cada movimiento. 
  def getPx(self):
    return self.__px
  def getPy(self):
    return self.__py

  #velocidad = hipotenusa
  def getSx(self):
    return self.__sx
  def getSy(self):
    return self.__sy

  # rebotar para no salirse del mundo (use otra logica para saber si entendí)
  def bounce(self, do_AxisY = False):
    if (do_AxisY):
      self.__sx *= -1
    else:
      self.__sy *= -1
    # PREGUNTA: ¿si sx=5 y le faltan 4 espacios para llegar al borde entonces 
    # camina 5 pasos para el lado contrario, o topa en el borde y rebota 1?
    #Según lo que entiendo con la formula, son 5 pasos para el lado contrario.

  #movimiento: calculamos la velocidad y correguimos la dirección en caso de rebote. 
  def move(self,world_width,world_height, replace_sx = 0,replace_sy = 0):
    
    if replace_sx == 0:
      sx= self.getSx()
    else:
      replace_sx
    if replace_sy == 0:
      sy= self.getSy() 
    else:
      replace_sy

    if(self.getPx() + sx > world_width and self.getSx() > 0):
      self.bounce()
    if(self.getSx() + sx < 0 and self.getSx() < 0):
      self.bounce()
    if(self.getPy() + sy > world_height and self.getSy() > 0):
      self.bounce()
    if(self.getPy() + sy < 0 and self.getSy() < 0):
      self.bounce()

  #Dirección de movimiento (viene lo bueno... notas en el cuaderno)
  def changeDirection(self, max_speed):
    max_speed = max(max_speed, Creature.MIN_SPEED) #por si la velocidad sale menor a 2
    random_speed = int(random()*(max_speed-Creature.MIN_SPEED) + Creature.MIN_SPEED) #hipotenusa
#random_angle = 2*pi*random = 2*3.14159*random (en mi consola, no se como poner PI grados)
# PI = 180º => random_angle = 2*pi*random = 2*180*random
# 2*180º = 360º => random_angle = 360*random (la solución que se me occurrió)
    random_angle = 360*random()
    self.__sx=int(random_speed*cos(random_angle)) # co = h*cos@
    self.__sy=int(random_speed*sin(random_angle)) # ca = h*sin@

#obteniendo vida, vida maxima; fuerza, magia y sus porcentajes
  def getLife(self):
    return self.__life
  def getMaxLife(self):
    return self.__max_life
  def getStrength(self):
    return self.__percent_strength
  def getMagic(self):
    return self.__magic
  def getPorcentStrength(self):
    return self.__percent_strength
  def getPorcentMagic(self):
    return self.__percent_magic
  
#La vida, fuerza y magia deben estar en la misma posición
# que la criatura, vamos a definir el punto (p) para que 
# las tres propiedades se mueva con él. 
  def setPx(self,p):
    self.__px = p
  def setPy(self,p):
    self.__py = p
  def setSx(self,p):
    self.__sx = p
  def setSy(self,p):
    self.__sy = p
#Ahora vamos a posicionar las propiedades en p
  def setLife(self,p):
    self.__life = p
  def setMaxLife(self,p):
    self.__max_life = p
  def setStrength(self,p):
    self.__strength = p
  def setMagic(self,p):
    self.__magic = p
  def setPorcentStrength(self,p):
    self.__percent_strength = p
  def setPorcentMagic(self,p):
    self.__percent_magic = p

#Usar Healer para curarte, 0.5 te divide la mitad la vida.
#por 1.5 aumenta la mitad de la vida a tu vida actual, si es mayor 
#de la vida maxima, entonces devuelve la vida maxima. 
  def heal(self):
    heal_life = int(1.5*self.getMaxLife())
    self.__life = min(heal_life, MAX_LIFE)

#Pelea: daño ejrecido y recivido. 
  def getHitForce(self):
    return self.getPorcentStrength()*self.getStrength() + self.getPorcentMagic*self.getMagic()
  def reciveHit(self,hit):
    self.setLife(set.getLife()-min(self.getLife(),hit))

# regresando cadena con datos
  def __str__(self):
    return f"______________________________________________________________________________\
      \n Position:(x,y) = ({self.getPx()},{self.getPy()})      Strength: {self.getStrength()} --- Magic: {self.getMagic()}\
      \n Speed: (sx,sy) = ({self.getSx()},{self.getSy()})      Life of Maxim Life: {self.getLife()} of {self.getLife()}"

if __name__ == "__main__":
    c = Creature(10,10,1)
    print(c)
    c.bounce()
    print(c)
    c.bounce(do_AxisY = True)
    print(c)

"""
***************************************
  Vamos a definir la clase hija Orcos
****************************************
"""


