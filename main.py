import json
from character import Character
from item import Item
from user_input import get_item_from_user
from compare_items import compare_items

# Create a character
char = Character('MyCharacter', 'druid')

# Equip a weapon from a file
weapon = Item.from_file('weapon.json', 'Moonlight')
if weapon is None:
    print("Item 'Moonlight' not found.")
else:
    char.equip_weapon(weapon)

# Get a new weapon from the user
new_weapon = get_item_from_user()

# Define the attribute weights
attribute_weights = {
    "DPS value": 5,
    "Sockets": 5,
    "Critical Strike Damage": 4,
    "Critical Strike Damage with Earth Skills": 4,
    "Vulnerable Damage": 3,
    "Core Skill Damage": 3,
    "Damage to Injured Enemies": 3,
    "Damage to Crowd Controlled Enemies": 3,
    "Overpower Damage": 3,
    "Willpower": 3,
}

# Compare the two weapons with the attribute weights
result = char.compare_weapon(new_weapon, attribute_weights)

print(result)
