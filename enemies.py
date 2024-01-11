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
troll = Enemy("Troll", 30, 30, 10, 0, 5, 10)
goblin = Enemy("Goblin", 10, 10, 2, 1, 5, 2)
hobgoblin = Enemy("HobGoblin", 25, 25, 10, 3, 6, 6)
forest_fairy = Enemy("Forest Fairy", 10, 10, 15, 1, 5, 5)
maantin = Enemy("Maantin", 30, 30, 25, 10, 15, 20)

forestenemylist = [wolf, troll, goblin, hobgoblin, forest_fairy, maantin]



        
    
