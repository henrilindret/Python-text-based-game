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
troll = Enemy("Troll", 30, 30, 8, 10, 5, 10)
goblin = Enemy("Goblin", 15, 15, 3, 8, 5, 2)
hobgoblin = Enemy("HobGoblin", 30, 30, 5, 12, 6, 6)
forest_fairy = Enemy("Forest Fairy", 15, 15, 5, 3, 5, 5)
maantin = Enemy("Maantin", 35, 35, 20, 20, 15, 10)
kneecrawler = Enemy("Kneecrawler", 100, 100, 30, 25, 25, 35)

forestenemylist = [wolf, troll, goblin, hobgoblin, forest_fairy]
forestbosslist = [kneecrawler]


husk = Enemy("Husk", 25, 25, 12, 15, 5, 3)
skeleton = Enemy("Skeleton", 20, 20, 10, 5, 5, 3)
scarab = Enemy("Scarab", 15, 15, 9, 5, 5, 5)
shrieker = Enemy("Shrieker", 15, 15, 9, 5, 5, 5)
repeater = Enemy("Repeater", 20, 20, 30, 8, 8, 10)
sanddevil = Enemy("Sanddevil", 55, 55, 3, 15, 8, 15)
soulmauler = Enemy("Soulmauler", 150, 150, 40, 30, 25, 55)

desertenemylist = [husk, skeleton, scarab, repeater, sanddevil]
desertbosslist = [soulmauler]


lank = Enemy("Lank", 45, 45, 9, 5, 10, 5)
lanker = Enemy("Lanker", 55, 55, 9, 5, 10, 10)
lankbeast = Enemy("Lankbeast", 60, 60, 9, 15, 5, 10)
lankton = Enemy("Lankton", 35, 35, 9, 10, 5, 15)
lankraper = Enemy("Lankraper", 80, 80, 9, 25, 5, 15)
lanktitan = Enemy("Lanktitan", 100, 100, 9, 30, 5, 25)
lanklord = Enemy("Lanklord", 200, 200, 55, 40, 5, 75)

lankenemylist =[lank, lanker, lankbeast, lankton, lankraper, lanktitan]
lankbosslist = [lanklord]





        
    
