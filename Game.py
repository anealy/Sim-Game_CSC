# Game Version 2.0



import random


Charecter1 = {"Name": "John"}

Charecter2 = {"Name": "Dylan"}

Charecter3 = {"Name": "Sarah"}

Charecter4 = {"Name": "Haley"}

# Character Class
class Character:
    def __init__(self, name, health, attack_points, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.inventory = inventory  # Inventory is a list of items (strings)
    
    def attack(self, monster):
        damage = random.randint(10, self.attack_points)  # Random damage between 10 and attack points
        print(f"{self.name} attacks {monster.name} for {damage} damage.")
        monster.take_damage(damage)
    
    def use_item(self, item):
        if item == "Potion":
            heal = random.randint(0, 10)  # Heal between 0 and 10
            self.health += heal
            print(f"{self.name} uses a potion and heals for {heal} HP. Total HP is now {self.health}.")
        elif item == "Short sword":
            bonus_damage = random.randint(5, 15)  # Bonus damage between 5 and 15
            self.attack_points += bonus_damage
            print(f"{self.name} equips a short sword, increasing attack power by {bonus_damage}. New attack power is {self.attack_points}.")
        elif item == "Long sword":
            bonus_damage = random.randint(10, 20)  # Bonus damage between 10 and 20
            self.attack_points += bonus_damage
            print(f"{self.name} equips a long sword, increasing attack power by {bonus_damage}. New attack power is {self.attack_points}.")
            
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} HP left.")
        
    def is_alive(self):
        return self.health > 0
    
    def display_inventory(self):
        if not self.inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s inventory: {self.inventory}")

# Monster Class
class Monster:
    def __init__(self, name, health, attack_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
    
    def attack(self, character):
        damage = random.randint(5, self.attack_points)  # Random damage between 5 and attack points
        print(f"{self.name} attacks {character.name} for {damage} damage.")
        character.take_damage(damage)
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} HP left.")
        
    def is_alive(self):
        return self.health > 0

# Game Logic
def battle(character, monster):
    while character.is_alive() and monster.is_alive():
        # Display inventory and ask if user wants to use an item
        character.display_inventory()
        user_choice = input("\nDo you want to use an item from your inventory? (yes/no): ").strip().lower()
        
        if user_choice == 'yes':
            item_choice = input("Which item would you like to use? (Potion/Long sword/Short sword): ").strip().lower()
            if item_choice in character.inventory:
                character.use_item(item_choice)
                character.inventory.remove(item_choice)  # Remove the used item from inventory
            else:
                print(f"You don't have a {item_choice} in your inventory.")
        
        # Prompt the user to attack the monster
        attack_choice = input("\nDo you want to attack the monster? (yes/no): ").strip().lower()
        
        if attack_choice == 'yes':
            character.attack(monster)
        
        # If the monster is still alive, it will attack back
        if monster.is_alive():
            monster.attack(character)
        
        print(f"\n{character.name} HP: {character.health} | {monster.name} HP: {monster.health}\n")
        
    # Check for victory or defeat
    if character.is_alive():
        print(f"Victory! {character.name} has defeated {monster.name}.")
    else:
        print(f"{character.name} has been defeated by {monster.name}. Game Over.")

# Main Function
def main():
    # Create the character and monster
    character_name = input(f"Choose your Character: {Charecter1}, {Charecter2}, {Charecter3}, {Charecter4}: ")
    character = Character(character_name, 100, 20, inventory=["Potion", "Short sword", "Long sword"])
    
    monster = Monster("Goblin", 80, 20)  # Monster starts with 80 HP and 20 attack points
    
    print(f"\nA wild {monster.name} appears! Your task is to defeat it!\n")
    
    # Start the battle
    battle(character, monster)

# Run the game
if __name__ == "__main__":
    main()