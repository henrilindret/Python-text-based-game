class Enemy:
    def __init__(self, name, health, maxhealth, attack, gold):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
        self.gold = gold


    def Attackdamage(self):
        return self.attack


Goblin = Enemy("Goblin", 20, 20, 10, 5)
Zombie = Enemy("Zombie", 20, 20, 10, 5)


enemylist1 = [Goblin, Zombie]
