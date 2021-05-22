"""
En un juego, el usuario entrega su magia por vida. 
Si la magia es menor a 5 la vida es 5. 
Si la magia esta entre 5 y 20 la vida es igual a la magia 
Si la magia es mayor a 20 la vida es de 20 
"""

print ("Vamos a calcular la vida que tienes por medio de tu magia")
magia = int (input ("dame tu magia:"))

vida_base = min(max(5,magia),20) 
vida_sobre = min(20,magia)
vida = max(vida_base,vida_sobre)

print (f"tu vida es de {vida}")
