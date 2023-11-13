import random
import weapons
import armor

class Enemy:
    def __init__(self, name, health, maxhealth, attack, armor, gold, exp):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
        self.armor = armor
        self.gold = gold
        self.exp = exp

def Attackdamage(self):
        return self.attack

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
    
