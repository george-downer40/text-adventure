import random
import time

#classes

class player:
    def __init__(self, Phealth, Pattack, Parmour, Pluck):
        self.health = Phealth
        self.attack = Pattack
        self.armour = Parmour
        self.luck = Pluck

class minion:
    def __init__(self, Mhealth, Mattack, Marmour):
        self.health = Mhealth
        self.attack = Mattack
        self.armour = Marmour


#functions

# def minion_room():


# def death():


def choose_player():
    player_select = ""

    player_select = input("do you wish to play as\n (1) The Lord?\n (2) The Adventurer?\n (3) The Vagabond?\n")
    if player_select == "1":
        print("You have chosen the Lord")
    elif player_select == "2":
        print("You have selected the Adventurer")
    elif player_select == "3":
        print("You have selected the Vagabond")
    else:
        print ("unrecognised input. Please select from the options given")
        choose_player()



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



choose_player()
choose_player()
choose_player()
choose_player()