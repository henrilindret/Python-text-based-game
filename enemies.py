import random
import weapons
import armor


class Enemy:
    def __init__(self, name, health, maxhealth, attack, armor, gold, xp):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
        self.armor = armor
        self.gold = gold
        self.xp = xp

def Attackdamage(self):
        return self.attack

wolf = Enemy("Wolf", 20, 20, 4, 5, 5, 3)
troll = Enemy("Troll", 40, 40, 8, 10, 5, 10)
goblin = Enemy("Goblin", 20, 20, 3, 8, 5, 2)
hobgoblin = Enemy("HobGoblin", 35, 35, 5, 12, 6, 6)
forest_fairy = Enemy("Forest Fairy", 18, 18, 5, 3, 5, 5)
kneecrawler = Enemy("Kneecrawler", 100, 100, 35, 25, 25, 35)
maantin = Enemy("Maantin", 35, 35, 20, 20, 15, 10)
husk = Enemy("Husk", 25, 25, 12, 15, 5, 3)
skeleton = Enemy("Skeleton", 20, 20, 10, 5, 5, 3)
scarab = Enemy("Scarab", 15, 15, 9, 5, 5, 5)
repeater = Enemy("Repeater", 20, 20, 30, 8, 8, 5)
sanddevil = Enemy("Sanddevil", 55, 55, 3, 15, 8, 10)
soulmauler = Enemy("Soulmauler", 100, 100, 35, 20, 25, 35)

forestenemylist = [wolf, troll, goblin, hobgoblin, forest_fairy]
desertenemylist = [husk, skeleton, scarab, repeater, sanddevil]

forestbosslist = [kneecrawler]
desertbosslist = [soulmauler]



        
    
