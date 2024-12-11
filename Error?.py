import tkinter as tk
from tkinter import messagebox
import random

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Dungeon Adventure Game")

        # Game state
        self.character_name = ""
        self.character_strength = 0
        self.character_health = 100
        self.inventory = {'Long Sword': 1, 'Bow and Arrow': 1, 'Potion': 3}  # Bow and Arrow replaces Short Sword
        self.equipped_weapon = None
        self.current_room = 'A1'
        self.is_fighting = False
        self.goblin_health = 0
        self.goblin_damage = 0
        self.monster_name = ""  # This will hold the randomized monster name
        self.bow_and_arrow_turns = 0  # Track consecutive turns when using Bow and Arrow

        self.grid = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                     'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                     'D1', 'D2', 'D3', 'D4', 'D5', 'D6',
                     'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
                     'F1', 'F2', 'F3', 'F4']

        self.create_start_screen()

    def create_start_screen(self):
        """Create the initial start screen where the player enters their name."""
        self.clear_window()

        tk.Label(self.root, text="Welcome to Dungeon Adventure!", font=("Arial", 20)).pack(pady=20)

        tk.Label(self.root, text="Enter your character's name:").pack(pady=5)
        self.character_name_entry = tk.Entry(self.root)
        self.character_name_entry.pack(pady=10)

        # Create Start Game Button and store it in self.start_button
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        """Start the game by setting up the character stats."""
        self.character_name = self.character_name_entry.get()
        if not self.character_name:
            messagebox.showerror("Error", "Please enter a character name.")
            return

        # Set random base strength
        self.character_strength = random.randint(5, 15)

        # Reset game state
        self.character_health = 100
        self.inventory = {'Long Sword': 1, 'Bow and Arrow': 1, 'Potion': 3}  # Start with 3 potions
        self.equipped_weapon = None
        self.current_room = 'A1'
        self.bow_and_arrow_turns = 0  # Reset Bow and Arrow turns

        self.show_room_options()

    def show_room_options(self):
        """Display the available rooms and direction buttons."""
        self.clear_window()

        tk.Label(self.root, text=f"{self.character_name}'s current room: {self.current_room}", font=("Arial", 16)).pack(pady=20)

        # Show available directions based on the current room
        directions = self.get_available_directions(self.current_room)

        for direction in directions:
            tk.Button(self.root, text=f"Go {direction}", command=lambda dir=direction: self.move(dir)).pack(pady=5)

        tk.Button(self.root, text="Quit", command=self.quit_game).pack(pady=20)

    def move(self, direction):
        """Move the player to a new room and handle potential encounters."""
        new_room = self.get_new_room(self.current_room, direction)
        self.current_room = new_room

        # Check if the player reached the end room (F4)
        if self.current_room == 'F4':
            self.end_game()

        # Check if there's a monster in the room
        elif random.random() < 0.25:  # 25% chance for a monster to spawn in a room
            self.enter_battle()
        else:
            self.show_room_options()

    def get_new_room(self, current_room, direction):
        """Calculate the new room based on the direction."""
        rows = ['A', 'B', 'C', 'D', 'E', 'F']
        columns = ['1', '2', '3', '4']

        row, col = current_room[0], current_room[1]
        row_idx, col_idx = rows.index(row), columns.index(col)

        if direction == "North" and row_idx > 0:
            new_row = rows[row_idx - 1]
            return f"{new_row}{col}"
        elif direction == "South" and row_idx < len(rows) - 1:
            new_row = rows[row_idx + 1]
            return f"{new_row}{col}"
        elif direction == "East" and col_idx < len(columns) - 1:
            new_col = columns[col_idx + 1]
            return f"{row}{new_col}"
        elif direction == "West" and col_idx > 0:
            new_col = columns[col_idx - 1]
            return f"{row}{new_col}"
        return current_room  # If out of bounds, return current room

    def enter_battle(self):
        """Enter battle if a monster spawns in the room."""
        self.is_fighting = True
        self.monster_name = random.choice(["Cave Spider", "Skeleton", "Zombie", "Goblin", "Troll", "Prof. Kuznicki"])
        self.goblin_health = 100
        self.goblin_damage = random.randint(0, 15)
        self.bow_and_arrow_turns = 0  # Reset consecutive attacks for Bow and Arrow
        self.goblins_attack()

    def goblins_attack(self):
        """Initiate combat between the character and the monster."""
        if self.character_health <= 0:
            self.character_death()
            return

        # Display fight screen
        self.clear_window()
        tk.Label(self.root, text=f"You encountered a {self.monster_name}!", font=("Arial", 16)).pack(pady=20)

        # Show inventory items and action buttons
        tk.Button(self.root, text="Attack", command=self.attack).pack(pady=5)
        tk.Button(self.root, text="Use Potion", command=self.use_potion).pack(pady=5)
        tk.Button(self.root, text="Equip Long Sword", command=self.equip_long_sword).pack(pady=5)
        tk.Button(self.root, text="Equip Bow and Arrow", command=self.equip_bow_and_arrow).pack(pady=5)
        tk.Button(self.root, text="Unequip Weapon", command=self.unequip_weapon).pack(pady=5)

        # Continue the fight if still alive
        if self.goblin_health <= 0:
            self.goblin_defeated()

    def attack(self):
        """Perform an attack with the equipped weapon."""
        if self.equipped_weapon is None:
            messagebox.showinfo("No weapon equipped", "You need to equip a weapon first!")
            return

        if self.equipped_weapon == "Bow and Arrow":
            if self.bow_and_arrow_turns < 2:
                # Calculate damage with Bow and Arrow
                damage = random.randint(5, 10)
                self.goblin_health -= damage
                messagebox.showinfo(f"{self.monster_name} Attack", f"You attacked the {self.monster_name} for {damage} damage!")

                self.bow_and_arrow_turns += 1  # Increment Bow and Arrow attack counter
            else:
                # After 2 attacks, switch to goblin's turn
                self.bow_and_arrow_turns = 0
                self.character_turn()
        else:
            # Calculate damage with Long Sword
            damage = random.randint(15, 20)
            self.goblin_health -= damage
            messagebox.showinfo(f"{self.monster_name} Attack", f"You attacked the {self.monster_name} for {damage} damage!")

            # Show updated health after the attack
            self.show_health_status()

            if self.goblin_health <= 0:
                self.goblin_defeated()
            else:
                self.character_turn()

    def character_turn(self):
        """The monster counterattacks."""
        if self.character_health <= 0:
            self.character_death()
            return

        # Monster attacks
        damage = random.randint(0, self.goblin_damage)
        self.character_health -= damage
        messagebox.showinfo(f"{self.monster_name} Attacks", f"The {self.monster_name} attacks you for {damage} damage!")

        # Show updated health after the monster's attack
        self.show_health_status()

        if self.character_health <= 0:
            self.character_death()
        else:
            self.goblins_attack()

    def use_potion(self):
        """Use a potion to heal the character."""
        if self.inventory['Potion'] == 0:
            messagebox.showinfo("No Potions", "You have no potions to use!")
            return

        # Heal the character
        healing = random.randint(10, 20)
        self.character_health += healing
        self.inventory['Potion'] -= 1  # Decrease the potion count
        messagebox.showinfo("Potion Used", f"You healed for {healing} health!\nPotions left: {self.inventory['Potion']}")

        # Show updated health after using potion
        self.show_health_status()

        # Continue fight
        self.character_turn()

    def equip_long_sword(self):
        """Equip the Long Sword."""
        if self.inventory['Long Sword'] > 0:
            self.equipped_weapon = "Long Sword"
            messagebox.showinfo("Weapon Equipped", "You have equipped the Long Sword!")
        else:
            messagebox.showinfo("No Long Sword", "You don't have a Long Sword in your inventory!")

    def equip_bow_and_arrow(self):
        """Equip the Bow and Arrow."""
        if self.inventory['Bow and Arrow'] > 0:
            self.equipped_weapon = "Bow and Arrow"
            messagebox.showinfo("Weapon Equipped", "You have equipped the Bow and Arrow!")
        else:
            messagebox.showinfo("No Bow and Arrow", "You don't have a Bow and Arrow in your inventory!")

    def unequip_weapon(self):
        """Unequip the current weapon."""
        self.equipped_weapon = None
        messagebox.showinfo("Weapon Unequipped", "You have unequipped your weapon!")

    def goblin_defeated(self):
        """Monster defeated, show congratulations and return to room options."""
        messagebox.showinfo("Victory!", f"Congratulations, you have defeated the {self.monster_name}!")
        self.show_room_options()

    def character_death(self):
        """Handle the character's death."""
        messagebox.showinfo("You Died", "Better luck next time!")
        self.character_health = 100  # Reset health
        self.current_room = 'A1'  # Reset to start room
        self.show_room_options()

    def quit_game(self):
        """Quit the game."""
        self.root.quit()

    def clear_window(self):
        """Clear the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def get_available_directions(self, room):
        """Return available movement directions based on current room."""
        directions = []
        rows = ['A', 'B', 'C', 'D', 'E', 'F']
        columns = ['1', '2', '3', '4']

        row, col = room[0], room[1]
        row_idx, col_idx = rows.index(row), columns.index(col)

        if row_idx > 0:
            directions.append("North")
        if row_idx < len(rows) - 1:
            directions.append("South")
        if col_idx < len(columns) - 1:
            directions.append("East")
        if col_idx > 0:
            directions.append("West")

        return directions

    def end_game(self):
        """Display a message when the player wins by reaching the end room (F4)."""
        messagebox.showinfo("Congratulations!", "You found the end room and won!!")
        self.create_start_screen()  # Go back to the start screen to play again

    def show_health_status(self):
        """Show the current health of both the character and the monster."""
        messagebox.showinfo("Current Health Status", 
                            f"Your health: {self.character_health}\n"
                            f"{self.monster_name}'s health: {self.goblin_health}")

# Create Tkinter window
root = tk.Tk()
game = Game(root)
root.mainloop()