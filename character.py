# character.py

class Character:
    def __init__(self, name, character_type):
        self.name = name
        self.character_type = character_type
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def compare_weapon(self, new_weapon, attribute_weights):
        from compare_items import compare_items
        return compare_items(self, new_weapon, attribute_weights)




