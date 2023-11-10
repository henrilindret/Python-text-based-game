import sys
import random
import pickle
import os
import enemies
import shop
import player
import loot

healed = 0

###########Start/talent############################

def main():
    os.system("cls")
    print("Welcome to the dungeon")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
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
        sys.exit()
    else:
        main()


def start():
    os.system("cls")
    print("What is your name?")
    player.user.name = input("")
    talentpick()


def talentpick():
    print("What is your talent?")
    print("Warrior")
    print("Paladin")
    talent = input("")
    if talent == "Warrior":
        player.user.talent = player.talents["Warrior"]
    elif talent == "Paladin":
        player.user.talent = player.talents["Paladin"]
    elif talent != "Warrior" or "Paladin":
        print("You have not chosen a talent, do you wish to have no talent?")
        decision = input("")
        if decision == "yes":
            player.user.talent = player.talents["Normal"]
        elif decision == "no" or "" or " ":
            talentpick()
    intro()

###########Start/talent############################


def intro():
    while True:
        os.system("cls")
        player.user.zone = "City"
        print("You arrive in the city of Karshrad, Would you like to")
        print("1.) Go outside the city")
        print("2.) Shop")
        print("3.) Stats")
        print("4.) Save")
        print("5.) Rest")
        print("6.) Exit")
        option = input("-> ")
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
        elif option == "6":
            sys.exit()
        if option == "5" and player.user.waves % 3 == 0:
            global healed
            healamount = random.randint(1, 10)
            healing = player.user.talent.health + healamount
            if healed == 1:
                print("you have already healed once")
                input()
            elif player.user.talent.health == player.user.talent.maxhealth:
                print("You are at max hp and cannot heal")
                input()
            elif player.user.talent.health < player.user.talent.maxhealth:
                print("Healed you for", healamount, "hp")
                player.user.talent.health = healing
                healed = healed + 1
                input()
                if player.user.talent.health > player.user.talent.maxhealth:
                    player.user.talent.health = player.user.talent.maxhealth
        elif option == "5":
            print("You cannot rest right now")
            input("")

##############Stats#####################################

def stats():
    print("Name:", player.user.name)
    print("Experience:", player.user.exp)
    print("Talent:", player.user.talent.name)
    print("Health:", player.user.talent.health, "/", player.user.talent.maxhealth)
    print("ManaTalent:", player.user.talent.manatalent)
    print("Attack:", player.user.Attackdamage())
    print("Armor:", player.user.armor)
    print("Weapon:", player.user.weapon.name)
    print("Waves done:", player.user.waves)
    print("Gold:", player.user.gold)
    print("Current Zone:", player.user.zone)
    input("")
    intro()
    
##############Stats#####################################

##############Combat Area################################

def fight():
    global enemy
    enemyencounter = random.choice(enemies.forestenemylist)
    enemy = enemyencounter
    print("you encounter an", enemy.name)
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Run away")
    option = input("-> ")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
    else:
        intro()

def fightcontin():
    print("Do you wish to continue fighting", enemy.name)
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Use Item")
    print("4.) Run away")
    option = input("-> ")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
    else:
        intro()


def Combat():
    userdamage = random.randint(
        player.user.Attackdamage() // 2, player.user.Attackdamage()
    )
    enemydamage = random.randint(enemy.attack // 2, enemy.attack) - random.randint(
        player.user.armor // 2, player.user.armor
    )
    if userdamage == player.user.Attackdamage() // 2:
        print("You missed")
    else:
        print(enemy.health)
        print("You hit", enemy.name, "for", userdamage)
        enemy.health = enemy.health - userdamage
    input(" ")
    if enemy.health <= 0:
        win()
    if enemydamage == enemy.attack // 2:
        print("The enemy missed their attack")
    elif enemydamage <= 0:
        print("Your armor helped block")
    else:
        player.user.talent.health -= enemydamage
        print(enemy.name, "hit you for", enemydamage)
    input(" ")
    if player.user.talent.health <= 0:
        dead()
    else:
        fightcontin()


#########Win area####################
def win():
    print("You won the battle")
    player.user.waves = player.user.waves + 1
    enemy.health = enemy.maxhealth
    player.user.gold = player.user.gold + enemy.gold
    player.user.exp = player.user.exp + enemy.exp
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
        Arriveforest()
    elif player.user.zone == "City":
        print("how are you here?")  
    global healed
    healed = 0
    
    
    
#########Win area####################

def dead():
    print("You have died")
    print("Do you want to start over?")
    print("1.) yes")
    print("2.) no")
    option = input("-> ")
    if option == 1:
        main()
    elif option == 2:
        sys.exit()
    else:
        dead()

##############Combat Area################################

##############Zone Area################################

def zonepick():
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
        zonepick()


def Arriveforest():
    print("You arrive at a safespot in the forest")
    print("In the Forest you can")
    print("1.) Explore")
    print("2.) Rest")
    print("3.) Stats")
    print("4.) Save")
    print("5.) Return")
    option = input("-> ")
    if option == "1":
        Explore()
    elif option == "2":
        print("rest")
    elif option == "3":
        stats()
    elif option == "4":
        with open("savefile", "wb") as f:
            pickle.dump(player.user, f)
            print("Game has been saved!")
        option = input("")
        Arriveforest()
    elif option == "5":
        return    
    
def Explore():
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
        Arriveforest()
        

##############Zone Area################################











main()
