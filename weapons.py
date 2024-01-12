import random
import armor
class Weapon:
    def __init__(self, name, attack, gold, weapon_id, drop_chance):
        self.name = name
        self.attack = attack
        self.gold = gold
        self.weapon_id = weapon_id
        self.drop_chance = drop_chance
        
        

Fist = Weapon("Scrawny fists", 1, 0, 8, 0)
Stick = Weapon("Stick", 3, 5, 1, 80) 
Dagger = Weapon("Dagger", 5, 15, 2, 80)
Jürioda = Weapon("Jürioda", 7, 25, 3, 80)
Ironsword = Weapon("Iron sword", 12, 35, 4, 80)  
Steelsword = Weapon("Steel sword", 15, 45, 5, 60)  
Recurve_bow = Weapon("Recurve bow", 13, 45, 6, 60) 
Mithrilsword = Weapon("Mithril sword", 18, 50, 7, 30)  
Hooked_Spear = Weapon("Hooked spear", 25, 65, 8, 30)  


weaponlist = [Stick, Dagger, Jürioda, Ironsword, Steelsword, Recurve_bow, Mithrilsword]




Titanic_arbalest = Weapon("Titanic arbalest", 35, 175, 9, 1)  
Emperors_Sword = Weapon("Emperors Sword", 60, 550, 10, 1)  
Dark_Lance = Weapon("Dark Lance", 100, 1000, 11, 1)  

lege_weaponlist = [Titanic_arbalest, Emperors_Sword, Dark_Lance]


