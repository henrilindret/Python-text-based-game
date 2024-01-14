import weapons
import armor
import random


class Player:
    def __init__(self):
        self.name = ""
        self.talent = normal
        self.maxhealth = self.talent.maxhealth
        self.health = self.talent.health
        self.gold = 0
        self.weapon = weapons.Fist
        self.weapondamage = self.weapon.attack
        self.basedamage = 0
        self.armor = armor.Naked
        self.armorsave = self.armor.armorsave
        self.basearmor = 0
        self.waves = 0
        self.rest = 0
        self.level = 0
        self.xp = 0
        self.maxp = 100
        self.zone = ""
        self.kills = 0
        self.bosskills = 0
        self.revive = 0
        self.merchantpay = 0
        
    def Attackdamage(self):
        return self.basedamage + self.weapondamage + self.talent.attack
    
    def Armorvalue(self):
        return self.basearmor + self.armorsave + self.talent.armorsum
    
    
class Talent:
    def __init__(self, name, attack, health, maxhealth, armorsum, mana, manatalent, lvlupattack, lvluparmor, lvluphealth):
        self.name = name
        self.attack = attack
        self.health = health
        self.maxhealth = maxhealth
        self.armorsum = armorsum
        self.mana = mana
        self.manatalent = manatalent
        self.lvlupattack = lvlupattack
        self.lvluparmor = lvluparmor
        self.lvluphealth = lvluphealth



warrior = Talent("Warrior", 4, 45, 45, 6, 50, 1, random.randint(3,5), random.randint(1,3), random.randint(5,10))
paladin = Talent("Paladin", 2, 50, 50, 4, 100, 2, random.randint(1,3), random.randint(2,5), random.randint(5,10))
assassin = Talent("Assassin", 10, 25, 25, 2, 50, 1, random.randint(4,8), random.randint(1,2), random.randint(1,5))
normal = Talent("Normal", 0, 40, 40, 2, 100, 1, random.randint(3,5), random.randint(1,3), random.randint(5,10))

    
    

user = Player()



    



