class Spell:
    def __init__(self, name, manacost, damage, defence, spelllevel, spellxp, spellmaxp, spellid, gold):
        self.name = name
        self.manacost = manacost
        self.damage = damage
        self.defence = defence
        self.spelllevel = spelllevel
        self.spellxp = spellxp
        self.spellmaxp = spellmaxp
        self.spellid = spellid
        self.gold = gold


Mana_blast = Spell("Mana blast", 20, 15, 1, 1, 1, 100, 1, 100)
Fire_blast= Spell("Fire blast", 30, 15, 1, 1, 2, 100, 2, 100)
Shadow_cloak = Spell("Shadow cloak", 30, 0, 5, 2, 3, 100, 3, 100)
Ice_blast = Spell("Ice blast", 40, 20, 1, 1, 1, 100, 4, 100)
lightning_strike = Spell("Lightning strike", 50, 25, 1, 1, 5, 100, 5, 100)
Capillary_burst = Spell("Capillary burst", 60, 30, 1, 1, 6, 100, 6, 100)
magic_barrier = Spell("Magic barrier", 70, 0, 10, 1, 1, 100, 7, 100)
life_drain = Spell("Life drain", 80, 40, 1, 1, 1, 100, 8, 100)


spelllist = [Mana_blast, Fire_blast, Shadow_cloak, Ice_blast, lightning_strike, Capillary_burst, magic_barrier, life_drain]


damagespelllist = [Mana_blast, Fire_blast, Ice_blast, lightning_strike, Capillary_burst, life_drain]

defencespelllist = [Shadow_cloak, magic_barrier]