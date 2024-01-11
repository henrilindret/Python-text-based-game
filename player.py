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
        self.armor = armor.Cloth
        self.armorsave = self.armor.armorsave
        self.waves = 0
        self.rest = 0
        self.level = 0
        self.exp = 0
        self.zone = ""
        

    
    def Attackdamage(self):
        return self.basedamage + self.weapondamage + self.talent.attack
    
    def Armorvalue(self):
        return self.armorsave + self.talent.armorsum
    

    

class Talent:
    def __init__(self, name, attack, maxhealth, health, armorsum, mana, manatalent, levelup):
        self.name = name
        self.attack = attack
        self.maxhealth = maxhealth
        self.health = health
        self.armorsum = armorsum
        self.mana = mana
        self.manatalent = manatalent
        self.levelup = levelup


talents = {
    "Warrior": Talent("Warrior", attack=4, maxhealth=110, health=110, armorsum=6, mana=50, manatalent=1, levelup={"maxhealth": 30, "basedamage": 3}),
    "Paladin": Talent("Paladin", attack=2, maxhealth=150, health=150, armorsum=4, mana=100, manatalent=2, levelup={"maxhealth": 40, "basedamage": 2}),
    "Normal": Talent("Normal", attack=0, maxhealth=100, health=100, armorsum=2, mana=100, manatalent=1, levelup={"maxhealth": 20, "basedamage": 2}),
}

    




user = Player()

