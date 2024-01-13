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
import travelingmerchant

healed = 0

###########Start/talent############################


def main():
    os.system("cls")
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
        os.system("cls")
        print("1.) Not sure what to do? Press 'ENTER'")
        print()
        print(
            "2.) Most of the times you can write either '1' or '2' instead of the full word"
        )
        print()
        print("Press 'ENTER' to return to menu")
        input()
        os.system("cls")
        main()

    elif option == "4":
        sys.exit()
    else:
        main()


def start():
    os.system("cls")
    print("What is your name?")
    player.user.name = input("")
    os.system("cls")
    talentpick()


def talentpick():
    print("What is your talent?")
    print()
    print("1.) Warrior")
    print("2.) Paladin")
    talent = input("")
    if talent == "1" or talent.lower() == "warrior":
        player.user.talent = player.talents["Warrior"]
    elif talent == "2" or talent.lower() == "paladin":
        player.user.talent = player.talents["Paladin"]
    elif talent != "Warrior" or "Paladin":
        os.system("cls")
        print("You have not chosen a talent, do you wish to have no talent?")
        decision = input("")
        if decision == "yes":
            player.user.talent = player.talents["Normal"]
        elif decision == "no" or "" or " ":
            os.system("cls")
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
        print("6.) Go to the Tavern")
        print("7.) Exit")
        option = input("-> ")
        os.system("cls")
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
    os.system("cls")
    print("Name:", player.user.name)
    print("Experience:", player.user.exp)
    print("Talent:", player.user.talent.name)
    print("Health:", player.user.talent.health, "/", player.user.talent.maxhealth)
    print("ManaTalent:", player.user.talent.manatalent)
    print("Attack:", player.user.Attackdamage())
    print("Armor:", player.user.armor.name, "(", player.user.armorsave, "armor )")
    print("Armor value:", player.user.Armorvalue())
    print("Weapon:", player.user.weapon.name, "(", player.user.weapondamage, "damage )")
    print("Waves done:", player.user.waves)
    print("Gold:", player.user.gold)
    print("Current Zone:", player.user.zone)
    input("")
    if player.user.zone == "Forest":
        playerzone()
    elif player.user.zone == "Desert":
        Arrivedesert()
    elif player.user.zone == "City":
        intro()


##############Stats#####################################

##############Healing#####################################


def rest():
    os.system("cls")
    if player.user.waves % 3 == 0:
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
                return
    else:
        print("You cannot rest right now")
        input("")
        if player.user.zone == "Forest":
            playerzone()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            intro()


def tavern():
    os.system("cls")
    print("Welcome to the tavern!")
    print("For only the price of 20 gold you can rest to full hp")
    print("Would you like to rest?")
    print("1.) yes")
    print("2.) no")
    option = input()
    os.system("cls")
    if option == "1":
        if player.user.gold >= 20:
            print("Sleep well!")
            player.user.talent.health == player.user.talent.maxhealth
            player.user.gold = player.user.gold - 20
            input()
            intro()
        elif player.user.gold < 20:
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
    os.system("cls")
    global enemy
    enemyencounter = random.choice(enemies.forestenemylist)
    enemyencounter.health = enemyencounter.maxhealth
    enemy = enemyencounter
    print(
        "You encounter an",
        enemy.name,
        max(0, enemy.health),
        "/",
        enemy.maxhealth,
        "health",
    )
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Run away")
    option = input("-> ")
    os.system("cls")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
    else:
        if player.user.zone == "Forest":
            playerzone()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            intro()


