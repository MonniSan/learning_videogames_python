"""
En un juego, el usuario entrega su magia por vida. 
Si la magia es menor a 5 la vida es 5. 
Si la magia esta entre 5 y 20 la vida es igual a 5 más la magia 
Si la magia es mayor a 20 la vida es de 20 
"""

print ("Vamos a calcular la vida que tienes por medio de tu magia")
magia = int (input ("dame tu magia:"))

vida_base = min(max(5,magia),20) 
vida_sobre = min(20,magia)
vida = max(vida_base,vida_sobre)

"""
Hasta aqui la solución es correcta para una magia abajo de 5 y 
arriba de 20, pero la magia esta entre 5 y 20 se omite sumarle 5 puntos a la vida.

Tambien se puede observar que si un jugador tiene más de 15 pero menos de 20 en su
magia, su vida superara los 20 puntos (21-24) por lo cual se sugiere lo siguiente:
"""

if (5<vida<20):
  vida = min(vida+5, 20)
else:
  vida = vida

print (f"tu vida es de {vida}")
