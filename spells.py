class Spell:
    def __init__(self, name, manacost, damage, manatalent, spell_id):
        self.name = name
        self.manacost = manacost
        self.damage = damage
        self.manatalent = manatalent
        self.spell_id = spell_id


Mana_blast = Spell("Mana blast", 20, 15, 1 or 2, 1)
Fire_blast= Spell("Fire blast", 30,15, 1 or 2, 2)

spelllist = [Mana_blast, Fire_blast]