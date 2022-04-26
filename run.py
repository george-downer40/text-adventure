import random
import time

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
    minion("Goblin", 25, 25, 25),
    minion("Skeleton", 50, 50, 50),
    minion("Kobold", 75, 75, 75),
]


# functions

def choose_player():

    player_select = input("do you wish to play as\n (1) The Lord?\n (2) The Adventurer?\n (3) The Vagabond?\n")
    while player_select != "1" and player_select != "2" and player_select != "3":
        print("unrecognised input. Please try again and select from the options given")
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
    enter_castle()

    return chosen_player


def enter_castle():
    time.sleep(1)
    print("You enter the castle and meet Treguard")
    time.sleep(1)
    print("he gives you your quest...")
    time.sleep(1)
    print("With that, you accept your quest and step through the shimmering portal...")
    time.sleep(1)
    main_hall()


def main_hall():
    print("You find yourself in a great hall with lots of flavour text.")
    time.sleep(1)
    print("There appears to be three exits from this place;\n a large door at the end of the hall,\n a door to your left,\n and a door to your right. ")
    time.sleep(1)
    player_select = input("Do you\n (1) go through the door in front of you?\n (2) take the door to your left? \n (3) take the door to your right?\n")

    while player_select != "1" and player_select != "2" and player_select != "3":
        print("unrecognised input. Please try again and select from the options given")
        player_select = input("Do you \n (1) go through the door in front of you? \n (2) take the door to your left? \n (3) take the door to your right?\n")
    
    if player_select == "1":
        print("you chose 1")
    elif player_select == "2":
        print("you chose 2")
    elif player_select == "3":
        print("you chose 3")
    



def minion_room(chosen_player):
    random_minion = random.choice(minion_list)
    chosen_minion = random_minion
    print(f"as you enter the room, you see before you a {chosen_minion.name}!")
    time.sleep(1)
    print("How do you proceed?")
    time.sleep(1)
    player_select = input("Do you:\n (1) fight the creature?\n (2) try to sneak past it?\n")
    while player_select != "1" and player_select != "2":
        print("unrecognised input. Please try again and select from the options given")
        player_select = input("Do you:\n (1) fight the creature?\n (2) try to sneak past it?\n")
    
    if player_select == "1":
        print("you prepare yourself for battle!")
        fight(minion, chosen_player)
    elif player_select == "2":
        print("you attempt to sneak past the creature")
    
    # return minion



def fight(minion, chosen_player):
    print(f"you, the {chosen_player.name} swing your weapon at the {minion.name}")



# def death():






 

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



minion_room(chosen_player)