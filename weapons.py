class Weapon:
    def __init__(self, name, attack, gold, weapon_id):
        self.name = name
        self.attack = attack
        self.gold = gold
        self.weapon_id = weapon_id

Stick = Weapon("Stick", 1, 1, 1)
Dagger = Weapon("Dagger", 3, 2, 2)
Ironsword = Weapon("Iron sword", 5, 5, 3)
Steelsword = Weapon("Steel sword", 10, 10, 4)
Recurve_bow = Weapon("Recurve bow", 10, 15, 5)
Mithrilsword = Weapon("Mithril sword", 15, 25, 6)
Hooked_Spear = Weapon("Hooked spear", 15, 20, 7)


weaponlist = [Ironsword, Steelsword, Mithrilsword, Dagger, Recurve_bow, Hooked_Spear]


#legendary weapons, boss drop only

Titanic_arbalest = Weapon("Titanic arbalest", 35, 175, 8)
Emperors_Sword = Weapon("Emperors Sword", 60, 550, 8)
Dark_Lance = Weapon("Dark Lance", 100, 1000, 9)

lege_weaponlist = [Titanic_arbalest, Emperors_Sword, Dark_Lance]
