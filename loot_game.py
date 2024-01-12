import loot
import enemies
import weapons
import armor
import player

def win():
    print("You defeated the", enemy.name)
    print()
    print("What would you like to do?")
    input()
    print("1. Loot")
    print("2. Move forward")
    option = input("->")
    if option == "1":
       loot_item = goblin_loot()
        
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