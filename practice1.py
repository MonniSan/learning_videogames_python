print("Hello Adventurer")
name = input ('How should I call you?: ')
print ("Welcome to the dungeon, " + name + "!")
race = input("What is your race? 1.elf 2.human 3.orc 4.wiz:")
print (f"Thanks for that, {name} of race {race}!")

""" Comentario largo
Config. arma 
Fuerza (fz) Magia (mg) Rupias (rps)
1) espada <10 fz, 20rps> 2) mazo <20 fz, 15rps>
1) fuego <20 mg, 35rps>  2) agua <10mg, 20rps>
1) long <+15fz, 20rps>  2) short <+5fz, 10rps>
"""
rupees = 0
force = 0
magic = 0

weapon_type = int(input("0.Mallet or 1.Sword?"))
rupees = rupees + 15 + 5*weapon_type
weapon_type = 1 - weapon_type
force = force + 10 + 10*weapon_type

magic_type = int(input("0.Water or 1.Fire?"))
rupees = rupees + 20  + 15*magic_type
magic = magic + 10 + 10*magic_type

cooldown_type = int(input("0.Short or 1.Long?"))
rupees = rupees + 10 + 10*cooldown_type
force = force + 5 + 10*cooldown_type