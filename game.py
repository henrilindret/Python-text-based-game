import sys
import random
import pickle
import os
import weapons
import enemies
import shop
import player


def main():
    os.system('cls')
    print("Welcome to the dungeon")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            with open('savefile', 'rb') as f:
                player.user = pickle.load(f)
            print("Loaded Save State...")
            option = input('')
            intro()
    elif option == "3":
        sys.exit()
    else:
        main()


def start():
    os.system('cls')
    print("What is your name?")
    player.user.name = input("")
    intro()


def intro():
    while True:
        os.system('cls')
        print("Would you like to")
        print("1.) Fight")
        print("2.) Shop")
        print("3.) Stats")
        print("4.) Save")
        print("5.) Exit")
        option = input("-> ")
        if option == "1":
            fight()
        elif option == "2":
            shop.shop1()
        elif option == "3":
            stats()
        elif option == "4":
            with open('savefile', 'wb') as f:
                pickle.dump(player.user, f)
                print("Game has been saved!")
            option = input('')
            intro()
        elif option == "5":
            sys.exit()


def stats():
    print("Name:", player.user.name)
    print("Health:", player.user.health)
    print("Attack:", player.user.attack)
    print("Weapon:", player.user.weapon.name)
    print("Waves done:", player.user.waves)
    print("Gold:", player.user.gold)
    input("")
    intro()


def fight():
    global enemy
    while player.user.waves <= 5:
        enemyencounter = random.choice(enemies.enemylist1)
        enemy = enemyencounter
        print("You explore until you encounter an", enemy.name)
        print("What would you like to do?")
        print("1.) Attack")
        print("2.) Run away")
        option = input("-> ")
        if option == "1":
            Combat()
        else:
            intro()
    fight2()


def Combat():
    # Opponent miss and hit system very basic
    userdamage = random.randint(player.user.attack // 2, player.user.attack)
    enemydamage = random.randint(enemy.attack // 2, enemy.attack)
    if userdamage == player.user.attack // 2:
        print("You missed")
    else:
        print(enemy.health)
        print("You hit", enemy.name, "for", userdamage)
        enemy.health = enemy.health - userdamage
    input(' ')
    if enemy.health <= 0:
        win()
    if enemydamage == enemy.attack // 2:
        print("The enemy missed their attack")
    else:
        player.user.health -= enemydamage
        print(enemy.name, "hit you for", enemydamage)
    input(' ')
    if player.user.health <= 0:
        dead()
    else:
        Combat()


def win():
    print("You won the battle")
    player.user.waves = player.user.waves + 1
    enemy.health = enemy.maxhealth
    player.user.gold = player.user.gold + enemy.gold
    input(' ')
    intro()


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


def fight2():
    print("New wave")


main()
