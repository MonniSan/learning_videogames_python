"""
Generar un sistema de inventarios
El usuario va a meter 3 objetos en su mochila con 
una cantidad de repeticiones de la misma. 
El usuario usara uno de ellos requerido al sistema el nombre 
Si el sistema identifica que existe y que tiene suficientes unidades, 
le dara una de ellas, restando el total. 
"""

def add_to_backpack (bp_items, bp_units, total_add):
  item = input("Usuario que va a meter en la mochila?:")
  units = int(input(f"Cuentas unidades del item {item} vas a meter en la mochila"))
  units = min(50-total_add, total_add)
#validando que si el item se repite entonces sumarlo en vez de crear uno nuevo
  if item in bp_items:
    idx = bp_items.index(item)
    backpack_units[idx] += bp_units[idx]+ units
  else:
    bp_items.append(item)
    bp_units.append(0)
    last_value = len(bp_units)-1
    bp_units[last_value] = units
  
  return units

def use_from_backpack (bp_items, bp_units):
  item = input("Usuario que vas a usar de la mochila?")
  units = int(input(f"Usuario, cuanto vas a usar de {item}:"))
  
  if item in bp_items:
    print ("Obtenido")
    idx = bp_items.index(item)
    units = min(bp_units[idx], units)
    bp_units[idx] = bp_units[idx] - units
  else:
    print (f"no tienes unidades de {item}")
    units = 0
  return units

def getRandom (a,b):
  return a, b

backpack_items =[]
backpack_units =[]

# for i in range(0,5):
#   print (i)
#   add_to_backpack (backpack_items, backpack_units)
#   print (backpack_items)
#   print (backpack_units)

do_next = True
i = 0
units_added = 0 
while i < 3 and do_next:
  i +=1
  units_added = units_added + add_to_backpack(backpack_items, backpack_units)
  print (backpack_items)
  print (backpack_units)
  if (units_added >= 50):
    do_next = False
  else:
    r = int(input("Deseas agregar mas cosas?\
      \n 0.SI \
      \n1.N0 \
      \n Respuesta:"))
  
  if(r == 1):
    do_next = False
  
units_to_use = use_from_backpack(backpack_items, backpack_units)
print (backpack_items)
print (backpack_units)
print (f"Usaste {units_to_use} de {backpack_items}")

# Hacer una batalla contra un enemigo. El enemigo es de tipo agua, fuego, aire o tierra 
# y cuenta con una vida en cada uno
# el usuario agregar hasta 3 elementos a su mochila
# cada uso, va a decidir cuanto usar de cada cosa, si su inventario se acaba antes de quitarle toda la vida
# al enemigo, entonces, pierde. 
# EN caso contrario gana. El enemigo cuenta con una vida aleatoria entre 10 y 30, el usuario 
# puede meter máximo 20 de cada elemento en su mochila, pero con un máximo de 50. 
# Ver sig tabla:
"""
    A F W E 
A   T M 0 M
F   M T M 0 
W   0 M T M
E   M 0 M T
0 -> sin daño
T -> Daño total de la cantidad de unidades
M -> Daño a la mitad de la cantidad de unidades
"""
print ("********************")
print ("****** BATTLE ******")
print ("********************")

types = ["Fuego", "Agua", "Aire", "Tierra"]
enemy_type = types [ get2w]