Charecter1 = {
    "Name": "John",
    "Gender": "Male",
    "Birthday": "8/13",
    
    "Special": "Quick Movement",
    "Starting weapon": "Stick",
    "Starting potion": "N/A"
}

Charecter2 = {
    "Name": "Dylan",
    "Gender": "Male",
    "Birthday": "3/25",
    
    "Special": "Super Strength",
    "Starting weapon": "N/A",
    "Starting potion": "Incredi_Buff"
}

Charecter3 = {
    "Name": "Sarah",
    "Gender": "Female",
    "Birthday": "10/2",
    
    "Special": "Resiliant",
    "Starting weapon": "N/A",
    "Starting potion": "Health Buff"
}

Charecter4 = {
    "Name": "Haley",
    "Gender": "Female",
    "Birthday": "2/6",
    
    "Special": "Defensive",
    "Starting weapon": "Shield",
    "Starting potion": "N/A"
}

Sword_attack = 3 - 5
Shield_defense = 3 - 5
Potion_health = 10 - 30     




class Being:
    def __init__(self):
        self.hp = 10
        self.strength = 2
        self.STR_mod = 0


class Items:
    def __init__(self):
        
        
        
        Sword_attack = 3 - 5
        Shield_defense = 3 - 5
        Potion_health = 10 - 30     

        
        self.STR_mod = Sword_attack
        self.DEF_mod = Shield_defense
        self.HLTH_mod = Potion_health  



class Item:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __repr__(self):
        return f"{self.name}(Attack: {self.attack}, Defense: {self.defense})"


class Sword(Item):
    def __init__(self):
        super().__init__(name="Sword", attack=10, defense=5)


class Dagger(Item):
    def __init__(self):
        super().__init__(name="Dagger", attack=6, defense=2)


class LongSword(Item):
    def __init__(self):
        super().__init__(name="Long Sword", attack=15, defense=7)

sword = Sword()
dagger = Dagger()
long_sword = LongSword()


print(sword)
print(dagger)
print(long_sword)  




class Character:
    def __init__(self, name, gender, birthday, special, starting_weapon, starting_potion):
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.special = special
        self.starting_weapon = starting_weapon
        self.starting_potion = starting_potion
        self.inventory = []  
        
        
        if self.starting_weapon != "N/A":
            self.pick_up_weapon(self.starting_weapon)

    def __repr__(self):
        inventory_list = ", ".join(self.inventory) if self.inventory else "None"
        return (f"Character: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Birthday: {self.birthday}\n"
                f"Special Ability: {self.special}\n"
                f"Starting Weapon: {self.starting_weapon}\n"
                f"Starting Potion: {self.starting_potion}\n"
                f"Inventory: {inventory_list}")

    def pick_up_weapon(self, weapon_name):
        """Method to add a weapon to the character's inventory."""
        self.inventory.append(weapon_name)
        print(f"{self.name} has picked up the {weapon_name} and added it to their inventory!")

    def display_inventory(self):
        """Method to display the current inventory of the character."""
        if self.inventory:
            print(f"{self.name}'s Inventory: {', '.join(self.inventory)}")
        else:
            print(f"{self.name} has no items in their inventory.")



character1 = Character(
    name="John",
    gender="Male",
    birthday="8/13",
    special="Quick Movement",
    starting_weapon="Stick",
    starting_potion="N/A"
)

character2 = Character(
    name="Dylan",
    gender="Male",
    birthday="3/25",
    special="Super Strength",
    starting_weapon="N/A",
    starting_potion="Incredi_Buff"
)

character3 = Character(
    name="Sarah",
    gender="Female",
    birthday="10/2",
    special="Resilient",
    starting_weapon="N/A",
    starting_potion="Health Buff"
)

character4 = Character(
    name="Haley",
    gender="Female",
    birthday="2/6",
    special="Defensive",
    starting_weapon="Shield",
    starting_potion="N/A"
)


character1.pick_up_weapon("Sword")
character2.pick_up_weapon("Dagger")
character3.pick_up_weapon("Long Sword")
character4.pick_up_weapon("Axe")


