# Adventure Game with Player Class and Game State Tracking

# Player class to track game state
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False


# Welcomes the player and returns a Player object
def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return Player(name)


# Describes the starting area
def describe_area():
    print("""
You find yourself in a dark forest...
The trees tower above you, and the air is thick with mystery.
You see two paths ahead:
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Stay where you are.
    Type 'i' to view your inventory.
""")


# Adds an item to the player's inventory
def add_to_inventory(player, item):
    if item not in player.inventory:
        player.inventory.append(item)
        print(f"You picked up a {item}!")
    else:
        print(f"You already have the {item}.")


# --- Main Game ---
player = welcome_player()
describe_area()

while True:
    choice = input("What will you do (1, 2, 3, or i)? ").lower()

    if choice == "1":
        print(f"{player.name}, you step into the dark woods...")
        if not player.has_lantern:
            add_to_inventory(player, "lantern")
            player.has_lantern = True
        else:
            print("You've already taken the lantern from here.")
    elif choice == "2":
        print(f"{player.name}, you climb toward the mountain pass...")
        if not player.has_map:
            add_to_inventory(player, "map")
            player.has_map = True
        else:
            print("You've already picked up the map.")
    elif choice == "3":
        print("You decide to stay put. Nothing happens.")
    elif choice == "i":
        print(f"\n📦 Inventory: {player.inventory}\n")
    else:
        print("Invalid input. Try again.")
