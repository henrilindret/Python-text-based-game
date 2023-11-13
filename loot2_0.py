import random


class Loot:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
        
        
class Weapon:
    def __init__(self, name, attack, gold, id):
        self.name = name
        self.attack = attack
        self.gold = gold
        self.id = id
        
        
class Armor:
    def __init__(self, name, armor, gold, id):
        self.name = name
        self.armor = armor
        self.gold = gold
        self.id = id     
        
class Misc:
    def __init__(self, name, gold, id):
        self.name = name
        self.gold = gold
        self.id = id

class Zoneloot:
    def __init__(self):
        self.feral_forest_loot = [Popes_garms, Holy]
        self.dune_desert_loot = [Quicksilver_shade, Dark_Lance, Hooked_Spear]
        self.lankland_loot = [Shadow, Mithrilsword, Dragonscale_armor]
        self.maatincity_loot = [Emperors_Sword]
        



Stick = Weapon("Stick", 2, 1, 1) 
Dagger = Weapon("Dagger", 3, 2, 2)  
Ironsword = Weapon("Iron sword", 5, 5, 3)  
Steelsword = Weapon("Steel sword", 10, 10, 4)  
Recurve_bow = Weapon("Recurve bow", 10, 15, 5) 
Mithrilsword = Weapon("Mithril sword", 15, 25, 6)  
Hooked_Spear = Weapon("Hooked spear", 15, 20, 7)

Titanic_arbalest = Weapon("Titanic arbalest", 35, 175, 8)  
Emperors_Sword = Weapon("Emperors Sword", 60, 550, 9)  
Dark_Lance = Weapon("Dark Lance", 100, 1000, 10)  


Cloth = Armor("Cloth armor", 2, 2, 11)
Leather = Armor("Leather armor", 4, 4, 12)
Iron = Armor("Iron armor", 10, 24, 13)
Holy = Armor("Holy armor", 20, 74, 14)
Shadow = Armor("Shadow armor",24, 100, 15)

Dragonscale_armor = Armor("Dragonscale armor", 34, 150, 16)
Quicksilver_shade = Armor("Quicksilver shade", 40, 250, 17)
Popes_garms = Armor("Pope's garms", 50, 450, 18)

        
    
    





zoneloot = Zoneloot()

zoneloot.feral_forest_loot = [Popes_garms, Holy]



def newloot():
    loot_value = random.randint(1,100)
    if loot_value <= 5:
        loot = zone_loot_gen
    else:
        loot = enemy_loot_gen




loot1 = random.randint(1,100)
if loot1 >= 50:
    newloot()


    
    
    
        








#Health_potion = Misc(150, )
#Xp_potion = Misc(150, )
#Revive_elixir = Misc(1500, )