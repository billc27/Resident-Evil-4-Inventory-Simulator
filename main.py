# Main Program
from Inventory import Inventory
from Item import Item
import random

# Inventory Initialization
print("Welcome to Resident Evil 4 Inventory Simulator")
inventory_col = int(input("Please input the desired number of columns for the inventory: "))
inventory_row = int(input("Please input the desired number of rows for the inventory: "))
user_inventory = Inventory(inventory_col, inventory_row)

# Common Resident Evil 4 Items
broken_butterfly = Item("01", "Broken Butterfly", 4, 2)
tmp = Item("02", "TMP", 3, 2)
rifle = Item("03", "Rifle", 8, 1)
rifle_sa = Item("04", "Rifle (Semi Auto)", 7, 2)
striker = Item("05", "Striker", 5, 2)
black_tail = Item("06", "Blacktail", 3, 2)
incendiary_grenade = Item("07", "Incendiary Grenade", 1, 2)
hand_grenade = Item("08", "Hand Grenade", 1, 2)
flash_grenade = Item("09", "Flash Grenade", 1, 2)
handgun_ammo = Item("10", "Handgun Ammo", 2, 1)
tmp_ammo = Item("11", "TMP Ammo", 2, 1)
magnum_ammo = Item("12", "Magnum Ammo", 2, 1)
rifle_ammo = Item("13", "Rifle Ammo", 2, 1)
shotgun_shells = Item("14", "Shotgun Shells", 2, 1)
herb = Item("15", "Herb", 1, 2)
mixed_herb = Item("16", "Mixed Herb", 1, 2)
scope_r = Item("17", "Scope (Rifle)", 3, 1)
stock_tmp = Item("18", "Stock (TMP)", 2, 2)
first_aid_spray = Item("19", "First Aid Spray", 1, 2)
chicken_egg = Item("20", "Chicken Egg", 1, 1)
available_re_items = [broken_butterfly, tmp, rifle, rifle_sa, striker, black_tail, incendiary_grenade, hand_grenade, flash_grenade, handgun_ammo, tmp_ammo, magnum_ammo, rifle_ammo, shotgun_shells, herb, mixed_herb, scope_r, stock_tmp, first_aid_spray, chicken_egg]

# Items Acquired by User
items = []
id_count = 21

user_continue_choice = True
while (user_continue_choice):
    # Ask the user to enter the item's width and height
    get_item_choice_valid = False
    while (not get_item_choice_valid):
        get_item_choice = input("Do you want to get random items (y/n): ")
        if (get_item_choice == "y"):
            random_item = random.choice(available_re_items)
            print("Acquired", random_item.get_name())
            print("Item ID:", random_item.get_id())
            print("Item size:", random_item.get_width(), "x", random_item.get_height())
            
            get_item_choice_valid = True

            # Item Placement
            user_inventory.printInventory()

            # Rotate Choice
            rotate_choice_valid = False
            while (not rotate_choice_valid):
                rotate_choice = input("Do you want to rotate the item (y/n): ")
                if (rotate_choice == "y"):
                    random_item.rotate_item()
                    print("Item rotated successfully!")
                    rotate_choice_valid = True
                elif (rotate_choice == "n"):
                    rotate_choice_valid = True
                else:
                    print("Input invalid. Please try again!")
            
            items.append(random_item) # Add to items
            start_point_valid = False
            while (not start_point_valid):
                print("Choose the starting point for the item placement!")
                desired_row = int(input("Row: "))
                desired_col = int(input("Column: "))
                if (isinstance(desired_row, int) and isinstance(desired_col, int)):
                    # Placement
                    if (user_inventory.add(random_item, desired_row, desired_col)):
                        print("Item is placed successfully!")
                        start_point_valid = True
                    else:
                        print("Item is not placed successfully. Please try again!")
                else:
                    print("Input invalid. Please try again!")

        elif (get_item_choice == 'n'):
            print("Please input the item manually!")
            item_name = input("Enter item name: ")
            width = int(input("Enter item width: "))
            height = int(input("Enter item height: "))
            item_acquired = Item(str(id_count), item_name, width, height)
            id_count += 1
            
            print("Item created successfully!")
            print("Item ID:", item_acquired.get_id())
            get_item_choice_valid = True

            # Item Placement
            user_inventory.printInventory()

            # Rotate Choice
            rotate_choice_valid = False
            while (not rotate_choice_valid):
                rotate_choice = input("Do you want to rotate the item (y/n): ")
                if (rotate_choice == "y"):
                    item_acquired.rotate_item()
                    print("Item rotated successfully!")
                    rotate_choice_valid = True
                elif (rotate_choice == "n"):
                    rotate_choice_valid = True
                else:
                    print("Input invalid. Please try again!")

            items.append(item_acquired) # Add to items
            start_point_valid = False
            while (not start_point_valid):
                print("Choose the starting point for the item placement!")
                desired_row = int(input("Row: "))
                desired_column = int(input("Column: "))
                if (isinstance(desired_row, int) and isinstance(desired_column, int)):
                    # Placement
                    if (user_inventory.add(item_acquired, desired_row, desired_column)):
                        print("Item is placed successfully!")
                        start_point_valid = True
                    else:
                        print("Item is not placed successfully. Please try again!")
                else:
                    print("Input invalid. Please try again!")
        else:
            print("Input invalid. Please try again!")

    # Ask the user if they want to add another item
    continue_choice_valid = False
    while (not continue_choice_valid):
        user_continue_choice = input("Do you want to add another item? (y/n): ")
        if user_continue_choice == "y":
            print("You can continue adding another item.")
            continue_choice_valid = True
        elif (user_continue_choice == "n"):
            continue_choice_valid = True
            user_continue_choice = False
        else:
            print("Input invalid. Please try again!")

inventory_choice_valid = False
while (not inventory_choice_valid):
    inventory_choice = input("Do you want to auto-sort the inventory (y/n): ")
    if (inventory_choice == "y"):
        print("Inventory before sorting:")
        user_inventory.printInventory()

        print("Sorted Inventory using the FFD algorithm: ")
        user_inventory.clear()
        user_inventory.ffd(items)
        print("Test FFD")
        user_inventory.printInventory()

        print("Sorted Inventory using the BFD algorithm: ")
        user_inventory.clear()
        user_inventory.bfd(items)
        print("Test BFD")
        user_inventory.printInventory()
        inventory_choice_valid = True

    elif (inventory_choice == "n"):
        print("Inventory: ")
        user_inventory.printInventory()
        inventory_choice_valid = True
    else:
        print("Input invalid. Please try again!")

print("Thank you for trying my RE Inventory Simulator :)")