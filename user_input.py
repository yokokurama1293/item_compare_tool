# user_input.py

from item import Item
import weapon_attributes

def get_item_from_user():
    name = input("Enter the name of the item: ")
    class_name = input("Enter your class: ")

    # Combine default attributes and class-specific attributes
    all_attributes = weapon_attributes.default_attributes + weapon_attributes.class_attributes.get(class_name, [])

    print("Enter the attributes for this item. When you're done, type 'done'.")
    dps_value = int(input("Enter the DPS value: "))

    attributes = {
        "DPS value": dps_value,
    }

    sockets = input("Enter the number of sockets (0-2): ")
    if sockets.isdigit() and int(sockets) in range(3):
        attributes["Sockets"] = int(sockets)
    else:
        print("Invalid number of sockets. Setting it to 0.")
        attributes["Sockets"] = 0

    print("Enter the core attribute for this item:")
    while True:
        core_attr = input("Enter the core attribute: ")
        if core_attr in all_attributes:
            break
        print("Invalid attribute. Please try again.")

    value = input(f"Enter the value of {core_attr}: ")
    attributes[core_attr] = float(value)

    print("Enter the secondary attributes for this item:")
    i = 1
    while i <= 4:
        attr = input(f"Enter attribute {i}: ")
        if attr.lower() == 'done':
            break
        if attr not in all_attributes:
            print("Invalid attribute. Please try again.")
            continue
        value = input(f"Enter the value of {attr}: ")
        attributes[attr] = float(value)
        i += 1

    return Item(name, attributes)





