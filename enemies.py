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


Goblin = Enemy("Goblin", 20, 20, 10, 5, 3, 50)
Zombie = Enemy("Zombie", 20, 20, 10, 5, 3, 50)


enemylist1 = [Goblin, Zombie]


Wolf = Enemy("Wolf", 20, 20, 3, 2, 5, 3)
Troll = Enemy("Troll", 30, 30, 10, 0, 5, 10)
Goblin = Enemy("Goblin", 10, 10, 2, 1, 5, 2)
HobGoblin = Enemy("HobGoblin", 25, 25, 5, 3, 6, 6)


forestenemylist = [Wolf, Troll, Goblin, HobGoblin]
