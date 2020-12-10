import weapons


class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.gold = 100
        self.weapon = weapons.Ironsword
        self.attack = self.weapon.attack


user = Player()
