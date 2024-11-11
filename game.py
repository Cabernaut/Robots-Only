import random

# Define the character class for the player's hero
class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.health = 100
        self.mp = 50
        self.attack = 10
        self.defense = 5
        self.magic = 5
        self.gold = 0
        self.potions = 0
        self.level = 1
        self.xp = 0

        # Apply class-specific attributes
        if char_class == "Warrior":
            self.attack += 5
            self.defense += 3
        elif char_class == "Mage":
            self.magic += 5
            self.mp += 10
        elif char_class == "Rogue":
            self.attack += 3
            self.defense += 1
            self.agility = 5

    # Reduces health based on damage received
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Heals the character and ensures it does not exceed maximum health
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    # Checks if character is still alive
    def is_alive(self):
        return self.health > 0

    # Levels up the character, increasing stats
    def level_up(self):
        self.level += 1
        self.attack += 5
        self.defense += 2
        self.magic += 2
        self.max_health += 10
        self.health = self.max_health
        self.xp = 0

# Define enemy class for encounters
class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 50 + level * 10
        self.attack = 5 + level * 2
        self.defense = 2 + level * 1
        self.magic = 0

    # Reduces health based on damage received
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Checks if enemy is still alive
    def is_alive(self):
        return self.health > 0

# Function to choose character class
def choose_class():
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    choice = input("Enter the number of your choice: ")

    # Map choice to character class
    if choice == "1":
        return "Warrior"
    elif choice == "2":
        return "Mage"
    elif choice == "3":
        return "Rogue"
    else:
        print("Invalid choice. Please select again.")
        return choose_class()

# Function to create the player's character
def create_character():
    name = input("Enter your character's name: ")
    char_class = choose_class()
    character = Character(name, char_class)
    print(f"\nWelcome {character.name}, the {char_class}!")
    return character

# Display current character status
def print_status(character):
    print(f"\n{character.name} - Level {character.level} - Health: {character.health}/100 - MP: {character.mp}/50")
    print(f"Gold: {character.gold} - Potions: {character.potions}\n")

# Player attacks the enemy
def attack_enemy(character, enemy):
    damage = character.attack - enemy.defense
    if damage < 0:
        damage = 0
    enemy.take_damage(damage)
    print(f"{character.name} attacks {enemy.name} for {damage} damage!")

# Player uses magic on the enemy
def use_magic(character, enemy):
    if character.mp >= 10:
        damage = character.magic - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)
        character.mp -= 10
        print(f"{character.name} casts a spell on {enemy.name} for {damage} damage!")
    else:
        print(f"{character.name} doesn't have enough MP to cast a spell!")

# Enemy attacks the player
def enemy_turn(character, enemy):
    damage = enemy.attack - character.defense
    if damage < 0:
        damage = 0
    character.take_damage(damage)
    print(f"{enemy.name} attacks {character.name} for {damage} damage!")

# Handles the combat sequence
def battle(character):
    print("\nA wild enemy appears!")
    enemy = Enemy("Goblin", character.level)

    while character.is_alive() and enemy.is_alive():
        print_status(character)
        print(f"{enemy.name} - Health: {enemy.health}/{enemy.health}")
        print("What would you like to do?")
        print("1. Attack")
        print("2. Use Magic")
        print("3. Flee")

        choice = input("Enter the number of your choice: ")

        # Player choice logic
        if choice == "1":
            attack_enemy(character, enemy)
        elif choice == "2":
            use_magic(character, enemy)
        elif choice == "3":
            print(f"{character.name} tries to flee from the battle!")
            break
        else:
            print("Invalid choice. Please select again.")
            continue

        # Enemy's turn to attack
        if enemy.is_alive():
            enemy_turn(character, enemy)

        # Check if enemy is defeated
        if character.is_alive() and not enemy.is_alive():
            print(f"\n{enemy.name} has been defeated!")
            character.xp += 20
            character.gold += 10
            if character.xp >= 100:
                character.level_up()
                print(f"{character.name} has leveled up!")
            break

    # Check if player has been defeated
    if not character.is_alive():
        print(f"\n{character.name} has been defeated. Game Over.")

# Main game loop and options
def main():
    character = create_character()

    while character.is_alive():
        print_status(character)
        print("What would you like to do?")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Quit Game")

        choice = input("Enter the number of your choice: ")

        # Game options
        if choice == "1":
            battle(character)
        elif choice == "2":
            print("You have no items yet.")
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select again.")

# Run the game if this script is the main program
if __name__ == "__main__":
    main()

#CODE MADE ENTIRELY WITH CHAT GPT!
