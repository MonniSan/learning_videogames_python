from os import system

"""
hacer un juego de narrativa interactiva, el usario responde 
hacia donde quiere ir. El programa debera presentar una 
historia, debe tener 4 finales, con al menos 2 descisiones. 
"""
system ("clear")

print ("Bienvenido al juego de friendzone. Eligue a la chica a conquistar")

chica = int(input("Eligue la chica [0.Maria 1.Ana]:"))
if chica==1:
  print (f"Elegiste a la mas guapa, ahora elige la frase para ligar")
  frase = int(input("Eligue la frase [0.Hola guapa 1.¿Que hora es?]:"))
  if frase==1:
    print ("Ana habla contigo y tienen una noche loca")
  else:
    print ("Ana te ignora y te deja en la Friendzone")
else:
  print (f"Elegiste a la mas divertida, ahora elige la frase para ligar")
  frase = int(input("Eligue la frase [0.Hola guapa 1.¿Que hora es?]:"))
  if frase==1:
    print ("Maria te ignora y te da mal la hora, nunca vuelves a saber de ella")
  else:
    print ("Maria y tu tienen una excelente conversacion y en 3 años se casan")