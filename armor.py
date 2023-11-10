class Armor:
    def __init__(self, name, armor, gold, armor_id):
        self.name = name
        self.armor = armor
        self.gold = gold
        self.armor_id = armor_id



Cloth = Armor("Cloth armor", 5, 5, 1)
Leather = Armor("Leather armor", 5, 10, 2)
Iron = Armor("Iron armor", 10, 25, 3)
Holy = Armor("Holy armor", 20, 75, 4)
Shadow = Armor("Shadow armor",25, 100, 5)

armorlist = [Cloth, Leather, Iron, Holy, Shadow]


#legendary armor, boss drop only

Dragonscale_armor = Armor("DRagonscale armor", 35, 150, 6)
Quicksilver_shade = Armor("Quicksilver shade", 40, 250, 7)
Popes_garms = Armor("Pope's garms", 50, 450, 8)

lege_armorlist = [Dragonscale_armor, Quicksilver_shade, Popes_garms]