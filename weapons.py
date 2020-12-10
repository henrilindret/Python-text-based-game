class Weapon:
    def __init__(self, name, attack, gold, weapon_id):
        self.name = name
        self.attack = attack
        self.gold = gold
        self.weapon_id = weapon_id


Ironsword = Weapon("Iron sword", 5, 5, 1)
Steelsword = Weapon("Steel sword", 10, 10, 2)
Mithrilsword = Weapon("Mithril sword", 15, 25, 3)

weaponlist = [Ironsword, Steelsword, Mithrilsword]