print(character1)
character1.display_inventory()

print("\n" + "-"*50 + "\n")

print(character2)
character2.display_inventory()

print("\n" + "-"*50 + "\n")

print(character3)
character3.display_inventory()

print("\n" + "-"*50 + "\n")

print(character4)
character4.display_inventory()

#! Boss Design


class Boss:
    
    def __init__(self, name, creature, special, starting_weapon, starting_health, strength):
        self.name = name
        self.creature = creature
        self.special = special
        self.starting_weapon = starting_weapon
        self.starting_health = starting_health
        self.strength = strength


boss1 = Boss(
   name="Dark Shenobi",
   creature="Ninja", 
   special="Quickness",
   starting_weapon="Katana",
   starting_health="100",
   strength="10"

)

class Hero:
    def __init__(self):
        self.hp = 50
        self.strength = 10





class EndRoom:
    def __init__(self):
        self.monster = Boss()
        self.hero = Hero()
        self.end_rooms = "end_room"
    def battle(self):
      hroll = d20()
      vroll = d20()  
      if(hroll > vroll):
          self.hero.attack(self)


#! Possible Game

import random


class Character:
    def __init__(self, name, health, attack_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
    
    def attack(self, monster):
        damage = random.randint(0, self.attack_points)
        print(f"{self.name} attacks {monster.name} for {damage} damage.")
        monster.take_damage(damage)
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} HP left.")
        
    def is_alive(self):
        return self.health > 0


class Monster:
    def __init__(self, name, health, attack_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
    
    def attack(self, character):
        damage = random.randint(0, self.attack_points)  
        print(f"{self.name} attacks {character.name} for {damage} damage.")
        character.take_damage(damage)
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} HP left.")
        
    def is_alive(self):
        return self.health > 0


def battle(character, monster):
    while character.is_alive() and monster.is_alive():
       
        user_choice = input("\nDo you want to attack the monster? (yes/no): ").strip().lower()
        
        if user_choice == 'yes':
            character.attack(monster)
        
        
        if monster.is_alive():
            monster.attack(character)
        
        print(f"\n{character.name} HP: {character.health} | {monster.name} HP: {monster.health}\n")
        
    
    if character.is_alive():
        print(f"Victory! {character.name} has defeated {monster.name}.")
    else:
        print(f"{character.name} has been defeated by {monster.name}. Game Over.")


def main():
    
    character_name = input("Enter your character's name: ")
    character = Character(character_name, 100, 20)
    
    monster = Monster("Goblin", 80, 15)
    
    print(f"\nA wild {monster.name} appears! Your task is to defeat it!\n")
    
    # Start the battle
    battle(character, monster)

# Run the game
if __name__ == "__main__":
    main()










# KP_Up	80	65431	↑ on the keypad

# KP_Down	88	65433	↓ on the keypad

# KP_Left	83	65430	← on the keypad

# KP_Right	85	65432	→ on the keypad

# Double	Specifies two events happening close together in time. For example, <Double-Button-1> describes two presses of button 1 in rapid succession.

# 19	Map	A widget is being mapped, that is, made visible in the application. This will happen, for example, when you call the widget's .grid() method.

# Unmap	A widget is being unmapped and is no longer visible. This happens, for example, when you use the widget's .grid_remove() method.







roomlist = {
    "A1":{"Name":"A1","South": "B2"},
    "A2":{"Name":"A2", "South": "B3"},
    "B1":{"Name":"B1","East": "B2","South": "C1"},
    "B2":{"Name":"B2","East": "B3","West": "B1","South": "C2","North": "A1"},
    "B3":{"Name":"B3", "North": "A2","West": "B2","Search": "C2"},
    "C1":{"Name":"C1", "North": "B1", "South": "D1", "East":"C2"},
    "C2":{"Name":"C2", "North": "B2", "South": "D2", "West": "C1", "Search": "B3"},
    "D1":{"Name":"D1", "North": "C1", "South":"E2", "East": "D2"},
    "D2":{"Name":"D2", "North":"C2", "South": "E3", "West":"D1"},
    "E1":{"Name":"E1", "East": "E2"},
    "E2":{"Name": "E2", "North": "D1", "East": "E3", "South": "F1", "West": "E1"},
    "E3":{"Name": "E3", "North": "D2", "East": "E4", "West": "E2", "Search": "F1"},
    "E4":{"Name": "E4", "West": "E3"},
    "F1":{"Name": "F1", "North": "E2", "South": "G1", "Search": "E3"},
    "G1":{"Name": "G1", "North": "F1"}
}
directions = ("North", "South", "East", "West", "Search")
currentroom = roomlist["B3"]

