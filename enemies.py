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

wolf = Enemy("Wolf", 20, 20, 5, 2, 5, 3)
troll = Enemy("Troll", 30, 30, 10, 5, 5, 10)
goblin = Enemy("Goblin", 15, 15, 4, 3, 5, 2)
hobgoblin = Enemy("HobGoblin", 25, 25, 7, 10, 6, 6)
forest_fairy = Enemy("Forest Fairy", 10, 10, 3, 1, 5, 5)
kneecrawler = Enemy("Kneecrawler", 100, 100, 35, 25, 25, 10)
maantin = Enemy("Maantin", 30, 30, 25, 15, 15, 20)
husk = Enemy("Husk", 20, 20, 10, 10, 5, 3)
skeleton = Enemy("Skeleton", 15, 15, 10, 1, 5, 3)
scarab = Enemy("Scarab", 10, 10, 5, 1, 5, 5)
repeater = Enemy("Repeater", 20, 20, 25, 5, 8, 5)
sanddevil = Enemy("Sanddevil", 50, 30, 3, 10, 8, 10)
soulmauler = Enemy("Soulmauler", 100, 100, 35, 20, 25, 10)

forestenemylist = [wolf, troll, goblin, hobgoblin, forest_fairy]
desertenemylist = [husk, skeleton, scarab, repeater, sanddevil]

forestbosslist = [kneecrawler]
desertbosslist = [soulmauler]



        
    
