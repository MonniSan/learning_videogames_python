# Battle For Middle Earth

Battle for Middle Earth with orcs and elves.

In this program, **Orcs** and **Elves** wiil have to <fight>. Orcs and Elves are **CREATURE**
of a **WORLD** in the Middle Earth. They should be modeled as such. **Trolls** arre around an can <eat> any Creature.

Orcs and Elves start around a world of 100^2 (logically) unit grid in which they can get together and start walking, as a _gurp of creatures_ called **HORD**. Two Creatures can't be occupying the same place at the same time (logically physical), so, when they are <moving>, be careful that the _position_ (x,y) the creature is heading to, doesn't have another creature already. They have a _speed_, too.

To determine if Orcs or Elves can <makeHorde>, the distance between them must be 5. Once they are a Horde, advancing is slower (average of all speds) and the future position must be in fuction of the centriod (x and y of the circule make for all).

If an Orc and an Elf meet in the World, they will start a fight. If 2 hordes meet ech other, one orc will stand against one elf. If there are more creatures on one side, one of the guys on the other side will die. By the developer desition, if the struggle is 2 creatures in favor ore more in one side (3-1,5-2,7-5,6-2,...) the hordes with more creatures kill all. So, only when the difernce of the creatures in a horde is 1 can kill the one with minimum _life_ and strunggle 1-1.

To fight, hech creature has a combination of _strength_ and _magic_ Elves have X2 on magic and orcs have X3 on strength. These specs are determined upon creature birth, and are random according to the following rules:

# Orc

> Stength: 50-140
> Magic: 1-10

# Elf

> Stength: 20-50
> Magic: 60-120

They can be modified if anything of the next events happen:
<OrcFindWeapon> strength +30
<OrcFindAmulet> destroys Amulet
<ElfFindWeapon> stength +10
<ElfFindAmulet> magic +40

> There are at least 4 **ITEMS** of each **Weapons** and **Amulets** randomly put on the World.

In the fights is possible that both creatures die. The damage they receive is according to the following formula:

If {
Damege is done by Orc = 0.7Stength + 0.3Magic
Damage is done by Elf = 0.2Stngth + 0.8Magic
Both cases considering updates of amulets and wapons.
}

The max life of each creature is according to:

> Orc: 1000-2500
> Elf: 1500-2000

There are som special **Healers**, are items that will recover 50% of life. The damage done by a creature to the other creature, unless the find a healer, will not recover. The game will end when there's no more creatures of one side.

Is important to note that when there is a horde, the move is going to be towards the nearest single enemy. When a creature vector each 5 day or when it has found the world is end. If ther are just hordes missing, they will follow the nearest one.

Extra Proyect:
Hordes will chase other hordes and creatures, they want more to find creatures.
The game will continue until all of a type of creature dies.

Nota: Se hara el programa de forma "sucia" para entender mejor lo que pasa, y luego lo factorizare (si puedo)
