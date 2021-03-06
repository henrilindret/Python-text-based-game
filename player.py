import weapons
import armor


class Player:
    def __init__(self):
        self.name = ""
        self.talent = talents["Normal"]
        self.maxhealth = self.talent.maxhealth
        self.health = self.talent.health
        self.gold = 0
        self.weapon = weapons.Ironsword
        self.weapondamage = self.weapon.attack
        self.basedamage = 3
        self.armor = armor.Cloth.armor
        self.waves = 0
    
    def Attackdamage(self):
        return self.basedamage + self.weapondamage + self.talent.attack



class Talent:
    def __init__(self, name, attack, maxhealth, health):
        self.name = name
        self.attack = attack
        self.maxhealth = maxhealth
        self.health = health

talents = {
"Warrior" : Talent("Warrior", attack = 2, maxhealth = 110, health = 110),
"Paladin" : Talent("Paladin", attack = 1, maxhealth= 150, health = 150),
"Normal" : Talent("Normal", attack = 0, maxhealth = 100, health = 100)
}


    





user = Player()

