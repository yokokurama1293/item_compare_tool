import json
import tkinter as tk
import customtkinter
from character import Character
from item import Item
from user_input import get_item_from_user
from compare_items import compare_items

# System Settings
customtkinter.set_appearance_mode("System")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")

def main():
    # Create a new Tk root window
    root = tk.Tk()

    # Set the title of the window
    root.title("Item Compare Tool")

    # Create a label and add it to the window
    label = tk.Label(root, text="Welcome to the Item Compare Tool!")
    label.pack()

    # Start the Tk event loop
    root.mainloop()

if __name__ == "__main__":
    main()

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