def bossfight():
    os.system("cls")
    global enemy
    bossencounter = random.choice(enemies.forestbosslist)
    bossencounter.health = bossencounter.maxhealth
    enemy = bossencounter
    print(
        "You encounter an",
        enemy.name,
        max(0, enemy.health),
        "/",
        enemy.maxhealth,
        "health",
    )
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Desperate escape")
    option = input("-> ")
    os.system("cls")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
        input()
        os.system("cls")
        bossfight()
    elif option == "3":
        escape = random.randint(1, 100)
        if escape >= 50:
            print("You managed to escape")
            input()
            os.system("cls")
            playerzone()
        elif escape < 50:
            escapedam = random.randint(5, 15)
            player.user.talent.health -= escapedam
            print("You failed to escape")
            input()
            os.system("cls")
            print(
                "The",
                enemy.name,
                "lacerated you while you tried to escape, causing",
                escapedam,
                "damage",
            )
            print("")
            print(
                "You now have",
                player.user.talent.health,
                "/",
                player.user.talent.maxhealth,
                "health left",
            )
            input()
            os.system("cls")
            fightcontin()
    elif player.user.zone == "Forest":
        Arriveforest()
    elif player.user.zone == "Desert":
        Arrivedesert()
    elif player.user.zone == "City":
        intro()


def fightcontin():
    print("The enemy has", enemy.health, "/", enemy.maxhealth, "health left")
    print(
        "You have",
        player.user.talent.health,
        "/",
        player.user.talent.maxhealth,
        "health left",
    )
    print()
    print("Do you wish to continue fighting", enemy.name)
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Use Item")
    print("4.) Run away")
    option = input("-> ")
    os.system("cls")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
        input()
        os.system("cls")
        fightcontin()
    elif option == "3":
        print("no")
        input()
        os.system("cls")
        fightcontin()
    elif option == "4":
        if enemy.name == "Kneecrawler":
            print("You cant run anymore, you have to fight")
            input()
            os.system("cls")
            fightcontin()
        else:
            playerzone()
    else:
        fightcontin()


def Combat():
    userdamage = random.randint(
        player.user.Attackdamage() // 2, player.user.Attackdamage()
    )
    enemydamage = random.randint(enemy.attack // 2, enemy.attack) - random.randint(
        player.user.armorsave // 2, player.user.armorsave
    )
    print("You run and attack the enemy...")
    print()
    input("'ENTER' to continue")
    os.system("cls")

    if userdamage == player.user.Attackdamage() // 2:
        print("You missed")
        print()
        input("'ENTER' to continue")
        if userdamage != player.user.Attackdamage() // 2:
            pass
        os.system("cls")
    else:
        print("You hit", enemy.name, "for", userdamage)
        print()
        input("'ENTER' to continue")
        os.system("cls")
        enemy.health = enemy.health - userdamage
        print(
            enemy.name, "has", max(0, enemy.health), "/", enemy.maxhealth, "health left"
        )
        print()
        input("'ENTER' to continue")
        os.system("cls")
    if enemy.health <= 0:
        win()
    elif enemy.health > 0:
        print("The enemy charges menacingly at you...")
        print()
        input("'ENTER' to continue")
        os.system("cls")
    if enemydamage == enemy.attack // 2:
        print("The enemy missed their attack")
        print()
        input("'ENTER' to continue")
        os.system("cls")
    elif enemydamage <= 0:
        print("Your armor helped block")
        print()
        input("'ENTER' to continue")
        os.system("cls")
        fightcontin()
    else:
        player.user.talent.health -= enemydamage
        print(enemy.name, "hit you for", enemydamage)
        print()
        input("'ENTER' to continue")
        os.system("cls")
    if player.user.talent.health <= 0:
        dead()
    else:
        print(
            "You have",
            player.user.talent.health,
            "/",
            player.user.talent.maxhealth,
            "health left",
        )
        print()
        input("'ENTER' to continue")
        os.system("cls")
        fightcontin()


#########Win area####################


