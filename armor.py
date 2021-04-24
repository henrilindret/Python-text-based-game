class Armor:
    def __init__(self, name, armor, gold):
        self.name = name
        self.armor = armor
        self.gold = gold



Cloth = Armor("Cloth", 5, 5)
Leather = Armor("Leather", 5, 10)
Iron = Armor("Iron", 10, 25)

armorlist = [Cloth, Leather, Iron]