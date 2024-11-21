import random

class Being:
    def __init__(self,Str_mod):
        self.hp =  10
        self.Str = 2
        self.STR_MOD = Str_mod #default 0


class Monster(Being): 
    def __init__(self,Hp, Str, Str_mod):
        super().__init__(self,Hp,Str,Str_mod)
        self.str = 
        
b = Being()
b.hp = 

class Hero:
    def __init__(self):
        
        self.hp = 54
        self.strength = 2



# def d20():
#     num = random.randrange(1,20)
#     return num

# def d8():
#     num = random.randrange(1,8)
#     return num

# def attack(Room()):
#     lroll = d20()
#     if(lroll > 10):
#         damage = d8()
#         print("")
#     if(lroll == 20):
#         damage = 2 * d8()
#     if(lroll <= 10):
#         print(f"")


# class Room:
#     def __init__(self):
#         self.monster = Monster()
#         self.hero = Hero()
#         self.treasure = "gold coins"
#         self.seen_rooms = "seen_rooms"
#     def battle(self):
#       hroll = d20()
#       vroll = d20()  
#       if(hroll > vroll):
#           self.hero.attack(self)






# def main():
