class Enemy:
    def __init__(self, name, health, maxhealth, attack, gold):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
        self.gold = gold


Goblin = Enemy("Goblin", 20, 20, 2, 50)
Zombie = Enemy("Zombie", 20, 20, 2, 30)


enemylist1 = [Goblin, Zombie]
