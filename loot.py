import enemies
import random
import weapons
import armor
import player

Stick = weapons.Weapon("Stick", 2, 1, 1, 80) 
Dagger = weapons.Weapon("Dagger", 3, 2, 2, 80)  
Ironsword = weapons.Weapon("Iron sword", 5, 5, 3, 80)  
Steelsword = weapons.Weapon("Steel sword", 10, 10, 4, 60)  
Recurve_bow = weapons.Weapon("Recurve bow", 10, 15, 5, 60) 
Mithrilsword = weapons.Weapon("Mithril sword", 15, 25, 6, 30)  
Hooked_Spear = weapons.Weapon("Hooked spear", 15, 20, 7, 30)
Cloth = armor.Armor("Cloth armor", 5, 5, 1, 80)
Leather = armor.Armor("Leather armor", 5, 10, 2, 80)
Iron = armor.Armor("Iron armor", 10, 25, 3, 60) 
Holy = armor.Armor("Holy armor", 20, 75, 4, 30) 
Shadow = armor.Armor("Shadow armor",25, 100, 5, 30)  


common_lootlist = [Stick, Dagger, Recurve_bow, Cloth, Leather]
rare_lootlist = [Ironsword, Steelsword, Iron]
epic_lootlist = [Mithrilsword, Hooked_Spear, Holy, Shadow]



Titanic_arbalest = weapons.Weapon("Titanic arbalest", 35, 175, 8, 1)  
Emperors_Sword = weapons.Weapon("Emperors Sword", 60, 550, 9, 1)  
Dark_Lance = weapons.Weapon("Dark Lance", 100, 1000, 10, 1)
Dragonscale_armor = armor.Armor("Dragonscale armor", 35, 150, 6, 5)  
Quicksilver_shade = armor.Armor("Quicksilver shade", 40, 250, 7, 5)  
Popes_garms = armor.Armor("Pope's garms", 50, 450, 8, 5)  

lege_lootlist = [Titanic_arbalest, Emperors_Sword, Dark_Lance, Dragonscale_armor, Quicksilver_shade, Popes_garms]


def random_drop_gen():
    rand_num = random.randint(1,100)
    
    if rand_num <= 10:                  #10% drop chance
        return random.choice(common_lootlist)  
    elif rand_num <= 16:                #6% drop chance
        return random.choice(rare_lootlist)
    elif rand_num <= 19:                #3% drop chance
        return random.choice(epic_lootlist)
    elif rand_num <= 1:                #1% drop chance
        return random.choice(lege_lootlist)
    else:
        return None                     #80% chance for no drop
       
lootdrop = random_drop_gen()


def gold_drop_gen():
    return random.randint(1,15)

gold_drop = gold_drop_gen()


if lootdrop:
    print(f"You found an {lootdrop.name}!")
    input()
    
    if isinstance(lootdrop, weapons.Weapon):
        if lootdrop in weapons.lege_weaponlist:
            print(f"You have found a Legendary {lootdrop.name}!")
            print(f"You currently have a {player.user.weapon}, would you like too equip the new weapon?")
        else:
            print(f"You currently have a {player.user.weapon}, would you like to equip the new weapon?")
            
    elif isinstance(lootdrop, armor.Armor):
        if lootdrop in armor.lege_armorlist:
            print(f"You have found a Legendary {lootdrop.name}!")
            print(f"You currently have a {player.user.armor}, would you like too equip the new armor?")
        else:
            print(f"You currently have a {player.user.armor}, would you like to equip the new armor?")
            
    else:
        print("This is not a recognized item type.")
        
    print("1.) Equip")
    print("2.) Discard")
    
    choice = input()
    if choice == "1":
        if isinstance(lootdrop, weapons.Weapon):
            player.user.weapon = lootdrop
            print(f"You have equipped the {lootdrop.name}!")
        elif isinstance(lootdrop, armor.Armor):
            player.user.armor = lootdrop
            print(f"You have equipped the {lootdrop.name}!")
    else:
        print("You have discarded the item.")
        
        
