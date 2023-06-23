# weapon_attributes.py
# Note that this is just an example and you might need to adjust it according to your game

default_attributes = [
    "All Stats",
    "Critical Strike Damage",
    "Overpower Damage",
    "Vulnerable Damage",
    "Damage Over Time",
    "Damage to Close Enemies",
    "Damage to Crowd Controlled Enemies",
    "Damage to Distant Enemies",
    "Damage to Injured Enemies",
    "Damage to Slowed Enemies",
    "Damage to Stunned Enemies",
    "Basic Skill Damage",
    "Core Skill Damage",
    "Ultimate Skill Damage",
    "Lucky Hit: Up to [X] Chance to Execute Injured Non-Elites",
    "Socket",
    "DPS"
]

class_attributes = {
    "barb" : [
        "Strength",
        "Damage while Berserking",
        "Damage to Bleeding Enemies"  
    ],
    
    "druid": [
        "Willpower",
        "Overpower Damage with Werebear Skills",
        "Critical Strike Damage with Earth Skills",
        "Critical Strike Damage with Werewolf Skills",
        "Lightning Critical Strike Damage",
        "Damage to Poisoned Enemies"
    ],

    "necro" : [
        "Intelligence",
        "Critical Strike Damage with Bone Skills",
        "Damage to Affected by Shadow Damage Over Time Enemies"
    ],
    
    "rouge" : [
        "Dexterity"
        "Critical Strike Damage with Imbued Skills",
        "Damage to Chilled Enemies",
        "Damage to Dazed Enemies",
        "Damage to Frozen Enemies",
        "Damage to Poisoned Enemies",
        "Damage to Enemies Affected by Trap Skills" 
    ],

    "sorceress" : [
        "Intelligence",
        "Lightning Critical Strike Damage",
        "Damage to Burning Enemies",
        "Damage to Chilled Enemies",
        "Damage to Frozen Enemies",
    ]
}
