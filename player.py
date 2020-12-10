import weapons


class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.gold = 50
        self.weapon = weapons.Ironsword
        self.attack = self.weapon.attack
        self.waves = 0


user = Player()
