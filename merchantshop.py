class Tome:
    def __init__(self, name, health, gold, damage, armor, item_id):
        self.name = name
        self.health = health
        self.gold = gold
        self.damage = damage
        self.armor = armor
        self.item_id = item_id
        
tome_of_health = Tome("Tome of Health", 10, 500, 0, 0, 1)
tome_of_strength = Tome("Tome of Strength", 0, 500, 5, 0, 2)
tome_of_armor = Tome("Tome of Armor", 0, 500, 0, 5, 3)

tomelist = [tome_of_health, tome_of_strength, tome_of_armor]
    