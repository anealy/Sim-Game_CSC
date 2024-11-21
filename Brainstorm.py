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

class Being:
    def __init__(self):
        self.hp = 10
        self.strength = 2
        self.STR_mod = 0


class Items:
    def __init__(self):
        Sword.attack = 0 - 5

        
        self.STR_mod = Sword.attack
        self.DEF_mod = Shield.defense
        self.HLTH_mod = Potion.effect
        