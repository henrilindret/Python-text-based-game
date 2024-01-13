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
        self.xp = 95
        self.maxp = 100
        self.level = 1
        self.zone = ""
        self.kills = 0
        self.bosskills = 0
        self.revive = 0
        self.merchantpay = 0
        

    
    def Attackdamage(self):
        return self.basedamage + self.weapondamage + self.talent.attack
    
    def Armorvalue(self):
        return self.armorsave + self.talent.armorsum
    

    

class Talent:
    def __init__(self, name, attack, maxhealth, health, armorsum, mana, manatalent):
        self.name = name
        self.attack = attack
        self.maxhealth = maxhealth
        self.health = health
        self.armorsum = armorsum
        self.mana = mana
        self.manatalent = manatalent


talents = {
    "Warrior": Talent("Warrior", attack=4, maxhealth=45, health=45, armorsum=6, mana=50, manatalent=1),
    "Paladin": Talent("Paladin", attack=2, maxhealth=50, health=50, armorsum=4, mana=100, manatalent=2),
    "Normal": Talent("Normal", attack=0, maxhealth=40, health=40, armorsum=2, mana=100, manatalent=1),
}

    




user = Player()

