""" 
Muestra la distancia a la que dos objetos circulares (bala y enemigo) 
deberian de estar para no chocar y la distancia a la que realmente 
están. 

Puedes pedir las siguientes entradas:
x,y de la bala y enemigo 
radio de bala y enemigo
"""
from math import sqrt 

print ("Vamos a calcular la distancia para matar al enemigo. Favor de darme las coordenadas solicitadas.")

x_enemigo = int(input ("X enemigo:"))
y_enemigo = int(input ("Y enemigo:"))
r_enemigo = int ( input ("cual es el radio del enemigo:"))

x_bala = int(input ("X bala:"))
y_bala = int(input ("Y bala:"))
r_bala = int ( input ("cual es el radio de la bala:"))

hipotenusa = r_bala + r_enemigo
a_cuad = (x_bala - x_enemigo)**2
b_cuad = (y_bala - y_enemigo)**2
d = sqrt(a_cuad+b_cuad)
print (f"la distancia entre el enemigo y la bala es de {d}, si su distancia critica es de {hipotenusa}, por lo tanto el enemigo...")

chocar = d - hipotenusa

if (chocar < 0):
  print ("muere")
else: 
  print ("sobrevive")