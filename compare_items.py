# compare_items.py
from item import Item

# basic comparison
# def compare_items(character, new_item, weights):
#     if character.weapon is None:
#         return f"{character.name} currently has no weapon equipped."

#     current_weapon_score = sum(character.weapon.attributes.get(attr, 0) * weight for attr, weight in weights.items())
#     new_weapon_score = sum(new_item.attributes.get(attr, 0) * weight for attr, weight in weights.items())

#     if new_weapon_score > current_weapon_score:
#         return f"The new weapon ({new_item.name}) is better than the currently equipped weapon."
#     elif new_weapon_score < current_weapon_score:
#         return f"The new weapon ({new_item.name}) is worse than the currently equipped weapon."
#     else:
#         return f"The new weapon ({new_item.name}) is equivalent to the currently equipped weapon."

# detailed comparison
def compare_items(character, new_item, weights):
    if character.weapon is None:
        return f"{character.name} currently has no weapon equipped."

    current_weapon_attributes = character.weapon.attributes
    new_weapon_attributes = new_item.attributes

    current_weapon_score = 0
    new_weapon_score = 0
    breakdown = ""

    # Lists to store matching attributes, values, and weights
    matching_attrs = []
    current_values = []
    new_values = []
    weights_values = []

# Create a set of all attributes from both weapons
    all_attributes = set(current_weapon_attributes.keys()).union(new_weapon_attributes.keys())

    for attr in all_attributes:
        weight = weights.get(attr, 0)  # Use a default weight of 0 for attributes not in the weights dictionary

        if attr == "DPS value":
            current_dps = current_weapon_attributes.get(attr, 0)
            new_dps = new_weapon_attributes.get(attr, 0)
            current_weapon_score += current_dps * weight
            new_weapon_score += new_dps * weight
            matching_attrs.append(attr)
            current_values.append(current_dps)
            new_values.append(new_dps)
            weights_values.append(weight)

        current_value = current_weapon_attributes.get(attr, 0)
        new_value = new_weapon_attributes.get(attr, 0)

        current_weapon_score += current_value * weight
        new_weapon_score += new_value * weight

        if current_value != 0 or new_value != 0:
            matching_attrs.append(attr)
            current_values.append(current_value)
            new_values.append(new_value)
            weights_values.append(weight)

    breakdown += "Breakdown:\n"

    # Include DPS value in the breakdown
    # dps_index = matching_attrs.index("DPS value")
    # breakdown += f"DPS value:\n"
    # breakdown += f"  Current weapon: {current_values[dps_index]}\n"
    # breakdown += f"  New weapon: {new_values[dps_index]}\n"
    # breakdown += f"  Weight: {weights_values[dps_index]}\n"

    for i in range(len(matching_attrs)):
        attr = matching_attrs[i]
        current_value = current_values[i]
        new_value = new_values[i]
        weight = weights_values[i]

        breakdown += f"{attr}:\n"
        breakdown += f"  Current weapon: {current_value}\n"
        breakdown += f"  New weapon: {new_value}\n"
        breakdown += f"  Weight: {weight}\n"
        breakdown += "\n"

    breakdown += f"Current weapon score: {current_weapon_score}\n"
    breakdown += f"New weapon score: {new_weapon_score}\n"

    if new_weapon_score > current_weapon_score:
        result = f"The new weapon ({new_item.name}) is better than the currently equipped weapon ({character.weapon.name})."
    elif new_weapon_score < current_weapon_score:
        result = f"The new weapon ({new_item.name}) is worse than the currently equipped weapon ({character.weapon.name})."
    else:
        result = f"The new weapon ({new_item.name}) is equivalent to the currently equipped weapon ({character.weapon.name})."

    return f"{result}\n\n{breakdown}"





