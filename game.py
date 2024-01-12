import sys
import random
import pickle
import os
from turtle import clear
import enemies
import shop
import player
import loot
import armor
import weapons

healed = 0

###########Start/talent############################

def main():
    os.system("clear")
    print("Welcome to the dungeon")
    print("1.) Start")
    print("2.) Load")
    print("3.) Tutorial")
    print("4.) Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            with open("savefile", "rb") as f:
                player.user = pickle.load(f)
            print("Loaded Save State...")
            option = input("")
            intro()
    elif option == "3":
        os.system("clear")
        print("1.) Not sure what to do? Press 'ENTER'")
        print()
        print("2.) Most of the times you can write either '1' or '2' instead of the full word")
        print()
        print("Press 'ENTER' to return to menu")
        input()
        os.system("clear")
        main()
        
    elif option == "4":
        sys.exit()
        
    elif option == "sui":
        reset_stats()
        main()
    else:
        main()


def start():
    os.system("clear")
    print("What is your name?")
    player.user.name = input("")
    os.system("clear")
    talentpick()


def talentpick():
    print("What is your talent?")
    print()
    print("1.) Warrior")
    print("2.) Paladin")
    talent = input("")
    if talent == "1" or talent.lower() == "warrior":
        player.user.talent = player.talents["Warrior"]
        player.user.health = player.user.talent.health
    elif talent == "2" or talent.lower() == "paladin":
        player.user.talent = player.talents["Paladin"]
        player.user.health = player.user.talent.health
    elif talent != "Warrior" or "Paladin":
        os.system("clear")
        print("You have not chosen a talent, do you wish to have no talent?")
        decision = input("")
        if decision == "yes":
            player.user.talent = player.talents["Normal"]
            player.user.health = player.user.talent.health
        elif decision == "no" or "" or " ":
            os.system("clear")
            talentpick()
    intro()

###########Start/talent############################


def intro():
    while True:
        os.system("clear")
        player.user.zone = "City"
        print("You arrive in the city of Karshrad, Would you like to")
        print("1.) Go outside the city")
        print("2.) Shop")
        print("3.) Stats")
        print("4.) Save")
        print("5.) Rest")
        print("6.) Go to the Tavern")
        print("7.) Exit")
        option = input("-> ")
        os.system("clear")
        if option == "1":
            zonepick()
        elif option == "2":
            shop.shop1()
        elif option == "3":
            stats()
        elif option == "4":
            with open("savefile", "wb") as f:
                pickle.dump(player.user, f)
                print("Game has been saved!")
            option = input("")
            intro()
        elif option == "5":
           rest()
        elif option == "6":
            tavern()
        elif option == "7":
            sys.exit()

##############Stats#####################################

def stats():
    os.system("clear")
    enemieskilled = 0
    print("Name:", player.user.name)
    print("Experience:", player.user.exp)
    print("Talent:", player.user.talent.name)
    print("Health:", player.user.talent.health, "/", player.user.talent.maxhealth)
    print("ManaTalent:", player.user.talent.manatalent)
    print("Attack:", player.user.Attackdamage())
    print("Armor:", player.user.armor.name, "(",player.user.armorsave, "armor )")
    print("Armor value:", player.user.Armorvalue())
    print("Weapon:", player.user.weapon.name, "(",player.user.weapondamage, "damage )")
    print("Waves done:", player.user.waves)
    print("Gold:", player.user.gold)
    print("Current Zone:", player.user.zone)
    print("Enemies killed:", player.user.kills)
    input("")
    if player.user.zone == "Forest":
        Arriveforest()
    elif player.user.zone == "Desert":
        Arriveforest()
    elif player.user.zone == "City":
        intro()  
    
##############Stats#####################################

##############Healing#####################################

def rest():
    os.system("clear")

    if player.user.waves % 3 == 0:
        global healed
        healamount = random.randint(5, 12)
        healing = player.user.talent.health + healamount
        healthlost = player.user.talent.maxhealth - player.user.talent.health

        if healamount > healthlost:
            healamount = healthlost
            healamount = abs(healamount)

        if healed == 1:
            print("You have already healed once")
            input()
        elif player.user.talent.health == player.user.talent.maxhealth:
            print("You are at max hp and cannot heal")
            input()
        elif player.user.talent.health < player.user.talent.maxhealth:
            print("Healed you for", healamount, "hp")
            player.user.talent.health = healing
            healed += 1
            input()
            intro()
    else:
        print("You cannot rest right now")
        input("")
        if player.user.zone == "Forest":
            Arriveforest()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            intro()  

def tavern():
    os.system("clear")
    print("Welcome to the tavern!")
    print("For only the price of 15 gold you can rest to full hp")
    print("Would you like to rest?")
    print("1.) yes")
    print("2.) no")
    option = input()
    os.system("clear")
    if option == "1":
        if player.user.gold >= 15:
            print("Sleep well!")
            player.user.talent.health = player.user.talent.maxhealth
            player.user.gold = player.user.gold - 20
            input()
            intro()
        elif player.user.gold < 15:
            print("You do not have enough gold, better luck next time")
            input()
            intro()
    elif option == "2":
        print("go away then")
        input()
        intro()
    else:
        tavern()
        
##############Healing#####################################

##############Combat Area################################

def fight():
    os.system("clear")
    global enemy
    
    if player.user.zone == "Forest":
        enemyencounter = random.choice(enemies.forestenemylist)
    elif player.user.zone == "Desert":
        enemyencounter = random.choice(enemies.desertenemylist)
    
    enemy = enemyencounter
    print("you encounter an", enemy.name)
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell WIP")
    print("3.) Run away")
    option = input("-> ")
    os.system("clear")
    if option == "1":
        Combat()
    elif option == "2":
        print("WIP")
        input()
        os.system("clear")
        fightcontin()
    else:
        if player.user.zone == "Forest":
            Arriveforest()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            intro()  

def fightcontin():
    
    print("Do you wish to continue fighting", enemy.name)
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell WIP")
    print("3.) Use Item WIP")
    print("4.) Run away")
    option = input("-> ")
    os.system("clear")
    if option == "1":
        os.system("clear")
        Combat()
    elif option == "2":
        print("no")
    elif option == "3":
        print("WIP")
        input()
        os.system("clear")
        fightcontin()
    elif option == "4":
        print(f"{enemy.name}: KUHU SA JOOKSED ARGGGG!!!")
        input()
        if player.user.zone == "Forest":
            Arriveforest()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            intro()  
    else:
        fightcontin()

def Combat():
    userdamage = random.randint(
        player.user.Attackdamage() // 2, player.user.Attackdamage()
    )
    enemydamage = random.randint(enemy.attack // 2, enemy.attack) - random.randint(
        player.user.armorsave // 2, player.user.armorsave
    )
    if userdamage == player.user.Attackdamage() // 2:
        print("You missed")
        print()
        input("'ENTER' to continue")
        os.system("clear")
    else:
        print(enemy.name, "has", enemy.health, "health left")
        print()
        input("'ENTER' to continue")
        os.system("clear")
        print("You hit", enemy.name, "for", userdamage)
        enemy.health = max(0, enemy.health - userdamage)
        print()
        input("'ENTER' to continue")
        os.system("clear")
    if enemy.health <= 0:
        win()
    if enemydamage == enemy.attack // 2:
        print("The enemy missed their attack")
        print()
        input("'ENTER' to continue")
        os.system("clear")
    elif enemydamage <= 0:
        print("Your armor helped block")
        print()
        input("'ENTER' to continue")
        os.system("clear")
    else:
        player.user.talent.health -= enemydamage
        print(enemy.name, "hit you for", enemydamage)
        print()
        input("'ENTER' to continue")
        os.system("clear")
    if player.user.talent.health <= 0:
        print("You have been killed")
        input()
        os.system("clear")
        dead()
    elif player.user.talent.health > 0:
        print("You have", player.user.talent.health, "health left")
        print()
        input("'ENTER' to continue")
        os.system("clear")
        fightcontin()
    else:
        fightcontin()





#########Win area####################



def win():
    os.system("clear")
    global enemy
    global healed

    print(f"You have killed the {enemy.name}")
    player.user.kills += 1
    input()
    os.system("clear")

    print("What would you like to do?")
    print("1) Loot")
    print("2) Move forward")
    choice = input("")
    os.system("clear")
    
    golddrop = loot.gold_drop_gen()
    lootdrop = loot.random_drop_gen()

    if choice == "1":
        print(f"You found {golddrop} gold!")
        player.user.gold += golddrop
        

        if lootdrop:
            if isinstance(lootdrop, weapons.Weapon):
                print(f"You found a {lootdrop.name}! ({lootdrop.attack} damage)")
                input()
                os.system("clear")
                print(f"You currently have a {player.user.weapon.name} ({player.user.weapondamage} damage): Would you like to equip the new weapon?")
            elif isinstance(lootdrop, armor.Armor):
                print(f"You found an {lootdrop.name}! ({lootdrop.armorsave} armor)")
                input()
                print(f"You currently have a {player.user.armor.name} ({player.user.armorsave} armor): Would you like to equip the new armor?")
            
            print("1.) Equip")
            print("2.) Discard")
            
            choice = input()
            os.system("clear")
            if choice == "1":
                if isinstance(lootdrop, weapons.Weapon):
                    player.user.weapon = lootdrop
                    player.user.weapondamage = lootdrop.attack
                    print(f"You have equipped the {lootdrop.name}!")
                    input()
                    arriveplayerzone()
                elif isinstance(lootdrop, armor.Armor):
                    player.user.armor = lootdrop
                    player.user.armorsave = lootdrop.armorsave
                    print(f"You have equipped the {lootdrop.name}!")
                    input()
                    arriveplayerzone()
                else:
                    print("You have discarded the item.")
                    input()
                    arriveplayerzone()

        elif choice == "2":
            print("You continue your exploration..")
            input()
            arriveplayerzone()

        else:
            print("")
            input()
            arriveplayerzone()

    player.user.waves += 1
    enemy.health = enemy.maxhealth
    player.user.gold += golddrop
    player.user.exp += enemy.exp
    current_talent = player.user.talent.name

    if player.user.exp >= 100 and current_talent in player.talents:
        level_up = player.talents[current_talent].levelup
        player.talents[current_talent].maxhealth += level_up["maxhealth"]
        player.user.basedamage += level_up["basedamage"]
        player.user.exp = 0
        print("Congratulations, you leveled up!")

    if player.user.zone == "Forest":
        Arriveforest()  
        
    elif player.user.zone == "Desert":
        Arrivedesert()
        
    elif player.user.zone == "City":
        print("How are you here?") 

    healed = 0

    
    
    
#########Win area####################

#########Dead area####################
    
def dead():
    os.system("clear")
    print("You have died")
    print("Do you want to start over?")
    print("1.) yes")
    print("2.) no")
    option = input("-> ")
    if option == "1" or "yes":
        reset_stats()
        main()
    elif option == 2 or "no":
        sys.exit()
    else:
        dead()
        
def reset_stats():
    global healed
    global player
    
    player.user.name = ""
    player.user.talent.health = player.user.health
    player.user.maxhealth = 0 + player.user.maxhealth 
    player.user.exp = 0
    player.user.gold = 50
    player.user.weapon = weapons.Fist
    player.user.weapondamage = player.user.weapon.attack
    player.user.armor = armor.Naked
    player.user.armorsave = player.user.armor.armorsave
    player.user.waves = 0
    player.user.kills = 0
    player.user.zone = ""
    
#########Dead area####################

##############Combat Area################################

##############Zone Area################################

def zonepick():
    os.system("clear")
    print("Outside the city you have different zones you can go to")
    print("1.) Forest")
    print("2.) Desert")
    option = input("")
    if option == "1":
        player.user.zone = "Forest"
        print("You decide to go to the forest")
        Arriveforest()
    elif option == "2":
        player.user.zone = "Desert"
        print("You decide to go to the desert")
        Arrivedesert()
        
def arriveplayerzone():
    if player.user.zone == "Forest":
        Arriveforest()
    elif player.user.zone == "Desert":
        Arrivedesert()


def Arriveforest():
    os.system("clear")
    print("You arrive at a safespot in the forest")
    print("In the forest you can")
    print("1.) Explore")
    print("2.) Rest")
    print("3.) Stats")
    print("4.) Save")
    print("5.) Return")
    option = input("-> ")
    if option == "1":
        Explore()
    elif option == "2":
        rest()
    elif option == "3":
        stats()
    elif option == "4":
        with open("savefile", "wb") as f:
            pickle.dump(player.user, f)
            print("Game has been saved!")
        option = input("")
        Arriveforest()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        Arriveforest()
        
def Arrivedesert():
    os.system("clear")
    print("You arrive at an refreshing oasis in desert")
    print("In the desert you can")
    print("1.) Explore")
    print("2.) Rest")
    print("3.) Stats")
    print("4.) Save")
    print("5.) Return")
    option = input("-> ")
    if option == "1":
        Explore()
    elif option == "2":
        rest()
    elif option == "3":
        stats()
    elif option == "4":
        with open("savefile", "wb") as f:
            pickle.dump(player.user, f)
            print("Game has been saved!")
        option = input("")
        Arriveforest()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        Arrivedesert()
    
def Explore():
    os.system("clear")
    print("You decide to explore around")
    Event = random.randint(1, 100)
    if Event >= 10:
        print("You spot something running at you")
        print("Battle")
        input()
        fight()
    else:
        print("While exploring you found a holy spring")
        print("You decide to")
        print("1.) Drink it")
        print("2.) Rest near it")
        print("3.) Ignore it and leave")
        option = input("")
        os.system("clear")
        if option == "1":
            print("You decide to drink from the well and continue on your way")
            player.user.health = player.user.health + 10
            if player.user.health >= player.user.maxhealth:
                player.user.health = player.user.maxhealth
            input()
            Explore()
        elif option == "2":
            print("You tried to rest but the noise of the spring annoyed you")
            input()
            Explore()
        elif option == "3":
            print("You ignore the spring and leave")
            input()
            Explore()
        else:
            Explore()
            
        

##############Zone Area################################











main()
