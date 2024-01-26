import weapons
import armor
import random


class Player:
    def __init__(self):
        self.name = ""
        self.talent = normal
        self.maxhealth = self.talent.maxhealth
        self.health = self.talent.health
        self.gold = 15000
        self.weapon = weapons.Fist
        self.weapondamage = self.weapon.attack
        self.magicdamage = 0
        self.basedamage = 0
        self.armor = armor.Naked
        self.armorsave = self.armor.armorsave
        self.mana = self.talent.mana
        self.maxmana = self.talent.maxmana
        self.basearmor = 0
        self.waves = 0
        self.rest = 0
        self.level = 1
        self.spelllevel = self.talent.magiclevel
        self.xp = 0
        self.maxp = 100
        self.zone = ""
        self.kills = 0
        self.bosskills = 0
        self.revive = 0
        self.merchantpay = 0
        self.spelllist = self.talent.known_spells
        
    def Attackdamage(self):
        return self.basedamage + self.weapondamage + self.talent.attack
    
    def Armorvalue(self):
        return self.basearmor + self.armorsave + self.talent.armorsum
    
    def Magicattackdamage(self):
        return self.magicdamage + self.talent.magicattack + self.basedamage
    
    def Magicarmorvalue(self):
        return self.armorsave + self.talent.armorsum + self.basearmor
    
    
class Talent:
    def __init__(self, name, attack, magicattack, health, maxhealth, armorsum, mana, maxmana, magiclevel, lvlupattack, lvluparmor, lvluphealth,):
        self.name = name
        self.attack = attack
        self.magicattack = magicattack
        self.health = health
        self.maxhealth = maxhealth
        self.armorsum = armorsum
        self.mana = mana
        self.maxmana = maxmana
        self.magiclevel = magiclevel
        self.lvlupattack = lvlupattack
        self.lvluparmor = lvluparmor
        self.lvluphealth = lvluphealth
        self.known_spells = []



warrior = Talent("Warrior", 4, 0, 45, 45, 6, 100, 100, 1, random.randint(3,5), random.randint(1,3), random.randint(5,10))
paladin = Talent("Paladin", 2, 5, 50, 50, 4, 150, 150, 2, random.randint(1,3), random.randint(2,5), random.randint(5,10))
assassin = Talent("Assassin", 10, 2, 25, 25, 2, 100, 100, 1, random.randint(4,8), random.randint(1,2), random.randint(1,5))
normal = Talent("Normal", 0, 2, 40, 40, 2, 150, 150, 1, random.randint(3,5), random.randint(1,3), random.randint(5,10))

    
    

user = Player()



    



