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
    character_type_label = tk.Label(tab1, text="Character Type:")
    character_type_label.grid(row=0, column=0)
    character_type_menu = ttk.Combobox(tab1, textvariable=character_type, values=character_types)
    character_type_menu.grid(row=0, column=1)

    # Create an entry field for the DPS value
    dps_value_label = tk.Label(tab1, text="DPS Value:")
    dps_value_label.grid(row=1, column=0)
    dps_value_entry = tk.Entry(tab1)
    dps_value_entry.grid(row=1, column=1)

    # Create an entry field for the number of sockets
    sockets_label = tk.Label(tab1, text="Sockets:")
    sockets_label.grid(row=2, column=0)
    sockets_entry = tk.Entry(tab1)
    sockets_entry.grid(row=2, column=1)

    # Create dropdown menus and entry fields for the user to select the attributes of the weapon and enter their values
# Create dropdown menus for the user to select the attributes of the weapon
    attributeC = tk.StringVar()
    attributeC_label = tk.Label(tab1, text="Core Attribute:")
    attributeC_label.grid(row=3, column=0)
    attributeC_menu = ttk.Combobox(tab1, textvariable=attributeC)
    attributeC_menu.grid(row=3, column=1)
    attributeC_value_label = tk.Label(tab1, text="Value:")
    attributeC_value_label.grid(row=3, column=2)
    attributeC_value = tk.Entry(tab1)
    attributeC_value.grid(row=3, column=3)

    attribute1 = tk.StringVar()
    attribute1_label = tk.Label(tab1, text="Attribute 1:")
    attribute1_label.grid(row=4, column=0)
    attribute1_menu = ttk.Combobox(tab1, textvariable=attribute1)
    attribute1_menu.grid(row=4, column=1)
    attribute1_value_label = tk.Label(tab1, text="Value:")
    attribute1_value_label.grid(row=4, column=2)
    attribute1_value = tk.Entry(tab1)
    attribute1_value.grid(row=4, column=3)

    attribute2 = tk.StringVar()
    attribute2_label = tk.Label(tab1, text="Attribute 2:")
    attribute2_label.grid(row=5, column=0)
    attribute2_menu = ttk.Combobox(tab1, textvariable=attribute2)
    attribute2_menu.grid(row=5, column=1)
    attribute2_value_label = tk.Label(tab1, text="Value:")
    attribute2_value_label.grid(row=5, column=2)
    attribute2_value = tk.Entry(tab1)
    attribute2_value.grid(row=5, column=3)

    attribute3 = tk.StringVar()
    attribute3_label = tk.Label(tab1, text="Attribute 3:")
    attribute3_label.grid(row=6, column=0)
    attribute3_menu = ttk.Combobox(tab1, textvariable=attribute3)
    attribute3_menu.grid(row=6, column=1)
    attribute3_value_label = tk.Label(tab1, text="Value:")
    attribute3_value_label.grid(row=6, column=2)
    attribute3_value = tk.Entry(tab1)
    attribute3_value.grid(row=6, column=3)

    attribute4 = tk.StringVar()
    attribute4_label = tk.Label(tab1, text="Attribute 4:")
    attribute4_label.grid(row=7, column=0)
    attribute4_menu = ttk.Combobox(tab1, textvariable=attribute4)
    attribute4_menu.grid(row=7, column=1)
    attribute4_value_label = tk.Label(tab1, text="Value:")
    attribute4_value_label.grid(row=7, column=2)
    attribute4_value = tk.Entry(tab1)
    attribute4_value.grid(row=7, column=3)


    # Update the attribute dropdown menus when the character type selection changes
    def update_attributes(*args):
        attributes = weapon_attributes.default_attributes + weapon_attributes.class_attributes.get(character_type.get(), [])
        attributeC.set(attributes[0])
        attributeC_menu['values'] = attributes
        attribute1.set(attributes[0])
        attribute1_menu['values'] = attributes
        attribute2.set(attributes[0])
        attribute2_menu['values'] = attributes
        attribute3.set(attributes[0])
        attribute3_menu['values'] = attributes
        attribute4.set(attributes[0])
        attribute4_menu['values'] = attributes


    character_type.trace('w', update_attributes)

    # Create a button to compare the new weapon with the currently equipped weapon
    compare_button = tk.Button(tab1, text="Compare", command=lambda: compare_weapons(character_type.get(), dps_value_entry.get(), sockets_entry.get(), attributeC.get(), attribute1.get(), attribute2.get(), attribute3.get(), attribute4.get()))
    compare_button.grid(row=10, column=0)

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

def compare_weapons(character_type, dps_value, sockets, attributeC, attribute1, attribute2, attribute3, attribute4):
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
        "DPS value": 5,
        "Sockets": 5,
        attributeC.get(): int(attribute1_value.get()),
        attribute1.get(): int(attribute2_value.get()),
        attribute2.get(): int(attribute1_value.get()),
        attribute3.get(): int(attribute2_value.get()),
        attribute4.get(): int(attribute1_value.get()),
    }

    # Compare the two weapons with the attribute weights
    result = char.compare_weapon(new_weapon, attribute_weights)

    print(result)

if __name__ == "__main__":
    main()
