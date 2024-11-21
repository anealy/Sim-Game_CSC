import random

class Monster:
    def __init__(self):
        self.hp = 10
        self.strength = 7
        
        self.defense = 5

class Hero:
    def __init__(self):
        self.hp = 54
        self.strength = 7
        
        self.defense = 20

class Room:
    def __init__(self):
        self.monster = Monster()
        self.hero = Hero()
        self.treasure = "gold coins"
    def battle(self):
        



        

