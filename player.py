import weapons
import armor


class Player:
    def __init__(self):
        self.name = ""
        self.talent = ""
        self.maxhealth = 100
        self.health = self.maxhealth
        self.gold = 0
        self.weapon = weapons.Ironsword
        self.attack = self.weapon.attack
        self.armor = armor.Cloth
        self.armor = armor.Cloth.armor
        self.waves = 0
    
class Warrior(Player):
    def __init__(self):
        self.name = "Warrior"
        self.attack = 2
        self.maxhealth = 110
        self.health = self.maxhealth









user = Player()
warrior = Warrior()
