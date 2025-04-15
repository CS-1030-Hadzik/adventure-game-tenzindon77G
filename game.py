# Adventure Game - Refactored with Functions and Inventory System

# Global inventory list
inventory = []

# Function to welcome the player and get their name
def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return name

# Function to describe the starting area
def describe_area():
    starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
    print(starting_area)

# Function to add items to the inventory
def add_to_inventory(item):
    if item not in inventory:
        inventory.append(item)
        print(f"You picked up a {item}!")
    else:
        print(f"You already have the {item}.")

# Start the game
player_name = welcome_player()
describe_area()

# Main game loop
while True:
    print("""
You see two paths ahead:
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Stay where you are.
    Type 'i' to view your inventory.
""")
    choice = input("What will you do (1, 2, 3, or i)? ").lower()

    if choice == "1":
        print(f"{player_name}, you step into the dark woods...")
        add_to_inventory("lantern")
    elif choice == "2":
        print(f"{player_name}, you climb toward the mountain pass...")
        add_to_inventory("map")
    elif choice == "3":
        print("You decide to stay put. Nothing happens.")
    elif choice == "i":
        print(f"\n📦 Inventory: {inventory}\n")
    else:
        print("Invalid input. Try again.")
