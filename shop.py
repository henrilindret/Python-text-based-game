import weapons
import player


def shop1():
    print("Welcome to the shop")
    print("You currently have", player.Player.gold, "Gold")
    print("The shop is currently selling")
    for wep in weapons.weaponlist:
        print(wep.name, wep.gold)
    print("What would you like to buy?")
    option = int(input())
    for wep in weapons.weaponlist:
        if wep == player.Player.weapon and option == wep.weapon_id:
            print("You have already bought this item")
            shop1()
        elif wep.weapon_id == option and player.Player.gold >= wep.gold:
            print(wep.name + " purchased")
            player.Player.gold = player.Player.gold - wep.gold
            print("You currently have", player.Player.gold, "Gold left")
            player.Player.weapon = wep
            player.Player.attack = wep.attack
            return
