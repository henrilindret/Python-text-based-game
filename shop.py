import weapons
import player


def shop1():
    print("Welcome to the shop")
    print("You currently have", player.user.gold, "Gold")
    print("The shop is currently selling")
    for wep in weapons.weaponlist:
        print(wep.name, wep.gold)
    print("What would you like to buy?")
    option = int(input())
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
            player.user.attack = wep.attack
            input()
            return
