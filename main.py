import json
import tkinter as tk
from tkinter import ttk
from character import Character
from item import Item
from user_input import get_item_from_user
from compare_items import compare_items
import weapon_attributes

def main():
    # Create a new Tk root window
    root = tk.Tk()

    # Set the title of the window
    root.title("Item Compare Tool")

    # Create a dropdown menu for the character type selection
    character_types = ["Barbarian", "Druid", "Necromancer", "Rouge", "Sorceress"]
    character_type = tk.StringVar()
    character_type.set(character_types[0])  # set the default option
    character_type_menu = ttk.Combobox(root, textvariable=character_type, values=character_types)
    character_type_menu.pack()

    # Create an entry field for the DPS value
    dps_value_entry = tk.Entry(root)
    dps_value_entry.pack()

    # Create an entry field for the number of sockets
    sockets_entry = tk.Entry(root)
    sockets_entry.pack()

    # Create dropdown menus for the user to select the attributes of the weapon
    attributes = weapon_attributes.default_attributes + weapon_attributes.class_attributes.get(character_type, [])
    attribute1 = tk.StringVar()
    attribute1.set(attributes[0])  # set the default option
    attribute1_menu = ttk.Combobox(root, textvariable=attribute1, values=attributes)
    attribute1_menu.pack()

    attribute2 = tk.StringVar()
    attribute2.set(attributes[0])  # set the default option
    attribute2_menu = ttk.Combobox(root, textvariable=attribute2, values=attributes)
    attribute2_menu.pack()

    attribute3 = tk.StringVar()
    attribute3.set(attributes[0])  # set the default option
    attribute3_menu = ttk.Combobox(root, textvariable=attribute2, values=attributes)
    attribute3_menu.pack()

    attribute4 = tk.StringVar()
    attribute4.set(attributes[0])  # set the default option
    attribute4_menu = ttk.Combobox(root, textvariable=attribute2, values=attributes)
    attribute4_menu.pack()

    attribute5 = tk.StringVar()
    attribute5.set(attributes[0])  # set the default option
    attribute5_menu = ttk.Combobox(root, textvariable=attribute2, values=attributes)
    attribute5_menu.pack()

    # Create a button to compare the new weapon with the currently equipped weapon
    compare_button = tk.Button(root, text="Compare", command=lambda: compare_weapons(character_type.get(), dps_value_entry.get(), sockets_entry.get(), attribute1.get(), attribute2.get()))
    compare_button.pack()

    # Start the Tk event loop
    root.mainloop()

def compare_weapons(character_type, dps_value, sockets, attribute1, attribute2):
    # Create a character
    char = Character('MyCharacter', character_type)

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
        "DPS value": int(dps_value),
        "Sockets": int(sockets),
        attribute1: 3,
        attribute2: 3,
    }

    # Compare the two weapons with the attribute weights
    result = char.compare_weapon(new_weapon, attribute_weights)

    print(result)

if __name__ == "__main__":
    main()
