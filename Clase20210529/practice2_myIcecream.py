"""
Simular la llegada de clientes 
Cada cliente tendra una cantidad de dinero aleatria, 
asi como un sabor que quiera y un nombre que será un numero entre 
el 1 y el 100 para detectarlos. Los nombres podran ser mapeados a nombres 
reales opcionalmente. 

El cliente tiene una cantidad de dinero que determinará el tamaño del helado 
y tendra un sabor favorito. Si la tienda le da el sabor que quiere, entonces 
dara propina, un aleatroio entre el 5% al 10% del costo del helado siempre y cuando 
tenga dinero para hacerlo. 

La tienda de helados tiene 3 tamaños: 1 bola, 2 bolas, 3 bolas. 
La tienda tambien tiene 1 especial: BananaSplit. Este es en general un
helado de 3 bolas y cuesta 20 pesos más. 

Cada helado que se entrega a un cliente solo se diferencia por la cantidad de bolas de 
helado y todas las bolas de helado son del mismo sabor. 

Cada helado que se entrega a un cliente solo se diferencia por la cantidad de bolas 
de helado y todas las bolas de helado son del mismo sabor. 

Los clientes cuando llegan pueden pedir helado de 1, 2, 3 bolas o banasplit, es 
aleatorio, y no depende de su dinero. Sin embargo, después de pedirlo, si no 
cuentan con el dinero suficiente, los clientes se van. 

El simulador tiene que entregar resultados de cantidad de dinero recabada 
a lo largo de 5 dias, en los cuales pueden llegar un minimo de 10 clientes 
y un maximo de 30.

Se deberá resolver usando metodologia orientada a objetos, con al menos las Clases:
cliente helado bananasplit extiende/hereda de helado

La salida del programa deberá indicar por cada cliente qué sucedió y 
al final dar la cuenta total. 
"""

from random import random

#Generando Clase Cliente

class Client:
  NumberC = 0
  FlavorC = 0 
  MoneyC = 0
#Función para obtener el número, sabor y dinero del cliente 
  def __init__(self, nc = 0, fc=0, mc = 0):
    self.__n = min(max(0, nc),10)
    self.__f = min(max(0, fc),5)
    self.__m = min(max(0,mc),200)
    Client.NumberC += 1
    Client.FlavorC += 1
    Client.MoneyC += 1
  def getN(self):
    return self.__n
  def getF(self):
    return self.__f
  def getM(self):
    return self.__m
#Función para asignar el número, sabor y dinero del cliente
  def setN(self, numN):
    numN = int(random()<=10)
    print("Número del Cliente: " + str(numN))
    self.__n = min(max(0, numN),100)
  def setF(self, numF):
    numF = int(random(random()<=5))
    print("Sabor favorito del Cliente: " + str(numF))
    self.__f = min(max(0, numF),100)
  def setM(self, numM):
    numM = int(random(random()<=200))
    print("Dinero del Cliente: " + str(numM))
    self.__n = min(max(0, numM),100)
#Función para regresar el número, sabor y dinero del cliente
  def __str__(self):
    return f'{self.__n}, {self.__f}, {self.__m} \n'