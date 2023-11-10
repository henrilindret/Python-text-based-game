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


Wolf = Enemy("Wolf", 20, 20, 3, 2, 5, 3,)
Troll = Enemy("Troll", 30, 30, 10, 0, 5, 10,)
Goblin = Enemy("Goblin", 10, 10, 2, 1, 5, 2,)
HobGoblin = Enemy("HobGoblin", 25, 25, 5, 3, 6, 6,)


forestenemylist = [Wolf, Troll, Goblin, HobGoblin]



#Forest_Fairy = Enemy("Forest Fairy", 10, 10, 5, 1, 15)
#Ork = Enemy("Ork", 30, 30, 15, 5, 50)
#Hollow_Man = Enemy("Hollow Man", 30, 30, 5, 5, 40)
#Lankbeast = Enemy("Lankbeast",50 , 50, 10, 10, 70)
