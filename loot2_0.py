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
        



Loot.lootstick = Stick = Weapon("Stick", 2, 1, 1) 
Loot.lootdagger = Dagger = Weapon("Dagger", 3, 2, 2)  
Loot.lootironsword = Ironsword = Weapon("Iron sword", 5, 5, 3)  
Loot.lootsteelsword =Steelsword = Weapon("Steel sword", 10, 10, 4)  
Loot.recurvebow = Recurve_bow = Weapon("Recurve bow", 10, 15, 5) 
Loot.mithrilsword = Mithrilsword = Weapon("Mithril sword", 15, 25, 6)  
Loot.hookedsepar = Hooked_Spear = Weapon("Hooked spear", 15, 20, 7)

Loot.titanicarbalest = Titanic_arbalest = Weapon("Titanic arbalest", 35, 175, 8)  
Loot.emperorssword = Emperors_Sword = Weapon("Emperors Sword", 60, 550, 9)  
Loot.darklance = Dark_Lance = Weapon("Dark Lance", 100, 1000, 10)  


Loot.cloth = Cloth = Armor("Cloth armor", 2, 2, 11)
Loot.leather = Leather = Armor("Leather armor", 4, 4, 12)
Loot.iron = Iron = Armor("Iron armor", 10, 24, 13)
Loot.holy = Holy = Armor("Holy armor", 20, 74, 14)
Loot.shadow = Shadow = Armor("Shadow armor",24, 100, 15)

Loot.drgagonscale = Dragonscale_armor = Armor("Dragonscale armor", 34, 150, 16)
Loot.quicksilver = Quicksilver_shade = Armor("Quicksilver shade", 40, 250, 17)
Loot.popes = Popes_garms = Armor("Pope's garms", 50, 450, 18)

        
    
    




zone_loot = Zoneloot()

Zoneloot.feral_forest_loot = [Popes_garms, Holy]


    
    
    
def newloot():
    loot_chance = random.randint(1,100)
    if loot_chance <= 15:
        print(" You found")
        input()
        
    elif loot_chance >= 16:
        print("you found loot")
        input()
    
    

if_loot = random.randint(1,100)
if if_loot >= 50:
    newloot()
else:
    print("You found nothing of value, press any key to continue")
    input()


    
    
    
        








#Health_potion = Misc(150, )
#Xp_potion = Misc(150, )
#Revive_elixir = Misc(1500, )