def win():
    os.system("cls")
    global enemy
    global healed

    print(f"You have killed the {enemy.name}")
    input()
    os.system("cls")

    print("What would you like to do?")
    print("1) Loot")
    print("2) Move forward")
    choice = input("")
    os.system("cls")

    if enemy.name == "Kneecrawler":
        golddrop = loot.boss_gold_gen()
        lootdrop = loot.boss_drop_gen()
    else:
        golddrop = loot.gold_drop_gen()
        lootdrop = loot.random_drop_gen()

    if choice == "1":
        print(f"You found {golddrop} gold!")
        player.user.gold += golddrop

        if lootdrop:
            if isinstance(lootdrop, weapons.Weapon):
                print(f"You found a {lootdrop.name}! ({lootdrop.attack} damage)")
                input()
                os.system("cls")
                print(
                    f"You currently have a {player.user.weapon.name} ({player.user.weapondamage} damage): Would you like to equip the new weapon?"
                )
            elif isinstance(lootdrop, armor.Armor):
                print(f"You found an {lootdrop.name}! ({lootdrop.armorsave} armor)")
                input()
                print(
                    f"You currently have a {player.user.armor.name} ({player.user.armorsave} armor): Would you like to equip the new armor?"
                )

            print("1.) Equip")
            print("2.) Discard")

            choice = input()
            os.system("cls")
            if choice == "1":
                if isinstance(lootdrop, weapons.Weapon):
                    player.user.weapon = lootdrop
                    player.user.weapondamage = lootdrop.attack
                    print(f"You have equipped the {lootdrop.name}!")
                    input()
                    playerzone()
                elif isinstance(lootdrop, armor.Armor):
                    player.user.armor = lootdrop
                    player.user.armorsave = lootdrop.armorsave
                    print(f"You have equipped the {lootdrop.name}!")
                    input()
                    playerzone()
                else:
                    print("You have discarded the item.")
                    input()
                    playerzone()

        elif choice == "2":
            print("You continue your exploration..")
            input()
            playerzone()

        else:
            print("")
            input()
            playerzone()

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
        playerzone()

    healed = 0


#########Win area####################

#########Dead area####################


def dead():
    os.system("cls")
    print("You have died")
    print("Do you want to start over?")
    print("1.) yes")
    print("2.) no")
    option = input("-> ")
    if option == "1" or "yes":
        main()
    elif option == 2 or "no":
        sys.exit()
    else:
        dead()


#########Dead area####################

##############Combat Area################################

##############Zone Area################################


def zonepick():
    os.system("cls")
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


def Arriveforest():
    os.system("cls")
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
        rest()
    elif option == "3":
        stats()
    elif option == "4":
        with open("savefile", "wb") as f:
            pickle.dump(player.user, f)
            print("Game has been saved!")
        option = input("")
        playerzone()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        playerzone()


def Arrivedesert():
    os.system("cls")
    print("You arrive at a refreshing osasis in the desert")
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
        playerzone()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        playerzone()


def playerzone():
    if player.user.zone == "Forest":
        Arriveforest()
    elif player.user.zone == "Desert":
        Arrivedesert()


