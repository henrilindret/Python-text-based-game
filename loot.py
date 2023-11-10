import random
import enemies
import weapons
import armor


class Loot:
    def __init__(self, name, gold, loot_id):
        self.name = name
        self.gold = gold
        self.loot_id = loot_id
        
def goblin_loot():
    loot_id = 1
    gob_loot_common = ["Stick", "Dagger"]
    gob_loot_rare = ["Iron sword"]
    gob_loot_epic = []
    
    
    drop_chance = random.randint(1,100)
    
    if drop_chance <= 5:
        return Loot(name =random.choice(gob_loot_rare), gold = random.randint(1,5))
    else:
        return Loot(name = random.choice(gob_loot_common), gold = random.randint(1,5))