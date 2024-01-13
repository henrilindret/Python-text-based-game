import player
import os
import merchantshop

def shop():
    os.system("cls")
    print("Welcome to the shadiest shop in the world har har")

    if not player.user.merchantpay:
        print("To look at my really suspicious wares you have to pay me 20 gold")
        print("Would you like to?")
        print("You currently have", player.user.gold, "Gold")
        print("1) yes")
        print("2) no")
        option = input()
        os.system("cls")
        if option == "1" and player.user.gold >= 20:
            player.user.gold -= 20
            player.user.merchantpay = True
            os.system("cls")
        elif option == "1" and player.user.gold < 20:
            print("You do not have enough money and leave")
            input()
            os.system("cls")
            return
        elif option == "2":
            print("You decide not to pay and leave")
            input()
            os.system("cls")
            return
        else:
            print("you leave")
            return

    print("You currently have", player.user.gold, "Gold left")
    print("You won't be disappointed ;)")
    print("Here's what I have right now")
    for item in merchantshop.tomelist:
        print(item.item_id, item.name, ": cost", item.gold)

    print("What would you like to buy?")
    print("If you wish to leave, write '100'")
    try:
        pick = int(input())
    except ValueError:
        print("Please enter a valid number")
        input()
        os.system("cls")
        shop()

    if pick == 100:
        player.user.merchantpay = False
        return

    for item in merchantshop.tomelist:
        if pick == item.item_id and player.user.gold >= item.gold:
            if pick == 1:
                print("You have bought Tome of health")
                player.user.talent.maxhealth += item.health
                player.user.gold -= item.gold
                print("Your max health has increased by 10")
            elif pick == 2:
                print("You have bought Tome of strength")
                player.user.basedamage += item.damage
                player.user.gold -= item.gold
                print("Your base damage has increased by 5")
            elif pick == 3:
                print("You have bought Tome of armor")
                player.user.basearmor += item.armor
                player.user.gold -= item.gold
                print("Your base armor has increased by 5")
            input()
            shop()
