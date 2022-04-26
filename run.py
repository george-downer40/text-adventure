# import random
# import time

# classes

class player:
    def __init__(self, Pname, Phealth, Pattack, Parmour, Pluck):
        self.name = Pname
        self.health = Phealth
        self.attack = Pattack
        self.armour = Parmour
        self.luck = Pluck

player_list = [
    player("lord", 100, 50, 40, 5),
    player("Adventurer", 75, 40, 30, 7),
    player("Vagabond", 50, 20, 20, 12),
]


class minion:
    def __init__(self, Mname, Mhealth, Mattack, Marmour):
        self.name = Mname
        self.health = Mhealth
        self.attack = Mattack
        self.armour = Marmour


minion_list = [
    minion("Goblin", 25, 20, 10),
    minion("Skeleton", 25, 20, 10),
    minion("Kobold", 25, 20, 10),
]


# functions

# def minion_room():


# def death():


def choose_player(player):

    player_select = input("do you wish to play as\n (1) The Lord?\n (2) The Adventurer?\n (3) The Vagabond?\n")
    if player_select == "1":
        chosen_player = player_list[0]
        print(f"You have chosen the {chosen_player.name}")
    elif player_select == "2":
        chosen_player = player_list[1]
        print(f"You have chosen the {chosen_player.name}")
    elif player_select == "3":
        chosen_player = player_list[2]
        print(f"You have chosen the {chosen_player.name}")
    else:
        print ("unrecognised input. Please select from the options given")
        choose_player(player)



# def enter_castle():


# def main_hall():
 

# def trap_fail():


# def hallway_trap_room():


# def curiosity_trap_room():


# def treasure_room():


# def bomb_room():


# def riddle_room_1():


# def split_room():


# def trap_room_2():


# def riddle_room_2():


# def potions_room():


# def mighty_sword_room():


# def boss_fight():


# def win_game():


# def play_again():



choose_player(player)
choose_player(player)
choose_player(player)
choose_player(player)