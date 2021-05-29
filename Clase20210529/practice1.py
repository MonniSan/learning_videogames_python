from random import random

#Generando una clase de coordenadas

class Point:
  number_of_points = 0
#Función para obtener coordenadas de "X" y "Y" en un panel limitado
  def __init__(self, px = 0, py = 0):
    self.__x = min(max(0, px),100)
    self.__y = min(max(0, py),100)
    Point.number_of_points += 1
#Función para regresar coordenadas
  def __str__(self):
    return f'{self.__x} , {self.__y}\n'
#Función para obtener coordenadas
  def getX(self):
    return self.__x
  def getY(self):
    return self.__y
#Función para asignar las coordenadas
  def setX(self, num):
    print("setting x " + str(num) )
    self.__x = min(max(0, num),100)
  def setY(self, num):
    self.__y = min(max(0, num),100)

#Generando una clase hijo del color de los puntos

class ColorPoint(Point):
  #llamando a la clase pardre para definir función de color
  def __init__(self, px = 0, py = 0, color = None):
    super().__init__(px=px,py=py)
    self.__c = color
  #Función para obtener el color
  def getColor(self):
    return self.__c
  #Función  para asignar el color
  def setColor(self, color):
  #Función de salida regresa el color
    self.__c = color
  def __str__(self):
    return f'{self.getX()}, {self.getY()}, {self.__c} \n'

#Generando clase de lista de coordenadas 

class PointList:
  def __init__(self):
    self.__points = []
    
  def append(self,point):
    self.__points.append(point)
    
  def get(self, i):
    return self.__points[i]
    
  def __str__(self):
    res = ""
    for i in self.__points:
      res += str(i) + '\n'
    return res

#Probando el sistema
p = Point(50,70)

q = Point(-50,-70)
q.setX(20)
q.setY(99)

r =  ColorPoint(40,50, [23,27,250])
print(r)
print(r.getX())
print(r.getY())

points = PointList()
f = open('points.csv','w')
for i in range(0,1000):
  if(random() > 0.5):
    points.append( Point( random()*100 ,  random()*100 ) )
  else:
    points.append( ColorPoint( random()*100 ,  random()*100 , [30,30,255] )  )

for i in range(0,1000):
  f.write( str(points.get(i)) )
f.close()

print("Total number of points " + str(Point.number_of_points))
