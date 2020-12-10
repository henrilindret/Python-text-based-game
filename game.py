import sys
import random
import pickle
import os
import weapons
import enemies
import shop
import player


# Future code plan, defense/armor reduces attack power. so if you have 5 defense then it will reduce attack by 2.


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
                global user
                user = pickle.load(f)
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
    name = input()
    global user
    user = player.Player(name)
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
                global user
                pickle.dump(user, f)
                print("Game has been saved!")
            option = input('')
            intro()
        elif option == "5":
            sys.exit()


def stats():
    print("Name:", user.name)
    print("Health:", user.health)
    print("Attack:", user.attack)
    print("Weapon:", user.weapon.name)
    print("Waves done:", user.waves)
    input("")
    intro()


def fight():
    global enemy
    while user.waves <= 5:
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
    userdamage = random.randint(user.attack // 2, user.attack)
    enemydamage = random.randint(enemy.attack // 2, enemy.attack)
    if userdamage == user.attack // 2:
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
        user.health -= enemydamage
        print(enemy.name, "hit you for", enemydamage)
    input(' ')
    if user.health <= 0:
        dead()
    else:
        Combat()


def win():
    print("You won the battle")
    user.waves = user.waves + 1
    enemy.health = enemy.maxhealth
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
