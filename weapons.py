class Weapon:
    def __init__(self, name, attack, gold, weapon_id, drop_chance):
        self.name = name
        self.attack = attack
        self.gold = gold
        self.weapon_id = weapon_id
        self.drop_chance = drop_chance
        
        

Fist = Weapon("Scrawny fists", 1, 0, 8, 0)
Stick = Weapon("Stick", 2, 1, 1, 80) 
Dagger = Weapon("Dagger", 3, 2, 2, 80)
Jürioda = Weapon("Jürioda", 4, 3, 3, 80)
Ironsword = Weapon("Iron sword", 5, 5, 4, 80)  
Steelsword = Weapon("Steel sword", 10, 10, 5, 60)  
Recurve_bow = Weapon("Recurve bow", 10, 15, 6, 60) 
Mithrilsword = Weapon("Mithril sword", 15, 25, 7, 30)  
Hooked_Spear = Weapon("Hooked spear", 15, 20, 8, 30)  


weaponlist = [Stick, Dagger, Jürioda, Ironsword, Steelsword, Recurve_bow, Mithrilsword]




Titanic_arbalest = Weapon("Titanic arbalest", 35, 175, 9, 1)  
Emperors_Sword = Weapon("Emperors Sword", 60, 550, 10, 1)  
Dark_Lance = Weapon("Dark Lance", 100, 1000, 11, 1)  

lege_weaponlist = [Titanic_arbalest, Emperors_Sword, Dark_Lance]


