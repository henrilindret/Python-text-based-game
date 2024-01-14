import weapons
import armor


class Player:
    def __init__(self):
        self.name = ""
        self.talent = talents["Normal"]
        self.maxhealth = self.talent.maxhealth
        self.health = self.talent.health
        self.gold = 50
        self.weapon = weapons.Ironsword
        self.weapondamage = self.weapon.attack
        self.basedamage = 3
        self.armor = armor.Cloth.armor
        self.waves = 0
        self.rest = 0
        self.level = 1
        self.exp = 0
        self.zone = ""
        

    
    def Attackdamage(self):
        return self.basedamage + self.weapondamage + self.talent.attack
    

    

class Talent:
    def __init__(self, name, attack, maxhealth, health, mana, manatalent, levelup):
        self.name = name
        self.attack = attack
        self.maxhealth = maxhealth
        self.health = health
        self.mana = mana
        self.manatalent = manatalent
        self.levelup = levelup


talents = {
    "Warrior": Talent("Warrior", attack=4, maxhealth=110, health=110, mana=50, manatalent=1, levelup={"maxhealth": 30, "basedamage": 3}),
    "Paladin": Talent("Paladin", attack=2, maxhealth=150, health=150, mana=100, manatalent=2, levelup={"maxhealth": 40, "basedamage": 2}),
    "Normal": Talent("Normal", attack=0, maxhealth=100, health=100, mana=100, manatalent=1, levelup={"maxhealth": 20, "basedamage": 2}),
}

    




user = Player()

