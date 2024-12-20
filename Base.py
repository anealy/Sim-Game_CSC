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
        self.inventory = {'Long Sword': 0, 'Short Sword': 0, 'Potion': 0}
        self.equipped_sword = None
        self.current_room = 'A1'
        self.is_fighting = False
        self.goblin_health = 0
        self.goblin_damage = 0

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
        self.inventory = {'Long Sword': 0, 'Short Sword': 0, 'Potion': 0}
        self.equipped_sword = None
        self.current_room = 'A1'

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

        # Check if there's a goblin in the room
        if random.random() < 0.3:  # 30% chance for a goblin to spawn in a room
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
        """Enter battle if a goblin spawns in the room."""
        self.is_fighting = True
        self.goblin_health = 100
        self.goblin_damage = random.randint(0, 15)
        self.goblins_attack()

    def goblins_attack(self):
        """Initiate combat between the character and the goblin."""
        if self.character_health <= 0:
            self.character_death()
            return

        # Display fight screen
        self.clear_window()
        tk.Label(self.root, text="You encountered a Goblin! Fight or Flee!", font=("Arial", 16)).pack(pady=20)

        # Show inventory items and action buttons
        tk.Button(self.root, text="Attack", command=self.attack).pack(pady=5)
        tk.Button(self.root, text="Use Potion", command=self.use_potion).pack(pady=5)
        tk.Button(self.root, text="Equip Long Sword", command=self.equip_long_sword).pack(pady=5)
        tk.Button(self.root, text="Equip Short Sword", command=self.equip_short_sword).pack(pady=5)
        tk.Button(self.root, text="Unequip Sword", command=self.unequip_sword).pack(pady=5)

        # Continue the fight if still alive
        if self.goblin_health <= 0:
            self.goblin_defeated()

    def attack(self):
        """Perform an attack with the equipped sword."""
        if self.equipped_sword is None:
            messagebox.showinfo("No weapon equipped", "You need to equip a sword first!")
            return

        # Calculate damage dealt
        if self.equipped_sword == "Long Sword":
            damage = random.randint(15, 20)
        else:
            damage = random.randint(10, 15)

        # Goblin takes damage
        self.goblin_health -= damage
        messagebox.showinfo("Attack", f"You attacked the Goblin for {damage} damage!")

        if self.goblin_health <= 0:
            self.goblin_defeated()
        else:
            self.character_turn()

    def character_turn(self):
        """The goblin counterattacks."""
        if self.character_health <= 0:
            self.character_death()
            return

        # Goblin attacks
        damage = random.randint(0, self.goblin_damage)
        self.character_health -= damage
        messagebox.showinfo("Goblin Attacks", f"The Goblin attacks you for {damage} damage!")

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
        self.inventory['Potion'] = 0
        messagebox.showinfo("Potion Used", f"You healed for {healing} health!")

        # Continue fight
        self.character_turn()

    def equip_long_sword(self):
        """Equip the Long Sword."""
        if self.inventory['Long Sword'] > 0:
            self.equipped_sword = "Long Sword"
            messagebox.showinfo("Sword Equipped", "You have equipped the Long Sword!")
        else:
            messagebox.showinfo("No Long Sword", "You don't have a Long Sword in your inventory!")

    def equip_short_sword(self):
        """Equip the Short Sword."""
        if self.inventory['Short Sword'] > 0:
            self.equipped_sword = "Short Sword"
            messagebox.showinfo("Sword Equipped", "You have equipped the Short Sword!")
        else:
            messagebox.showinfo("No Short Sword", "You don't have a Short Sword in your inventory!")

    def unequip_sword(self):
        """Unequip the current sword."""
        self.equipped_sword = None
        messagebox.showinfo("Sword Unequipped", "You have unequipped your sword!")

    def goblin_defeated(self):
        """Goblin defeated, show congratulations and return to room options."""
        messagebox.showinfo("Victory!", "Congratulations, you have defeated the Goblin!")
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

# Create Tkinter window
root = tk.Tk()
game = Game(root)
root.mainloop()