def Explore():
    os.system("cls")
    print("You decide to explore around")
    Event = random.randint(1, 100)
    if Event < 1:
        print("You spot something running at you")
        print("Battle")
        input()
        fight()

    elif Event > 5:
        print("You encounter a strange man in a black cloak, he keeps smiling at you with his crooked teeth")
        print("Do you want to go and talk with him or leave?")
        print("1) go to him")
        print("2) Ignore him and leave")
        option = input()
        if option == "1":
            travelingmerchant.shop()
        elif option == "2": 
            print("You decided to leave and continue exploring")
            Explore()
        else:
            print("You decided to leave and continue exploring")
            Explore()


    elif Event <= 1:
        if player.user.zone == "Forest":
            print("You stumble upon an overgrown shrine, deep in the forest...")
            input()
            os.system("cls")
            print("You decide to...")
            print("")
            print("1.) Explore the shrine")
            print("2.) Leave the place alone")
            option = input("")
            os.system("cls")
            if option == "1":
                outcome = random.randint(1, 100)
                if outcome <= 75:
                    print("You hear some whispering in your head...")
                    input()
                    os.system("cls")
                    print("A shrine guardian appears! It's the Kneecrawler!")
                    bossfight()
                else:
                    print("While looking around, you find a chest, long forgotten...")
                    input()
                    os.system("cls")
                    print("You decide to...")
                    print()
                    print("1.) Try to open it")
                    print("2.) Leave it be")
                    chestopt = input("")
                    os.system("cls")
                    if chestopt == "1":
                        randomizer = random.randint(1, 100)
                        if randomizer <= 50:
                            legendaryarmor = random.choice(armor.lege_armorlist)
                            print(
                                "You found a legendary armor: The",
                                legendaryarmor.name,
                                "( ",
                                legendaryarmor.armorsave,
                                "armor )",
                            )
                            input("")
                            os.system("cls")
                            print(
                                "You currently have ",
                                player.user.armor.name,
                                "(",
                                player.user.armorsave,
                                "armor)",
                                "Would you like to equip the new armor?",
                            )
                            print()
                            print("1.) Yes")
                            print("2.) No")
                            option = input("")
                            os.system("cls")
                            if option == "1":
                                player.user.armor = legendaryarmor
                                player.user.armorsave = legendaryarmor.armorsave
                                print(
                                    "You have equipped the",
                                    legendaryarmor.name,
                                    "( ",
                                    legendaryarmor.armorsave,
                                    "armor )",
                                )
                                input()
                                os.system("cls")
                                print(
                                    "Leave this place alone, before you anger the gods..."
                                )
                                playerzone()
                            else:
                                Explore()
                        else:
                            legendaryweapon = random.choice(weapons.lege_weaponlist)
                            print(
                                "You found a legendary weapon: The",
                                legendaryweapon.name,
                                "( ",
                                legendaryweapon.attack,
                                "damage)",
                            )
                            input()
                            os.system("cls")
                            print(
                                "You currently have ",
                                player.user.weapon.name,
                                " (",
                                player.user.weapondamage,
                                "damage)" " would you like to equip the new weapon?",
                            )
                            print()
                            print("1.) Yes")
                            print("2.) No")
                            option = input("")
                            os.system("cls")
                            if option == "1":
                                player.user.weapon = legendaryweapon
                                player.user.weapondamage = legendaryweapon.attack
                                print(
                                    "You have equipped the",
                                    legendaryweapon.name,
                                    "( ",
                                    legendaryweapon.attack,
                                    "damage)",
                                )
                                input()
                                os.system("cls")
                                print(
                                    "Leave this place alone, before you anger the gods..."
                                )
                                playerzone()
                            else:
                                Explore()

            else:
                Explore()

        elif player.user.zone == "Desert":
            print()

    else:
        print("While exploring you found a holy spring")
        print("You decide to")
        print("1.) Drink it")
        print("2.) Rest near it")
        print("3.) Ignore it and leave")
        option = input("")
        os.system("cls")
        if option == "1":
            if player.user.talent.health == player.user.talent.maxhealth:
                print("You are at max health and cannot heal")
                input()
                os.system("cls")
                playerzone()
            else:
                waterhealth = random.randint(1, 10)
                print("You decide to drink from the spring and continue on your way")
                player.user.talent.health = player.user.talent.health + waterhealth
                if player.user.talent.health >= player.user.talent.maxhealth:
                    player.user.talent.health = player.user.talent.maxhealth
                input()
                os.system("cls")
                print("The refreshing water healed you for", waterhealth, "hp")
                playerzone()
        elif option == "2":
            print("You tried to rest but the noise of the spring annoyed you")
            input()
            os.system("cls")
            playerzone()
        elif option == "3":
            print("You ignore the spring and leave")
            input()
            os.system("cls")
            playerzone()
        else:
            playerzone()


##############Zone Area################################


main()
