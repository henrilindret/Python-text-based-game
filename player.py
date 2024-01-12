import weapons
import armor


class Player:
    def __init__(self):
        self.name = ""
        self.talent = talents["Normal"]
        self.maxhealth = self.talent.maxhealth
        self.health = self.talent.health
        self.gold = 0
        self.weapon = weapons.Fist
        self.weapondamage = self.weapon.attack
        self.basedamage = 3
        self.armor = armor.Naked
        self.armorsave = self.armor.armorsave
        self.waves = 0
        self.rest = 0
        self.level = 0
        self.exp = 0
        self.zone = ""
        self.kills = 0
        self.bosskills = 0
        

    
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
    "Warrior": Talent("Warrior", attack=4, maxhealth=45, health=45, armorsum=6, mana=50, manatalent=1, levelup={"maxhealth": 30, "basedamage": 3}),
    "Paladin": Talent("Paladin", attack=2, maxhealth=50, health=50, armorsum=4, mana=100, manatalent=2, levelup={"maxhealth": 40, "basedamage": 2}),
    "Normal": Talent("Normal", attack=0, maxhealth=40, health=40, armorsum=2, mana=100, manatalent=1, levelup={"maxhealth": 20, "basedamage": 2}),
}

    




user = Player()

