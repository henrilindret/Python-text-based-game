import weapons
import player
import armor

def shop1():
    print("Welcome to the shop")
    print("You currently have", player.user.gold, "Gold")
    print("Do you wish to check weapons or armor?")
    shoptype = input()
    
    if shoptype == "weapon":
        print("The shop is currently selling")
        for wep in weapons.weaponlist:
            print(wep.weapon_id, wep.name, "cost", wep.gold)
        print("What would you like to buy?")
        print("If you wish to leave, write 5")
        
        try:
            option = int(input())
        except ValueError:
            print("Please enter a valid number")
            input()
            shop1()
        
        for wep in weapons.weaponlist:
            if wep == player.user.weapon and option == wep.weapon_id:
                print("You have already bought this item")
                input("")
                shop1()
            elif wep.weapon_id == option and player.user.gold >= wep.gold:
                print(wep.name + " purchased")
                player.user.gold = player.user.gold - wep.gold
                print("You currently have", player.user.gold, "Gold left")
                player.user.weapon = wep
                player.user.weapondamage = wep.attack
                input("")
                shop1()
            elif wep.weapon_id == option and player.user.gold <= wep.gold:
                print("You do not have enough money to buy the weapon")
                input("")
                shop1()
            elif option == "5":
                return
    
    elif shoptype == "armor":
        print("The shop is currently selling")
        for arm in armor.armorlist:
            print(arm.armor_id, arm.name, "cost", arm.gold)
        print("What would you like to buy?")
        print("If you wish to leave, write 5")
        try:
            option = int(input())
        except ValueError:
            print("Please enter a valid number")
            input()
            shop1()
            return
        
        for arm in armor.armorlist:
            if arm == player.user.armor and option == arm.armor_id:
                print("You have already bought this item")
                input("")
                shop1()
            elif arm.armor_id == option and player.user.gold >= arm.gold:
                print(arm.name + " purchased")
                player.user.gold = player.user.gold - arm.gold
                print("You currently have", player.user.gold, "Gold left")
                player.user.armor = arm.armor
                input("")
                shop1()
            elif arm.armor_id == option and player.user.gold <= arm.gold:
                print("You do not have enough money to buy the armor")
                input("")
                shop1()
            elif option == "5":
                return
        
    

            
