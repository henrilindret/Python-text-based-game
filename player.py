import weapons


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        self.weapon = weapons.Ironsword
        self.attack = self.weapon.attack
