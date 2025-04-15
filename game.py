# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.has_map = False
        self.has_lantern = False
        self.has_treasure = False
        self.has_rare_herbs = False

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name}, you picked up a {item}!")
        self.show_inventory()

    def show_inventory(self):
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")


# Function to welcome the player
def welcome_player():
    print("Welcome to the Adventure Game!")
    player_name = input("What is your name, adventurer? ")
    player = Player(player_name)
    print(f"Welcome, {player.name}! Your journey begins now.")
    return player


# Function to describe the starting area
def describe_area():
    print("""
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
""")


# Function to show the main menu
def show_main_menu():
    print(f"""
    1. Explore the dark woods
    2. Explore the mountain pass
    3. Explore the cave
    4. Search for the hidden valley
    5. Stay where you are
    6. View inventory
    """)


# Function to handle player choices
def handle_choice(choice, player):
    if choice == "1":
        explore_dark_woods(player)
    elif choice == "2":
        explore_mountain_pass(player)
    elif choice == "3":
        explore_cave(player)
    elif choice == "4":
        explore_hidden_valley(player)
    elif choice == "5":
        stay_still(player)
    elif choice == "6":
        player.show_inventory()
    else:
        print("Invalid choice, please select a valid option.")


# Function for exploring the dark woods
def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods...")
    if not player.has_lantern:
        print("It's too dark to continue without a lantern.")
    else:
        player.add_to_inventory("lantern")
        player.has_lantern = True


# Function for exploring the mountain pass
def explore_mountain_pass(player):
    print(f"{player.name}, you head toward the mountain pass.")
    if not player.has_map:
        print("You can't find your way without a map.")
    else:
        player.add_to_inventory("map")
        player.has_map = True


# Function for exploring the cave
def explore_cave(player):
    if player.has_lantern:
        print(f"{player.name}, you venture into the cave...")
        player.add_to_inventory("treasure")
        player.has_treasure = True
    else:
        print("It's too dark to continue without a lantern.")


# Function for exploring the hidden valley
def explore_hidden_valley(player):
    if player.has_map:
        print(f"{player.name}, you search for the hidden valley...")
        player.add_to_inventory("rare herbs")
        player.has_rare_herbs = True
    else:
        print("You can't find the valley without a map.")


# Function for staying still (no progress)
def stay_still(player):
    print(f"{player.name}, you decide to stay where you are.")


# Main game loop
def main():
    player = welcome_player()
    describe_area()

    while True:
        show_main_menu()
        choice = input("Choose an action (1-6): ").strip()
        handle_choice(choice, player)


# Run the game
if __name__ == "__main__":
    main()
