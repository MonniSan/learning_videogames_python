# Utilizar objetos mientras el usuario quiera
# Validar que los objetos no se puedan agregar
"""
a-1
a-2
a-3
Mala lista 
[a,a,a]
[1,2,3]
deberia quedar
[a]
[6]
"""

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