def move():
    global currentroom
    print("\n\nYou can check North, South, East, West, or Search")
    print("Finished")
    print(currentroom["Name"])   #take out later. debug
    print("What direction would you like to move?: ")
    direction = input().title()
    if(direction in directions):
        if(direction in currentroom.keys()):
            print(f"You take the {direction} corridor")
            newroom = currentroom[direction]   #set where destination is
            for x in roomlist:   #check for location of destination
                print(newroom) #this is a debug print
                if x == newroom:    #loop through indiv room libraries
                    print("HI")  #debug print
                    currentroom = roomlist[x]
                    print(" " + currentroom["Name"])



            print(f"You are in room {currentroom["Name"]}")  #currentroom["Name"] is to ref name of current room
        
        else:
            print("You can't move that way")
            print(f"You are in room {currentroom['Name']}")
            
    else:
        print("You can't move that way")
        print(f"You are in room {currentroom['Name']}")

move()






roomlist = {
    "A1": {"Name": "A1", "South": "B2"},
    "A2": {"Name": "A2", "South": "B3"},
    "B1": {"Name": "B1", "East": "B2", "South": "C1"},
    "B2": {"Name": "B2", "East": "B3", "West": "B1", "South": "C2", "North": "A1"},
    "B3": {"Name": "B3", "North": "A2", "West": "B2", "Search": "C2"},
    "C1": {"Name": "C1", "North": "B1", "South": "D1", "East": "C2"},
    "C2": {"Name": "C2", "North": "B2", "South": "D2", "West": "C1", "Search": "B3"},
    "D1": {"Name": "D1", "North": "C1", "South": "E2", "East": "D2"},
    "D2": {"Name": "D2", "North": "C2", "South": "E3", "West": "D1"},
    "E1": {"Name": "E1", "East": "E2"},
    "E2": {"Name": "E2", "North": "D1", "East": "E3", "South": "F1", "West": "E1"},
    "E3": {"Name": "E3", "North": "D2", "East": "E4", "West": "E2", "Search": "F1"},
    "E4": {"Name": "E4", "West": "E3"},
    "F1": {"Name": "F1", "North": "E2", "South": "G1", "Search": "E3"},
    "G1": {"Name": "G1", "North": "F1"}
}

# Define valid directions for movement
directions = ("North", "South", "East", "West", "Search")

# Initialize the starting room
currentroom = roomlist["B3"]

def move():
    global currentroom

    # Present the available directions to the user
    print("\nYou can check North, South, East, West, or Search")
    print(f"You are currently in room {currentroom['Name']}")

    # Ask for user input on where to move
    print("What direction would you like to move? (North, South, East, West, Search): ")
    direction = input().title()

    # Check if the direction is valid
    if direction in directions:
        # Check if the direction exists for the current room
        if direction in currentroom:
            print(f"You take the {direction} corridor...")

            # Get the new room based on the direction
            newroom_name = currentroom[direction]

            # Update current room to the new room
            currentroom = roomlist.get(newroom_name)

            # Confirm the new room name
            print(f"You are now in room {currentroom['Name']}.")

        else:
            print(f"You can't move {direction} from here.")
            print(f"You are still in room {currentroom['Name']}.")
    else:
        print(f"{direction} is not a valid direction.")
        print(f"You are still in room {currentroom['Name']}.")

# Call the move function to initiate the movement logic
move()