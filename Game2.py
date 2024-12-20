



import random
import tkinter as tk
from tkinter import messagebox

# Character Class
class Character:
    def __init__(self, name, health, attack_points, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.inventory = inventory  # Inventory is a list of items (strings)
        self.equipped_item = None  # To track the currently equipped item
        self.potion_used = False  # To track if potion has been used

    def attack(self, monster):
        damage = random.randint(0, self.attack_points)  # Random damage between 0 and attack points
        monster.take_damage(damage)
        return damage
    
    def use_item(self, item):
        if item == "potion" and not self.potion_used:
            heal = random.randint(5, 10)  # Heal between 5 and 10
            self.health += heal
            self.potion_used = True
            return heal, "heals"

        elif item == "potion" and self.potion_used:
            return 0, "already used"

        elif item == "long sword":
            if self.equipped_item != "long sword":
                self.attack_points += random.randint(10, 20)  # Long Sword increases attack power
                self.equipped_item = "long sword"
                return self.attack_points, "equipped long sword"
            else:
                return 0, "already equipped"

        elif item == "short sword":
            if self.equipped_item != "short sword":
                self.attack_points += random.randint(5, 10)  # Short Sword increases attack power
                self.equipped_item = "short sword"
                return self.attack_points, "equipped short sword"
            else:
                return 0, "already equipped"
    
    def unequip_item(self):
        if self.equipped_item == "long sword":
            self.attack_points -= random.randint(10, 20)
            self.equipped_item = None
            return "unequipped long sword"
        elif self.equipped_item == "short sword":
            self.attack_points -= random.randint(5, 10)
            self.equipped_item = None
            return "unequipped short sword"
        else:
            return "no item equipped"

    def take_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0

# Monster Class
class Monster:
    def __init__(self, name, health, attack_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
    
    def attack(self, character):
        damage = random.randint(0, self.attack_points)  # Random damage between 0 and attack points
        character.take_damage(damage)
        return damage
    
    def take_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0

# GUI Application Class
class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battle Game")
        
        self.character = None
        self.monster = None
        self.rooms = ['Start Room', 'Goblin Room', 'Treasure Room', 'Dungeon']
        self.current_room = 0  # Starting room is the 'Start Room'
        
        self.health_bar_width = 200
        self.create_intro_screen()

    def create_intro_screen(self):
        """ Create the introductory screen """
        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.pack(padx=20, pady=20)

        intro_label = tk.Label(self.intro_frame, text="Welcome to the Battle Game!\nDefeat monsters and try to win!", font=("Arial", 16))
        intro_label.pack(pady=20)

        start_button = tk.Button(self.intro_frame, text="Start Game", command=self.create_name_screen)
        start_button.pack(pady=10)

    def create_name_screen(self):
        """ Create the screen to ask for the player's name """
        self.intro_frame.destroy()  # Remove the intro screen

        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(padx=20, pady=20)

        name_label = tk.Label(self.name_frame, text="Enter your character's name:", font=("Arial", 14))
        name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        submit_button = tk.Button(self.name_frame, text="Submit", command=self.start_game)
        submit_button.pack(pady=10)

    def start_game(self):
        """ Start the game after the player enters their name """
        character_name = self.name_entry.get() or "Hero"  # Default name if none is provided
        self.character = Character(character_name, 100, 20, inventory=["potion", "short sword", "long sword", "potion"])
        self.monster = Monster("Goblin", 80, 15)

        self.name_frame.destroy()  # Remove the name input screen
        self.create_room_screen()

    def create_room_screen(self):
        """ Create the room screen where the player can choose to fight, pass, or use items """
        room_name = self.rooms[self.current_room]
        self.room_frame = tk.Frame(self.root)
        self.room_frame.pack(padx=20, pady=20)

        room_label = tk.Label(self.room_frame, text=f"You are in the {room_name}", font=("Arial", 16))
        room_label.pack(pady=10)

        if self.current_room == 1:  # Goblin Room
            fight_button = tk.Button(self.room_frame, text="Fight Goblin", command=self.enter_battle)
            fight_button.pack(pady=10)
        
        pass_button = tk.Button(self.room_frame, text="Pass Turn", command=self.pass_turn)
        pass_button.pack(pady=10)

        items_button = tk.Button(self.room_frame, text="Items", command=self.open_items_menu)
        items_button.pack(pady=10)

    def open_items_menu(self):
        """ Open the items menu to allow the player to select an item """
        self.items_window = tk.Toplevel(self.root)
        self.items_window.title("Items Menu")

        tk.Button(self.items_window, text="Use Potion", command=self.use_potion).pack(pady=5)
        tk.Button(self.items_window, text="Equip Long Sword", command=self.equip_long_sword).pack(pady=5)
        tk.Button(self.items_window, text="Equip Short Sword", command=self.equip_short_sword).pack(pady=5)
        tk.Button(self.items_window, text="Unequip Current Item", command=self.unequip_item).pack(pady=5)

    def use_potion(self):
        if "potion" in self.character.inventory:
            heal, action = self.character.use_item("potion")
            if heal:
                messagebox.showinfo("Potion Used", f"You used a potion and {action}. Your health is now {self.character.health}.")
                self.character.inventory.remove("potion")
            else:
                messagebox.showinfo("Potion", "You've already used a potion in this fight.")
            self.items_window.destroy()
        else:
            messagebox.showwarning("Potion", "You don't have any potions left.")
    
    def equip_long_sword(self):
        if "long sword" in self.character.inventory:
            if self.character.equipped_item:
                self.character.unequip_item()  # Unequip any current item
            damage, action = self.character.use_item("long sword")
            messagebox.showinfo("Sword Equipped", f"You {action}. Your attack power is now {self.character.attack_points}.")
            self.items_window.destroy()
        else:
            messagebox.showwarning("No Long Sword", "You don't have a long sword in your inventory.")
    
    def equip_short_sword(self):
        if "short sword" in self.character.inventory:
            if self.character.equipped_item:
                self.character.unequip_item()  # Unequip any current item
            damage, action = self.character.use_item("short sword")
            messagebox.showinfo("Sword Equipped", f"You {action}. Your attack power is now {self.character.attack_points}.")
            self.items_window.destroy()
        else:
            messagebox.showwarning("No Short Sword", "You don't have a short sword in your inventory.")

    def unequip_item(self):
        if self.character.equipped_item:
            message = self.character.unequip_item()
            messagebox.showinfo("Item Unequipped", f"You {message}. Your attack power is now {self.character.attack_points}.")
        else:
            messagebox.showinfo("No Item Equipped", "You don't have any item equipped.")
        self.items_window.destroy()

    def enter_battle(self):
        """ Begin the fight with the monster """
        self.room_frame.destroy()  # Remove room screen
        self.battle_frame = tk.Frame(self.root)
        self.battle_frame.pack(padx=20, pady=20)

        self.update_health_bars()

        fight_button = tk.Button(self.battle_frame, text="Attack", command=self.fight)
        fight_button.pack(pady=10)

        pass_button = tk.Button(self.battle_frame, text="Pass Turn", command=self.pass_turn)
        pass_button.pack(pady=10)

    def update_health_bars(self):
        """ Update the health bars for both character and monster """
        # Update health for character and monster dynamically
        # Health bar logic here
        
        # For simplicity, only show health info for now:
        pass

    def fight(self):
        damage = self.character.attack(self.monster)
        messagebox.showinfo("Fight", f"You attacked the monster for {damage} damage!")
        self.update_health_bars()
        
        if self.monster.is_alive():
            monster_damage = self.monster.attack(self.character)
            messagebox.showinfo("Monster Attacks", f"The monster attacked you for {monster_damage} damage!")
            self.update_health_bars()

        if not self.character.is_alive():
            self.end_game()
        elif not self.monster.is_alive():
            messagebox.showinfo("Victory", "You defeated the goblin!")
            self.current_room += 1  # Move to the next room

    def pass_turn(self):
        pass  # Functionality to skip turn, can add further features

    def end_game(self):
        """ End the game and show a message box """
        messagebox.showinfo("Defeat", f"You were defeated by the {self.monster.name}.")
        self.game_over()

    def game_over(self):
        """ Show a Game Over screen with the option to retry or quit """
        retry = messagebox.askretrycancel("Game Over", "You died! Would you like to try again?")
        if retry:
            self.restart_game()
        else:
            self.root.quit()

    def restart_game(self):
        """ Restart the game after death """
        self.character.health = 100
        self.monster.health = 80
        self.start_game()

# Main Tkinter Application
def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

























    import random
import tkinter as tk
from tkinter import messagebox





#^ battle, -> change "self" and change "Cenemy"
    #^your turn
        #^choose attack, or run
    #^check if enemy is dead.
    #^enemy turn
        #^attack (or use ability under condition-possibly add a random function to ref here to randomize an unknown number of abilities within an enemy class.)
    #^check if dead or smthn






#b = Being() #test being
#b.hp = "j"
#"beep poop"


# def main():


#Movement
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
        




# root = tk.Tk()

# text = tk.Text(root)
# text.pack()

# old_stdout = sys.stdout    
# sys.stdout = Redirect(text)

# root.mainloop()

# sys.stdout = old_stdout





# Character Class
class Character:
    def __init__(self, name, health, attack_points, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.inventory = inventory  # Inventory is a list of items (strings)
        self.equipped_item = None  # To track the currently equipped item
        self.potion_used = False  # To track if potion has been used

    def attack(self, monster):
        damage = random.randint(0, self.attack_points)  # Random damage between 0 and attack points
        monster.take_damage(damage)
        return damage
    
    def use_item(self, item):
        if item == "potion" and not self.potion_used:
            heal = random.randint(5, 10)  # Heal between 5 and 10
            self.health += heal
            self.potion_used = True
            return heal, "heals"

        elif item == "potion" and self.potion_used:
            return 0, "already used"

        elif item == "long sword":
            if self.equipped_item != "long sword":
                self.attack_points += random.randint(10, 20)  # Long Sword increases attack power
                self.equipped_item = "long sword"
                return self.attack_points, "equipped long sword"
            else:
                return 0, "already equipped"

        elif item == "short sword":
            if self.equipped_item != "short sword":
                self.attack_points += random.randint(5, 10)  # Short Sword increases attack power
                self.equipped_item = "short sword"
                return self.attack_points, "equipped short sword"
            else:
                return 0, "already equipped"
    
    def unequip_item(self):
        if self.equipped_item == "long sword":
            self.attack_points -= random.randint(10, 20)
            self.equipped_item = None
            return "unequipped long sword"
        elif self.equipped_item == "short sword":
            self.attack_points -= random.randint(5, 10)
            self.equipped_item = None
            return "unequipped short sword"
        else:
            return "no item equipped"

    def take_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0

# Monster Class
class Monster:
    def __init__(self, name, health, attack_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
    
    def attack(self, character):
        damage = random.randint(0, self.attack_points)  # Random damage between 0 and attack points
        character.take_damage(damage)
        return damage
    
    def take_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0

# GUI Application Class
class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battle Game")
        
        self.character = None
        self.monster = None
        
        self.health_bar_width = 200
        self.create_intro_screen()

    def create_intro_screen(self):
        """ Create the introductory screen """
        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.pack(padx=20, pady=20)

        intro_label = tk.Label(self.intro_frame, text="Welcome to the Battle Game!\nDefeat monsters and level up!", font=("Arial", 16))
        intro_label.pack(pady=20)

        start_button = tk.Button(self.intro_frame, text="Start Game", command=self.create_name_screen)
        start_button.pack(pady=10)

    def create_name_screen(self):
        """ Create the screen to ask for the player's name """
        self.intro_frame.destroy()  # Remove the intro screen

        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(padx=20, pady=20)

        name_label = tk.Label(self.name_frame, text="Enter your character's name:", font=("Arial", 14))
        name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        submit_button = tk.Button(self.name_frame, text="Submit", command=self.start_game)
        submit_button.pack(pady=10)

    def start_game(self):
        """ Start the game after the player enters their name """
        character_name = self.name_entry.get() or "Hero"  # Default name if none is provided
        self.character = Character(character_name, 100, 20, inventory=["potion", "short sword", "long sword", "potion"])
        self.monster = Monster("Goblin", 80, 15)

        self.name_frame.destroy()  # Remove the name input screen
        self.create_battle_screen()

    def create_battle_screen(self):
        """ Create the battle screen """
        self.battle_frame = tk.Frame(self.root)
        self.battle_frame.pack(padx=20, pady=20)

        self.health_label = tk.Label(self.battle_frame, text="Character Health:")
        self.health_label.pack(pady=5)

        self.character_health_bar = tk.Canvas(self.battle_frame, width=self.health_bar_width, height=20, bg="red")
        self.character_health_bar.pack(pady=5)

        self.monster_health_label = tk.Label(self.battle_frame, text="Monster Health:")
        self.monster_health_label.pack(pady=5)

        self.monster_health_bar = tk.Canvas(self.battle_frame, width=self.health_bar_width, height=20, bg="green")
        self.monster_health_bar.pack(pady=5)

        self.fight_button = tk.Button(self.battle_frame, text="Fight", state=tk.NORMAL, command=self.fight)
        self.fight_button.pack(pady=5)

        self.pass_button = tk.Button(self.battle_frame, text="Pass", state=tk.NORMAL, command=self.pass_turn)
        self.pass_button.pack(pady=5)

        self.items_button = tk.Button(self.battle_frame, text="Items", state=tk.NORMAL, command=self.open_items_menu)
        self.items_button.pack(pady=5)

        self.update_health_bars()

    def update_health_bars(self):
        """ Update the health bars of both the character and the monster """
        # Update character health bar
        character_health_percentage = (self.character.health / 100) * 200
        self.character_health_bar.coords(self.character_health_bar.create_rectangle(0, 0, character_health_percentage, 20, fill="blue"))

        # Update monster health bar
        monster_health_percentage = (self.monster.health / 80) * 200
        self.monster_health_bar.coords(self.monster_health_bar.create_rectangle(0, 0, monster_health_percentage, 20, fill="black"))

    def open_items_menu(self):
        """ Open the items menu to allow the player to select an item """
        self.items_window = tk.Toplevel(self.root)
        self.items_window.title("Items Menu")

        tk.Button(self.items_window, text="Use Potion", command=self.use_potion).pack(pady=5)
        tk.Button(self.items_window, text="Equip Long Sword", command=self.equip_long_sword).pack(pady=5)
        tk.Button(self.items_window, text="Equip Short Sword", command=self.equip_short_sword).pack(pady=5)
        tk.Button(self.items_window, text="Unequip Current Item", command=self.unequip_item).pack(pady=5)

    def use_potion(self):
        if "potion" in self.character.inventory:
            heal, action = self.character.use_item("potion")
            self.update_health_bars()
            if heal:
                messagebox.showinfo("Potion Used", f"You used a potion and {action}. Your health is now {self.character.health}.")
                self.character.inventory.remove("potion")
            else:
                messagebox.showinfo("Potion", "You've already used a potion in this fight.")
            self.items_window.destroy()
        else:
            messagebox.showwarning("Potion", "You don't have any potions left.")
    
    def equip_long_sword(self):
        if "long sword" in self.character.inventory:
            if self.character.equipped_item:
                self.character.unequip_item()  # Unequip any current item
            damage, action = self.character.use_item("long sword")
            self.update_health_bars()
            messagebox.showinfo("Sword Equipped", f"You {action}. Your attack power is now {self.character.attack_points}.")
            self.items_window.destroy()
        else:
            messagebox.showwarning("No Long Sword", "You don't have a long sword in your inventory.")
    
    def equip_short_sword(self):
        if "short sword" in self.character.inventory:
            if self.character.equipped_item:
                self.character.unequip_item()  # Unequip any current item
            damage, action = self.character.use_item("short sword")
            self.update_health_bars()
            messagebox.showinfo("Sword Equipped", f"You {action}. Your attack power is now {self.character.attack_points}.")
            self.items_window.destroy()
        else:
            messagebox.showwarning("No Short Sword", "You don't have a short sword in your inventory.")

    def unequip_item(self):
        if self.character.equipped_item:
            message = self.character.unequip_item()
            self.update_health_bars()
            messagebox.showinfo("Item Unequipped", f"You {message}. Your attack power is now {self.character.attack_points}.")
        else:
            messagebox.showinfo("No Item Equipped", "You don't have any item equipped.")
        self.items_window.destroy()

    def fight(self):
        damage = self.character.attack(self.monster)
        self.update_health_bars()
        messagebox.showinfo("Fight", f"You attacked the monster for {damage} damage!")

        if self.monster.is_alive():
            monster_damage = self.monster.attack(self.character)
            self.update_health_bars()
            messagebox.showinfo("Monster Attacks", f"The monster attacked you for {monster_damage} damage!")
        
        if self.character.is_alive() and self.monster.is_alive():
            self.ask_use_item()
        else:
            self.end_game()

    def pass_turn(self):
        self.pass_button.config(state=tk.DISABLED)
        self.fight_button.config(state=tk.NORMAL)
        self.ask_use_item()

    def ask_use_item(self):
        """ Ask if the player wants to use an item """
        self.items_button.config(state=tk.NORMAL)
        
    def end_game(self):
        """ End the game and show a message box """
        if self.character.is_alive():
            messagebox.showinfo("Victory", f"Congratulations! You defeated the {self.monster.name}.")
        else:
            messagebox.showinfo("Defeat", f"You were defeated by {self.monster.name}. Game Over.")
        
        self.reset_game()

    def reset_game(self):
        """ Reset the game after it ends """
        self.start_button.config(state=tk.NORMAL)
        self.fight_button.config(state=tk.DISABLED)
        self.pass_button.config(state=tk.DISABLED)
        self.items_button.config(state=tk.DISABLED)

# Main Tkinter Application
def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()