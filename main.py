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

    # Create a notebook (tab control)
    notebook = ttk.Notebook(root)
    notebook.pack()

    # Create the first tab
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Compare Weapons")

    # Create a dropdown menu for the character type selection
    character_types = ["Barbarian", "Druid", "Necromancer", "Rouge", "Sorceress"]
    character_type = tk.StringVar()
    character_type.set(character_types[0])  # set the default option
    character_type_menu = ttk.Combobox(tab1, textvariable=character_type, values=character_types)
    character_type_menu.pack()

    # Create an entry field for the DPS value
    dps_value_entry = tk.Entry(tab1)
    dps_value_entry.pack()

    # Create an entry field for the number of sockets
    sockets_entry = tk.Entry(tab1)
    sockets_entry.pack()

    # Create dropdown menus for the user to select the attributes of the weapon
    attribute1 = tk.StringVar()
    attribute1_menu = ttk.Combobox(tab1, textvariable=attribute1)
    attribute1_menu.pack()

    attribute2 = tk.StringVar()
    attribute2_menu = ttk.Combobox(tab1, textvariable=attribute2)
    attribute2_menu.pack()

    attribute3 = tk.StringVar()
    attribute3_menu = ttk.Combobox(tab1, textvariable=attribute3)
    attribute3_menu.pack()

    attribute4 = tk.StringVar()
    attribute4_menu = ttk.Combobox(tab1, textvariable=attribute4)
    attribute4_menu.pack()

    attribute5 = tk.StringVar()
    attribute5_menu = ttk.Combobox(tab1, textvariable=attribute5)
    attribute5_menu.pack()


    # Update the attribute dropdown menus when the character type selection changes
    def update_attributes(*args):
        attributes = weapon_attributes.default_attributes + weapon_attributes.class_attributes.get(character_type.get(), [])
        attribute1.set(attributes[0])
        attribute1_menu['values'] = attributes
        attribute2.set(attributes[0])
        attribute2_menu['values'] = attributes
        attribute3.set(attributes[0])
        attribute3_menu['values'] = attributes
        attribute4.set(attributes[0])
        attribute4_menu['values'] = attributes
        attribute5.set(attributes[0])
        attribute5_menu['values'] = attributes


    character_type.trace('w', update_attributes)

    # Create a button to compare the new weapon with the currently equipped weapon
    compare_button = tk.Button(tab1, text="Compare", command=lambda: compare_weapons(character_type.get(), dps_value_entry.get(), sockets_entry.get(), attribute1.get(), attribute2.get(), attribute3.get(), attribute4.get(), attribute5.get()))
    compare_button.pack()

    # Create the second tab
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Set Weights")

    # Create entry fields for the user to set the weights
    weight1_entry = tk.Entry(tab2)
    weight1_entry.pack()

    weight2_entry = tk.Entry(tab2)
    weight2_entry.pack()

    weight3_entry = tk.Entry(tab2)
    weight3_entry.pack()

    weight4_entry = tk.Entry(tab2)
    weight4_entry.pack()

    weight5_entry = tk.Entry(tab2)
    weight5_entry.pack()

    # Start the Tk event loop
    root.mainloop()

def compare_weapons(character_type, dps_value, sockets, attribute1, attribute2, attribute3, attribute4, attribute5):
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
    }

    # Compare the two weapons with the attribute weights
    result = char.compare_weapon(new_weapon, attribute_weights)

    print(result)

if __name__ == "__main__":
    main()
