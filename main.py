import random

class Monster:
    def __init__(self):
        self.hp = 10
        self.strength = 7
        
        self.defense = 12

class Hero:
    def __init__(self):
        self.hp = 54
        self.strength = 7

        self.defense = 18

def d20():
    num = random.randrange(1,20)
    return num

def d8():
    num = random.randrange(1,8)
    return num

def attack(Room()):
    lroll = d20()
    if(lroll > 10):
        damage = d8()
        print("")
    if(lroll == 20):
        damage = 2 * d8()
    if(lroll <= 10):
        print(f"")


class Room:
    def __init__(self):
        self.monster = Monster()
        self.hero = Hero()
        self.treasure = "gold coins"
    def battle(self):
      hroll = d20()
      vroll = d20()  
      if(hroll > vroll):
          self.hero.attack(self)

def main():

        



        

