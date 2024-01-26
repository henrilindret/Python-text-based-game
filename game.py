import sys
import random
import pickle
import os
from turtle import clear
import enemies
import player
import loot
import armor
import weapons
import merchantshop
import wizardshop
import spells
import platform


healed = 0

###########Start/talent############################

def main():
    os.system("clear")
    print("Welcome to the Age of Lindret")
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
    print("1.) Warrior")
    print("2.) Paladin")
    print("3.) Assassin")
    talent = input("").lower()

    if talent == "1" or talent == "warrior":
        player.user.talent = player.warrior
    elif talent == "2" or talent == "paladin":
        player.user.talent = player.paladin
    elif talent == "3" or talent == "assassin":
        player.user.talent = player.assassin
    elif talent not in ["warrior", "paladin"]:
        os.system("clear")
        print("You have not chosen a valid talent.")
        print("Do you wish to have no talent?")
        print("1.) Yes")
        print("2.) No")
        decision = input().lower()

        while decision not in ["yes", "no", "1", "2"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            decision = input().lower()

        if decision == "yes" or decision == "1":
            player.user.talent = player.normal["Normal"]
        elif decision == "no" or decision == "2":
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
        print("3.) Magic shop")
        print("4.) Stats")
        print("5.) Spells")
        print("6.) Save")
        print("7.) Rest")
        print("8.) Go to the Tavern")
        print("9.) Exit")
        option = input("-> ")
        os.system("clear")
        if option == "1":
            zonepick()
        elif option == "2":
            shop1()
        elif option == "3":
            shop2()
        elif option == "4":
            stats()
        elif option == "5":
            spellstats()
        elif option == "6":
            with open("savefile", "wb") as f:
                pickle.dump(player.user, f)
                print("Game has been saved!")
            option = input("")
            intro()
        elif option == "7":
           rest()
        elif option == "8":
            tavern()
        elif option == "9":
            sys.exit()
        else:
            intro()

##############Stats#####################################

def stats():
    os.system("clear")
    print("Name:", player.user.name)
    print("Level:", player.user.level, "(", player.user.xp, "/", player.user.maxp, "xp)")
    print("Talent:", player.user.talent.name)
    print("Health:", player.user.talent.health, "/", player.user.talent.maxhealth)
    print("Magic Level:", player.user.talent.magiclevel, "(", player.user.talent.mana, "/", player.user.talent.maxmana, "mana )")
    print("Weapon:", player.user.weapon.name, "(",player.user.weapondamage, "damage )")
    print("Attack:", player.user.Attackdamage())
    print("Armor:", player.user.armor.name, "(",player.user.armorsave, "armor )")
    print("Armor value:", player.user.Armorvalue())
    print("Waves done:", player.user.waves)
    print("Gold:", player.user.gold)
    print("Enemy kills:", player.user.kills, "/", "Boss kills:", player.user.bosskills)
    input("")
    if player.user.zone == "Forest":
        Arriveplayerzone()
    elif player.user.zone == "Desert":
        Arrivedesert()
    elif player.user.zone == "City":
        intro()
        
def learn_spell(self, spell):
    self.known_spells.append(spell)
    print(f"{self.name} learned the spell: {spell.name}")

def display_talentspells(self):
    print("Your known Spells:")
    print()
    for spell in self.known_spells:
        print(f"{spell.name} - Damage: {spell.damage}, Mana Cost: {spell.mana_cost}")       

def spellstats():
    os.system("clear")
    print("Here are all your known spells:")
    print()
    
    input()
    
    
    
##############Stats#####################################

##############Shops#####################################
def shop1():
    os.system("clear")
    print("WELCOME TO THE SHOP")
    print()
    print("You currently have", player.user.gold, "Gold")
    print("Do you wish to check weapons(1) or armor(2)?")
    print("If you wish to leave, press 'ENTER'")
    shoptype = input().lower()
    os.system("clear")

    if shoptype in ["weapon", "weapons", "1"]:
        print("The shop is currently selling:    You currently have", player.user.gold, "Gold")
        for wep in weapons.weaponlist:
            print(wep.weapon_id, wep.name, "(", wep.attack, "damage ): cost", wep.gold)
        print()
        print("What would you like to buy?")
        print("If you wish to leave, press 'ENTER'")
        try:
            option = int(input())
        except ValueError:
            shop1()
        else:
            os.system("clear")
            for wep in weapons.weaponlist:
                if wep == player.user.weapon and option == wep.weapon_id:
                    print("You have already bought this item")
                    input()
                    shop1()
                elif wep.weapon_id == option and player.user.gold >= wep.gold:
                    print(wep.name + " purchased")
                    player.user.gold -= wep.gold
                    print("You currently have", player.user.gold, "Gold left")
                    player.user.weapon = wep
                    player.user.weapondamage = wep.attack
                    input()
                    shop1()
                elif wep.weapon_id == option and player.user.gold < wep.gold:
                    print("You do not have enough money to buy the weapon")
                    input()
                    shop1()

    elif shoptype in ["armor", "2"]:
        print("The shop is currently selling:    You currently have", player.user.gold, "Gold")
        for arm in armor.armorlist:
            print(arm.armor_id, arm.name, "(", arm.armorsave, "armor ): cost", arm.gold)
        print()
        print("What would you like to buy?")
        print("If you wish to leave, press 'ENTER'")
        try:
            option = int(input())
        except ValueError:
            shop1()
        else:
            os.system("clear")
            for arm in armor.armorlist:
                if arm == player.user.armorsave and option == arm.armor_id:
                    print("You have already bought this item")
                    input()
                    shop1()
                elif arm.armor_id == option and player.user.gold >= arm.gold:
                    print(arm.name + " purchased")
                    player.user.gold -= arm.gold
                    print("You currently have", player.user.gold, "Gold left")
                    player.user.armorsave = arm.armorsave
                    player.user.armor = arm
                    input()
                    shop1()
                elif arm.armor_id == option and player.user.gold < arm.gold:
                    print("You do not have enough money to buy the armor")
                    input()
                    shop1()

    Arriveplayerzone()
    
    
def shopintro():
    os.system("clear")
    print("You see a shady figure standing in the distance...")
    input()
    os.system("clear")
    print("You decide to...")
    print("1.) Approach the figure")
    print("2.) Move on")
    option = input()
    os.system("clear")
    if option == "1":
        print("Welcome to the shadiest shop in the world har har")
        input()
        os.system("clear")
        if not player.user.merchantpay:
            print("To look at my really suspicious wares you have to pay me 20 gold")
            print()
            print("You have", player.user.gold, "Gold")
            input()
            os.system("clear")
            print("Would you like to pay 20 gold?")
            print("1) yes")
            print("2) no")
            option = input()
            os.system("clear")
            if option == "1" and player.user.gold >= 20:
                player.user.gold -= 20
                player.user.merchantpay = True
                os.system("clear")
                shop()
            elif option == "1" and player.user.gold < 20:
                print("You do not have enough money and leave")
                input()
                os.system("clear")
                Arriveplayerzone()
            elif option == "2":
                print("You decide not to pay and leave")
                input()
                os.system("clear")
                Arriveplayerzone()
            else:
                print("you leave")
                input()
                os.system("clear")
                Arriveplayerzone()
    elif option == "2":
        Arriveplayerzone()


def shop():
    print("You currently have:", player.user.gold, "Gold")
    print()
    print("You won't be disappointed ;)")
    print("Here's what I have right now:")
    print()
    
    for item in merchantshop.tomelist:
        print(item.item_id, item.name, ": cost", item.gold)

    print()
    print("What would you like to buy?")
    print("If you wish to leave, press 'ENTER'")
    try:
        pick = int(input())
    except ValueError:
        os.system("clear")
        Arriveplayerzone()

    if pick == 100:
        player.user.merchantpay = False
        os.system("clear")
        Arriveplayerzone()

    for item in merchantshop.tomelist:
        if pick == item.item_id and player.user.gold >= item.gold:
            if pick == 1:
                os.system("clear")
                print("You have bought Tome of health")
                player.user.talent.maxhealth += item.health
                player.user.gold -= item.gold
                print("Your max health has increased by 10")
                input()
                os.system("clear")
                shop()
            elif pick == 2:
                os.system("clear")
                print("You have bought Tome of strength")
                player.user.basedamage += item.damage
                player.user.gold -= item.gold
                print("Your base damage has increased by 5")
                input()
                os.system("clear")
                shop()
            elif pick == 3:
                os.system("clear")
                print("You have bought Tome of armor")
                player.user.basearmor += item.armor
                player.user.gold -= item.gold
                print("Your base armor has increased by 5")
                input()
                os.system("clear")
                shop()
    
        
def buy_spell(self, spell):
    os.system("clear")
    self.talent.known_spells.append(spell)
    print(f"{self.name} learned the spell: {spell.name}")
    input()
    
def shop2():
    os.system("clear")
    print("Welcome to the wizard shop")
    print()
    input("Press 'ENTER' to continue")
    os.system("clear")
    print("You currently have:", player.user.gold, "Gold")
    print()
    print("Here's what I have right now:")
    print()
    for item in wizardshop.wizarditemslist:
        print(item.id, item.name, ": cost", item.gold)
    
    try:
        option = int(input("Enter the ID of the spell you want to buy: "))
    except ValueError:
        print("You have not chosen a valid option")
        input()
        shop2()
    else:
        os.system("clear")
        for spell in wizardshop.wizarditemslist:
            if spell.id == option:
                if spell in player.user.spelllist:
                    os.system("clear")
                    print("You have already bought this item")
                    input()
                    shop2()
                elif player.user.gold >= spell.gold:
                    os.system("clear")
                    print(spell.name + " purchased")
                    player.user.gold -= spell.gold
                    player.user.spelllist.append(spell)
                    print("You currently have", player.user.gold, "Gold left")
                    input()
                    os.system("clear")
                    shop2()
                elif option == 100:
                    os.system("clear")
                    Arriveplayerzone()
                else:
                    os.system("clear")
                    print("You do not have enough money to buy the spell")
                    input()
                    shop2()
    intro()
# Call shop2() to start the shopping process
 
    

        
##############Shop#####################################

##############Healing#####################################

def rest():
    os.system("clear")
    if player.user.waves % 3 == 0:
        global healed
        healamount = random.randint(1, 10)
        healing = player.user.talent.health + healamount
        if healed == 1:
            print("you have already healed once")
            input()
            Arriveplayerzone()
        elif player.user.talent.health == player.user.talent.maxhealth:
            print("You are at max hp and cannot heal")
            input()
            Arriveplayerzone()
        elif player.user.talent.health < player.user.talent.maxhealth:
            player.user.talent.health = healing
            healed = healed + 1
            if player.user.talent.health > player.user.talent.maxhealth:
                player.user.talent.health = player.user.talent.maxhealth
                return
            print("Healed you for", healamount, "hp")
            input("")
            os.system("clear")
            Arriveplayerzone()
    else:
        print("You cannot rest right now")
        input("")
        if player.user.zone == "Forest":
            Arriveplayerzone()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            Arriveplayerzone()  

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
            player.user.gold = player.user.gold - 15
            input()
            Arriveplayerzone()
        elif player.user.gold < 15:
            print("You do not have enough gold, better luck next time")
            input()
            Arriveplayerzone()
    elif option == "2":
        print("go away then")
        input()
        Arriveplayerzone()
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
    elif player.user.zone == "Lankland": 
        enemyencounter = random.choice(enemies.lankenemylist)
    
    enemyencounter.health = enemyencounter.maxhealth
    enemy = enemyencounter
    print("You encounter an",enemy.name, max(0,enemy.health), "/", enemy.maxhealth, "health")
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Run away")
    option = input("-> ")
    os.system("clear")
    if option == "1":
        Combat()
    elif option == "2":
        print("not work")
        input()
        os.system("clear")
        Combat()
    elif option == "3":
        if player.user.zone == "Forest":
            Arriveplayerzone()
        elif player.user.zone == "Desert":
            Arrivedesert()
        elif player.user.zone == "City":
            intro()
    else:
        Combat()
        
            
            
def bossfight():
    os.system("clear")
    global enemy
    
    if player.user.zone == "Forest": 
        bossencounter = random.choice(enemies.forestbosslist)
    elif player.user.zone == "Desert":
        bossencounter = random.choice(enemies.desertbosslist)
    elif player.user.zone == "Lankland": 
        bossencounter = random.choice(enemies.lankbosslist)
    
    bossencounter.health = bossencounter.maxhealth
    enemy = bossencounter
    print("You encounter an",enemy.name, max(0,enemy.health), "/", enemy.maxhealth, "health")
    print("What would you like to do?")
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Desperate escape")
    option = input("-> ")
    os.system("clear")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
        input()
        os.system("clear")
        bossfight()
    elif option == "3":
        escape = random.randint(1, 100)
        if escape >= 50:
            print("You managed to escape")
            input()
            os.system("clear")
            Arriveplayerzone()
        elif escape < 50:
            escapedam = random.randint(5,15)
            player.user.talent.health -= escapedam
            print("You failed to escape")
            input()
            os.system("clear")
            print("The", enemy.name, "lacerated you while you tried to escape, causing", escapedam, "damage")
            print("")
            input()
            os.system("clear")
            if player.user.talent.health <= 0:
                dead()
            else:
                print("You now have", max(0,player.user.talent.health), "/", player.user.talent.maxhealth, "health left")
                input()
                os.system("clear")
                fightcontin()
    elif player.user.zone == "Forest":
        Arriveforest()
    elif player.user.zone == "Desert":
        Arrivedesert()
    elif player.user.zone == "City":
        intro()

def fightcontin():
    
    print("The enemy has", enemy.health, "/", enemy.maxhealth , "health left")
    print("You have", player.user.talent.health,  "/", player.user.talent.maxhealth, "health left")
    print()
    print("Do you wish to continue fighting", enemy.name)
    print("1.) Attack")
    print("2.) Use spell")
    print("3.) Use Item")
    print("4.) Run away")
    option = input("-> ")
    os.system("clear")
    if option == "1":
        Combat()
    elif option == "2":
        print("no")
        input()
        os.system("clear")
        fightcontin()
    elif option == "3":
        print("no")
        input()
        os.system("clear")
        fightcontin()
    elif option == "4":
        if enemy.name == "Kneecrawler" or enemy.name == "Soulmauler":
            print("You cant run anymore, you have to fight")
            input()
            os.system("clear")
            fightcontin()
        else:
            Arriveplayerzone()
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
    os.system("clear")
    
    if userdamage == player.user.Attackdamage() // 2:
        print("You missed")
        print()
        input("'ENTER' to continue")
        if userdamage != player.user.Attackdamage() // 2:
            pass
        os.system("clear")
    else:
        print("You hit", enemy.name, "for", userdamage)
        print()
        input("'ENTER' to continue")
        os.system("clear")
        enemy.health = enemy.health - userdamage
        print(enemy.name, "has", max(0, enemy.health), "/", enemy.maxhealth, "health left")
        print()
        input("'ENTER' to continue")
        os.system("clear")
    if enemy.health <= 0:
        win()
    elif enemy.health > 0:
        print("The enemy charges menacingly at you...")
        print()
        input("'ENTER' to continue")
        os.system("clear")
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
        fightcontin()
    else:
        player.user.talent.health -= enemydamage
        print(enemy.name, "hit you for", enemydamage)
        print()
        input("'ENTER' to continue")
        os.system("clear")
    if player.user.talent.health <= 0:
        dead()
    else:
        print("You have", player.user.talent.health, "/", player.user.talent.maxhealth, "health left")
        print()
        input("'ENTER' to continue")
        os.system("clear")
        fightcontin()



##############Combat Area################################

#########Win area####################



def win():
    os.system("clear")
    global enemy
    global healed

    print(f"You have killed the {enemy.name}")
    input()
    os.system("clear")
    if enemy.name not in enemies.desertbosslist and enemy.name not in enemies.forestbosslist and enemy.name not in enemies.lankbosslist:
        player.user.kills += 1
    else:
        player.user.bosskills += 1
#########Level up####################    
    player.user.xp = player.user.xp + enemy.xp
    print("You gained", enemy.xp, "xp from killing the", enemy.name)
    input()
    os.system("clear")
    if player.user.xp >= player.user.maxp:
        player.user.level += 1
        player.user.xp = 0
        player.user.talent.attack += player.user.talent.lvlupattack
        player.user.talent.armorsum += player.user.talent.lvluparmor
        player.user.talent.maxhealth += player.user.talent.lvluphealth
        print("You have leveled up!")
        print("You are now level", player.user.level)
        input()
        os.system("clear")
        print("You gained:")
        print("+",player.user.talent.lvluphealth, "health. You now have max health of:", player.user.talent.maxhealth)
        print("+",player.user.talent.lvlupattack, "attack. You now have base attack of:", player.user.talent.attack)
        print("+",player.user.talent.lvluparmor, "armor. You now have base armor of:", player.user.talent.armorsum)
        input()
        os.system("clear")
    else:
        print("You now have", player.user.xp, "/", player.user.maxp, "xp")
        input()
        os.system("clear")
#########Level up#################### 
    print("You see something glimmering from the corpse of the", enemy.name,)
    input()
    os.system("clear")
    print("What would you like to do?")
    print("1) Loot")
    print("2) Move forward")
    choice = input("")
    os.system("clear")
    
    if enemy.name == "Kneecrawler" or enemy.name == "Soulmauler" or enemy.name == "Lanklord":
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
                os.system("clear")
                print(f"You currently have a {player.user.weapon.name} ({player.user.weapondamage} damage): Would you like to equip the new weapon? ({lootdrop.attack} attack)")
            elif isinstance(lootdrop, armor.Armor):
                print(f"You found an {lootdrop.name}! ({lootdrop.armorsave} armor)")
                input()
                os.system("clear")
                print(f"You currently have a {player.user.armor.name} ({player.user.armorsave} armor): Would you like to equip the new armor? ({lootdrop.armorsave} armor)")
            
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
                    Arriveplayerzone()
                elif isinstance(lootdrop, armor.Armor):
                    player.user.armor = lootdrop
                    player.user.armorsave = lootdrop.armorsave
                    print(f"You have equipped the {lootdrop.name}!")
                    input()
                    Arriveplayerzone()
                else:
                    print("You have discarded the item.")
                    input()
                    Arriveplayerzone()

        elif choice == "2":
            print("You continue your exploration..")
            input()
            Arriveplayerzone()

        else:
            print("")
            input()
            os.system("clear")
            Arriveplayerzone()

    player.user.waves += 1
    enemy.health = enemy.maxhealth
    player.user.gold += golddrop
    current_talent = player.user.talent.name
    
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
    healed = 0

    player.user.name = ""
    player.user.talent.health = player.user.talent.maxhealth
    player.user.talent.maxhealth = 0 + player.user.talent.maxhealth 
    player.user.exp = 0
    player.user.gold = 0
    player.user.weapon = weapons.Fist
    player.user.weapondamage = player.user.weapon.attack
    player.user.armor = armor.Naked
    player.user.armorsave = player.user.armor.armorsave
    player.user.waves = 0
    player.user.kills = 0
    player.user.bosskills = 0
    player.user.zone = ""
        
#########Dead area####################

##############Combat Area################################

##############Zone Area################################

def zonepick():
    os.system("clear")
    print("Outside the city you have different zones you can go to")
    print("1.) Forest (lvl 1)")
    print("2.) Desert (lvl 5)")
    print("3.) Lankland (lvl 10)")
    option = input("")
    if option == "1":
        if player.user.level >= 1:
            os.system("clear")
            player.user.zone = "Forest"
            print("You decide to go to the forest")
            Arriveforest()
        else:
            os.system("clear")
            print("You need to be level 1 to enter this area!", "( level:", player.user.level, ")")
            input()
            zonepick()
    elif option == "2":
        if player.user.level >= 5:
            os.system("clear")
            player.user.zone = "Desert"
            print("You decide to go to the desert")
            Arrivedesert()
        else:
            os.system("clear")
            print("You need to be level 5 to enter this area!", "( level:", player.user.level, ")")
            input()
            zonepick()
    elif option == "3":
        if player.user.level >= 10:
            os.system("clear")
            player.user.zone = "Lankland"
            print("You decide to go to the lankland")
            Arrivelankland()
        else:
            os.system("clear")
            print("You need to be level 10 to enter this area!", "( level:", player.user.level, ")")
            input()
            zonepick()
    else:
        intro()
        
def Arriveforest():
    os.system("clear")
    print("You arrive at a safespot in the Forest")
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
        Arriveplayerzone()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        Arriveplayerzone()

        
        
        
        
def Arrivedesert():
    os.system("clear")
    print("You arrive at a refreshing osasis in the Desert")
    print("In the Desert you can")
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
        Arriveplayerzone()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        os.system("clear")
        Arriveplayerzone()
        
        
def Arrivelankland():
    os.system("clear")
    print("You arrive at a barren wasteland called Lankland")
    print("In the Lankland you can")
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
        Arriveplayerzone()
    elif option == "5":
        intro()
    try:
        option = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        os.system("clear")
        Arriveplayerzone()
    
    
    
    
def Arriveplayerzone():
    if player.user.zone == "Forest":
        Arriveforest()
    elif player.user.zone == "Desert":
        Arrivedesert()



def Explore():
    os.system("clear")
    print("You decide to explore around")
    input()
    os.system("clear")
    Event = random.randint(1, 100)
    if Event >= 10:
        print("You spot something running at you")
        print("Battle")
        input()
        fight()
    else:
        specialevent = random.randint(1,3)
        if specialevent == 1:
            bossevent()
        elif specialevent == 2:
            shopintro()
        elif specialevent == 3:
            springevent()
        else:
            shopintro()
    
        
        
def bossevent():
    if player.user.zone == "Forest":
            print("You stumble upon an overgrown shrine, deep in the forest...")
            input()
            os.system("clear")
            print("You decide to...")
            print("1.) Explore the shrine")
            print("2.) Leave the place alone")
            option = input("")
            os.system("clear")
            if option == "1":
                outcome = random.randint(1, 100)
                if outcome <= 75:
                    print("You hear some whispering in your head...")
                    input()
                    os.system("clear")
                    print("A shrine guardian appears! It's the Kneecrawler!")
                    bossfight()
                else:
                    print("While looking around, you find a chest, long forgotten...")
                    input()
                    os.system("clear")
                    print("You decide to...")
                    print()
                    print("1.) Try to open it")
                    print("2.) Leave it be")
                    chestopt = input("")
                    os.system("clear")
                    if chestopt == "1":
                        randomizer = random.randint(1,100)
                        if randomizer <= 50:
                            legendaryarmor= random.choice(armor.lege_armorlist)
                            print("You found a legendary armor: The", legendaryarmor.name, "( ", legendaryarmor.armorsave, "armor )" )
                            input("")
                            os.system("clear")
                            print("You currently have ", player.user.armor.name, "(",player.user.armorsave,"armor)", "Would you like to equip the new armor?")
                            print()
                            print("1.) Yes")
                            print("2.) No")
                            option = input("")
                            os.system("clear")
                            if option == "1":
                                player.user.armor = legendaryarmor
                                player.user.armorsave = legendaryarmor.armorsave
                                print("You have equipped the", legendaryarmor.name, "( ", legendaryarmor.armorsave, "armor )")
                                input()
                                os.system("clear")
                                print("Leave this place alone, before you anger the gods...")
                                Arriveplayerzone()
                            else:
                                Explore()
                        else:
                            legendaryweapon = random.choice(weapons.lege_weaponlist)
                            print("You found a legendary weapon: The", legendaryweapon.name, "( ", legendaryweapon.attack, "damage)")
                            input()
                            os.system("clear")
                            print("You currently have ", player.user.weapon.name," (", player.user.weapondamage, "damage)" " would you like to equip the new weapon?")
                            print()
                            print("1.) Yes")
                            print("2.) No")
                            option = input("")
                            os.system("clear")
                            if option == "1":
                                player.user.weapon = legendaryweapon
                                player.user.weapondamage = legendaryweapon.attack
                                print("You have equipped the", legendaryweapon.name, "( ", legendaryweapon.attack, "damage)")
                                input()
                                os.system("clear")
                                print("Leave this place alone, before you anger the gods...")
                                Arriveplayerzone()
                            else:
                                Explore()
            elif option == "2":
                Arriveplayerzone()
        
        
        
    elif player.user.zone == "Desert":
        print("You stumble upon an underground pyramid, showing through the sand...")
        input()
        os.system("clear")
        print("You decide to...")
        print("")
        print("1.) Explore the pyramid")
        print("2.) Leave the place alone")
        option = input("")
        os.system("clear")
        if option == "1":
            outcome = random.randint(1, 100)
            if outcome <= 75:
                print("You hear some whispering in your head...")
                input()
                os.system("clear")
                print("A pyramid sentinel appears! It's the Soulmauler!")
                bossfight()
            else:
                print("While looking around, you find a chest, long forgotten...")
                input()
                os.system("clear")
                print("You decide to...")
                print()
                print("1.) Try to open it")
                print("2.) Leave it be")
                chestopt = input("")
                os.system("clear")
                if chestopt == "1":
                    randomizer = random.randint(1,100)
                    if randomizer <= 50:
                        legendaryarmor= random.choice(armor.lege_armorlist)
                        print("You found a legendary armor: The", legendaryarmor.name, "( ", legendaryarmor.armorsave, "armor )" )
                        input("")
                        os.system("clear")
                        print("You currently have", player.user.armor.name, "(",player.user.armorsave,"armor)", "Would you like to equip the new armor?", "( ", legendaryarmor.armorsave, "armor )")
                        print()
                        print("1.) Yes")
                        print("2.) No")
                        option = input("")
                        os.system("clear")
                        if option == "1":
                            player.user.armor = legendaryarmor
                            player.user.armorsave = legendaryarmor.armorsave
                            print("You have equipped the", legendaryarmor.name, "( ", legendaryarmor.armorsave, "armor )")
                            input()
                            os.system("clear")
                            print("Leave this place alone, before you anger the gods...")
                            Arriveplayerzone()
                        else:
                            Explore()
                    else:
                        legendaryweapon = random.choice(weapons.lege_weaponlist)
                        print("You found a legendary weapon: The", legendaryweapon.name, "( ", legendaryweapon.attack, "damage)")
                        input()
                        os.system("clear")
                        print("You currently have", player.user.weapon.name," (", player.user.weapondamage, "damage)" " would you like to equip the new weapon?", "( ", legendaryweapon.attack, "damage)")
                        print()
                        print("1.) Yes")
                        print("2.) No")
                        option = input("")
                        os.system("clear")
                        if option == "1":
                            player.user.weapon = legendaryweapon
                            player.user.weapondamage = legendaryweapon.attack
                            print("You have equipped the", legendaryweapon.name, "( ", legendaryweapon.attack, "damage)")
                            input()
                            os.system("clear")
                            print("Leave this place alone, before you anger the gods...")
                            Arriveplayerzone()
                        else:
                            Explore()
        elif option == "2":
            Arriveplayerzone()
    
    elif player.user.zone == "Lankland":
        print("You stumble upon an defiled mansion, giving you an eerie feeling...")
        input()
        os.system("clear")
        print("You decide to...")
        print("")
        print("1.) Explore the mansion")
        print("2.) Leave the place alone")
        option = input("")
        os.system("clear")
        if option == "1":
            outcome = random.randint(1, 100)
            if outcome <= 75:
                print("You can feel something choking you...")
                input()
                os.system("clear")
                print("A mansion beast appears! It's the Lanklord!")
                bossfight()
            else:
                print("While looking around, you find a chest, long forgotten...")
                input()
                os.system("clear")
                print("You decide to...")
                print()
                print("1.) Try to open it")
                print("2.) Leave it be")
                chestopt = input("")
                os.system("clear")
                if chestopt == "1":
                    randomizer = random.randint(1,100)
                    if randomizer <= 50:
                        legendaryarmor= random.choice(armor.lege_armorlist)
                        print("You found a legendary armor: The", legendaryarmor.name, "( ", legendaryarmor.armorsave, "armor )" )
                        input("")
                        os.system("clear")
                        print("You currently have", player.user.armor.name, "(",player.user.armorsave,"armor)", "Would you like to equip the new armor?", "( ", legendaryarmor.armorsave, "armor )")
                        print()
                        print("1.) Yes")
                        print("2.) No")
                        option = input("")
                        os.system("clear")
                        if option == "1":
                            player.user.armor = legendaryarmor
                            player.user.armorsave = legendaryarmor.armorsave
                            print("You have equipped the", legendaryarmor.name, "( ", legendaryarmor.armorsave, "armor )")
                            input()
                            os.system("clear")
                            print("Leave this place alone, before you anger the gods...")
                            Arriveplayerzone()
                        else:
                            Explore()
                    else:
                        legendaryweapon = random.choice(weapons.lege_weaponlist)
                        print("You found a legendary weapon: The", legendaryweapon.name, "( ", legendaryweapon.attack, "damage)")
                        input()
                        os.system("clear")
                        print("You currently have", player.user.weapon.name," (", player.user.weapondamage, "damage)" " would you like to equip the new weapon?", "( ", legendaryweapon.attack, "damage)")
                        print()
                        print("1.) Yes")
                        print("2.) No")
                        option = input("")
                        os.system("clear")
                        if option == "1":
                            player.user.weapon = legendaryweapon
                            player.user.weapondamage = legendaryweapon.attack
                            print("You have equipped the", legendaryweapon.name, "( ", legendaryweapon.attack, "damage)")
                            input()
                            os.system("clear")
                            print("Leave this place alone, before you anger the gods...")
                            Arriveplayerzone()
                        else:
                            Explore()
        elif option == "2":
            Arriveplayerzone()
    
    
def springevent():
    print("While exploring you found a holy spring")
    print("You decide to")
    print("1.) Drink it")
    print("2.) Rest near it")
    print("3.) Ignore it and leave")
    option = input("")
    os.system("clear")
    if option == "1":
        if player.user.talent.health == player.user.talent.maxhealth:
            print("You are at max health and cannot heal")
            input()
            os.system("clear")
            Arriveplayerzone()
        else:
            waterhealth = random.randint(1, 10)
            print("You decide to drink from the spring and continue on your way")
            player.user.talent.health = player.user.talent.health + waterhealth
            if player.user.talent.health >= player.user.talent.maxhealth:
                player.user.talent.health = player.user.talent.maxhealth
            input()
            os.system("clear")
            print("The refreshing water healed you for", waterhealth, "hp")
            Arriveplayerzone()
    elif option == "2":
        print("You tried to rest but the noise of the spring annoyed you")
        input()
        os.system("clear")
        Arriveplayerzone()
    elif option == "3":
        print("You ignore the spring and leave")
        input()
        os.system("clear")
        Arriveplayerzone()
    else:
        Arriveplayerzone()
        
            
        

##############Zone Area################################











main()