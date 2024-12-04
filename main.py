import random

class Being:
    def __init__(self):
        self.hp =  10
        self.attack_points = 2
        self.item_mod = 0 #default 0


class Monster(): 
    def __init__(self):
        self.hp =  15
        self.attack_points = 4
        self.item_mod = 0 


class Hero:
    def __init__(self):

        self.hp = 54
        self.strength = 2



def d20():
    num = random.randrange(1,20)
    return num

def d8():
    num = random.randrange(1,8)
    return num

def attack(Room):
    lroll = d20()
    if(lroll > 10):
        damage = d8()
        print("")
    if(lroll == 20):
        damage = 2 * d8()
    if(lroll <= 10):
        print(f"")

def GAME_OVER():
    print("GAME OVER\n YOU DIED")


#^ battle, -> change "self" and change "Cenemy"
    #^your turn
        #^choose attack, or run
    #^check if enemy is dead.
    #^enemy turn
        #^attack (or use ability under condition-possibly add a random function to ref here to randomize an unknown number of abilities within an enemy class.)
    #^check if dead or smthn
def battle (self, enemy):
    while True:
        while True:




class Room:
    def __init__(self):
        self.monster = "none"
        self.hero = False
        self.treasure = "coins"
        self.seen_rooms = "seen_rooms"
    def battle(self):
      hroll = d20()
      vroll = d20()  
      if(hroll > vroll):
          self.hero.attack(self)


b = Being() #test being
b.hp = "j"



# def main():
