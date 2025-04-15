# Adventure Game
# Author: sangye lama
# Version: 2.0
# Description: A text-based adventure game with inventory, flags, and area unlocking

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

    def add_to_inventory(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"{self.name}, you picked up a {item}!")
        else:
            print(f"{self.name}, you already have the {item}.")

def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return Player(name)

def describe_area():
    print("""
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
""")

def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods...")
    if not player.has_lantern:
        player.add_to_inventory("lantern")
        player.has_lantern = True
    else:
        print("You wander the woods again, but find nothing new.")

def explore_mountain_pass(player):
    print(f"{player.name}, you climb the rocky mountain pass...")
    if not player.has_map:
        player.add_to_inventory("map")
        player.has_map = True
    else:
        print("The pass is steep, but there's nothing new here.")

def explore_cave(player):
    print(f"{player.name}, you approach a dark cave...")
    if player.has_lantern:
        print("With your lantern, you light the way inside.")
        player.add_to_inventory("treasure")
    else:
        print("It’s too dark to enter. You need a lantern.")
        player.health -= 10
        print("You stumble in the darkness and lose 10 health.")

def explore_hidden_valley(player):
    print(f"{player.name}, you search for the hidden valley...")
    if player.has_map:
        print("Using your map, you find a hidden trail to the valley.")
        player.add_to_inventory("rare herbs")
    else:
        print("You wander in circles. Without a map, you can’t find the valley.")
        player.health -= 10
        print("The long journey tires you. You lose 10 health.")

def stay_still(player):
    print(f"{player.name}, you stay where you are.")
    print("Time passes. You feel weaker...")
    player.health -= 10
    print("You lose 10 health.")

def check_inventory(player):
    print(f"\n{player.name}'s Inventory: {player.inventory}")
    print(f"Health: {player.health}\n")

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("\n🎉 Congratulations! You've found the treasure and rare herbs. You win!")
        return True
    return False

def check_lose(player):
    if player.health <= 0:
        print("\n💀 You have run out of health. Game over.")
        return True
    return False

def main():
    player = welcome_player()
    describe_area()

    while True:
        print("""
What will you do?
1. Take the left path into the dark woods
2. Take the right path toward the mountain pass
3. Explore a nearby cave
4. Search for a hidden valley
5. Stay where you are
i. Check inventory
q. Quit game
""")
        choice = input("Choose an action (1-5, i, q): ").lower()

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
        elif choice == "i":
            check_inventory(player)
        elif choice == "q":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

        print(f"Current Health: {player.health}")

        if check_win(player) or check_lose(player):
            break

if __name__ == "__main__":
    main()
