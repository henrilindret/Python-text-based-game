class Armor:
    def __init__(self, name, armor, gold, armor_id):
        self.name = name
        self.armor = armor
        self.gold = gold
        self.armor_id = armor_id

Cloth = Armor("Cloth", 5, 5, 1)
Leather = Armor("Leather", 10, 10, 2)
Iron = Armor("Iron", 15, 25, 3)

armorlist = [Cloth, Leather, Iron]