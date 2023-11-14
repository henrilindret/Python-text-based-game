import random
import weapons
import armor

class Enemy:
    def __init__(self, name, health, maxhealth, attack, armor, gold, exp, loot, loot_chance):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
        self.armor = armor
        self.gold = gold
        self.exp = exp
        self.loot = loot
        self.loot_chance = loot_chance

    def Attackdamage(self):
        return self.attack

    def drop_loot(self):
        return random.choices(self.loot, weights=self.loot_chance, k=1)[0]

wolf_loot =[weapons.Dagger, weapons.Ironsword]
wolf_loot_chance = [0.40, 0.60]

troll_loot =[armor.cloth, armor.Leather, weapons.Hooked_Spear]
troll_loot_chance =[0.80, 0.19, 0.01]

goblin_loot =[weapons.Stick, weapons.Dagger, weapons.Ironsword, armor.Cloth]
goblin_loot_chance =[0.4, 0.4, 0.03, 0.17]

hobgoblin_loot =[weapons.Steelsword, armor.Cloth, armor.Leather, armor.Holy]
hobgoblin_loot_chance =[0.09, 0.55, 0.35, 0.01]

forest_fairy_loot =[weapons.Dagger, armor.Quicksilver_shade]
fores_fairy_loot_chance = [0.999, 0.001]

husk_loot =[weapons.Ironsword, armor.Leather, armor.Cloth, weapons.Dagger]
husk_loot_chance =[0.15, 0.25, 0.35, 0.25]

skeleton_loot =[weapons.Recurve_bow, armor.Leather, weapons.Titanic_arbalest]
skeleton_loot_chance =[0.55, 0.449, 0.001]

scarab_loot =[weapons.Hooked_Spear, weapons.Dagger, armor.Leather]
scarab_loot_chance =[0.05, 0.65, 0.3]

repeater_loot =[weapons.Mithrilsword, weapons.Steelsword, weapons.Dark_Lance]
repeater_loot_chance = [0.20, 0.799, 0.001]

sanddevil_loot =[armor.Leather, armor.Dragonscale_armor]
sanddevil_loot_chance =[0.99, 0.01]

lank_loot =[armor.cloth, weapons.Dagger, weapons.Stick, weapons.Emperors_Sword]
lank_loot_chance =[0.499, 0.25, 0.25, 0.001]

lankbeast_loot =[armor.iron, armor.Shadow, weapons.Mithrilsword, armor.Dragonscale_armor]
lankbeast_loot_chance =[0.45, 0.35, 0.19, 0.01]

lanklord_loot =[armor.Popes_garms, weapons.Emperors_Sword, weapons.Hooked_Spear, armor.iron]
lanklord_loot_chance = [0.03, 0.02, 0.60, 0.35]

lanker_loot =[weapons.Dagger, armor.Leather, weapons.Hooked_Spear]
lanker_loot_chance =[0.5, 0.45, 0.05]

lank_centurion_loot =[armor.iron, armor.holy, armor.Dragonscale_armor]
lank_centurion_loot_chance =[0.8, 0.15, 0.05]

maat_loot =[armor.Leather, weapons.Dagger]
maat_loot_chance =[0.35, 0.65]

maatincarrier_loot =[weapons.Dark_Lance, weapons.Emperors_Sword, armor.Popes_garms, armor.iron, weapons.Ironsword]
maatincarrier_loot_chance =[0.05, 0.05, 0.05, 0.4, 0.45]

maatincenturion_loot =[armor.Holy, armor.Shadow, armor.Iron]
maatincenturion_loot_chance =[0.1, 0.1, 0.8]

maatinwilder_loot =[weapons.Dark_Lance, weapons.Recurve_bow, weapons.Dagger]
maatinwilder_loot_chance =[0.01, 0.49, 0.5]

maatbeast_loot =[armor.Leather, armor.Iron, armor.Shadow, armor.Quicksilver_shade]
maatbeast_loot_chance =[0.6, 0.2, 0.15, 0.05]


wolf = Enemy("Wolf", 20, 20, 3, 2, 5, 3)
troll = Enemy("Troll", 30, 30, 10, 0, 5, 10)
goblin = Enemy("Goblin", 10, 10, 2, 1, 5, 2)
hobgoblin = Enemy("HobGoblin", 25, 25, 5, 3, 6, 6)
forest_fairy = Enemy("Forest Fairy", 10, 10, 5, 1, 5, 5)
husk = Enemy("Husk", 25, 25, 3, 2, 5, 3)
skeleton = Enemy("Skeleton", 15, 15, 4, 1, 5, 3)
scarab = Enemy("Scarab", 10, 10, 3, 1, 5, 5)
repeater = Enemy("Repeater", 30, 30, 5, 3, 8, 5)
sanddevil = Enemy("Sanddevil", 30, 30, 10, 5, 8, 10)
lank = Enemy("Lank", 15, 15, 5, 3, 5, 5)
lankbeast = Enemy("Lankbeast", 40, 40, 10, 8, 8, 10)
lanklord = Enemy("Lanklord", 35, 35, 15, 6, 10, 10)
lanker = Enemy("Lanker", 20, 20, 10, 5, 5, 5)
lank_centurion = Enemy("Lank centurion", 35, 35, 10, 10, 5, 5)
maat = Enemy("Maat", 15, 15, 5, 2, 5, 5)
maatincarrier = Enemy("Maatincarrier", 50, 50, 25, 5, 15, 10)
maatincenturion = Enemy("Maatincenturion", 55, 55, 15, 15, 10, 5)
maatinwilder = Enemy("Maatinwilder", 45, 45, 20, 5, 5, 5)
maatbeast = Enemy("Maatbeast", 60, 60, 10, 10, 25, 5)






forestenemylist = [wolf, troll, goblin, hobgoblin, forest_fairy]        #boss: the thing

desertenemylist = [husk, skeleton, scarab, repeater, sanddevil]         #boss: the maul

lankenemylist = [lank, lankbeast, lanklord, lanker, lank_centurion]     #boss: the ronan

maatinenemylist = [maat, maatincarrier, maatincenturion, maatinwilder, maatbeast]    #boss: the maatin    
    
