class Armor:
    def __init__(self, name, armorsave, gold, armor_id, drop_chance):
        self.name = name
        self.armorsave = armorsave
        self.gold = gold
        self.armor_id = armor_id
        self.drop_chance = drop_chance



Naked = Armor("Raw skin", 1, 0, 6, 0)  #common
Cloth = Armor("Cloth armor", 2, 10, 1, 80)  #common
Leather = Armor("Leather armor", 4, 20, 2, 80)  #common
Iron = Armor("Iron armor", 10, 35, 3, 60)  #rare
Holy = Armor("Holy armor", 20, 80, 4, 30)  #epic
Shadow = Armor("Shadow armor",24, 100, 5, 30)  #epic

armorlist = [Cloth, Leather, Iron, Holy, Shadow]


#legendary armor, boss drop only

Dragonscale_armor = Armor("Dragonscale armor", 34, 150, 6, 5)  #legendary
Quicksilver_shade = Armor("Quicksilver shade", 40, 250, 7, 5)  #legendary
Popes_garms = Armor("Pope's garms", 50, 450, 8, 5)  #legendary

lege_armorlist = [Dragonscale_armor, Quicksilver_shade, Popes_garms]
