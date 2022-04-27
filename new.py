import time
import random

PLAYER_DATA = {
    "vitality": 20,
    "luck": 10
}

def vitality(vitality_level: int):
    PLAYER_DATA["vitality"] = PLAYER_DATA["vitality"] + (vitality_level)

def luck(luck_level: int):
    PLAYER_DATA["luck"] = PLAYER_DATA["luck"] + (luck_level)

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
        hall_fight_1()
    elif player_select == "2":
        print("you chose 2")
        curiosity_trap()
    elif player_select == "3":
        print("you chose 3")
        bomb_trap()

def bomb_trap():
    time.sleep(1)
    print("You find yourself in a what seems to be a workshop,")
    print("with beaten copper panels lining the wall.")
    time.sleep(1)
    print("There are crates of nuts and bolts strewn across the floor")
    print("and a large wooden table a few paces in front of you")
    time.sleep(1)
    print("It looks like there's a door on the other side of the workshop")
    time.sleep(1)
    print("A loud hissing noise emanates from the middle of the workshop...")
    time.sleep(1)
    print("It's a large bomb! It's fuse is slowly burning down.")
    time.sleep(1)
    print("You don't have much time to act.")
    time.sleep(1)
    print("Do you...")
    player_select = input("(1) Run for the door\n (2) Take shelter using the table?")

    while player_select != "1" and player_select != "2":
        print("unrecognised input. Please try again and select from the options given")
        player_select = input("(1) Run for the door\n (2) Take shelter using the table?")
    
    if player_select == "1":
        print("you sprint for the door")
        chance = random.randint(8, 12)
        if int(chance) > PLAYER_DATA["luck"]:
            print("You were caught in the blast")
            vitality(-3)
        else:
            print("You managed to reach the door before it blew")
        
    elif player_select == "2":
        print("you throw the table onto its side and hope for the best")
        time.sleep(1)
        print("You hear the fuse hissing away. It'll blow any second")
        time.sleep(1)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(1)
        print("BOOM")
        time.sleep(1)
        print("The explosion rocks the workshop, sending the crates and their contents everywhere")
        time.sleep(1)
        print("Thankfully, the table sheltered you from the blast.")
        time.sleep(1)
        print("Although dazed, you make your way to the door at the end of the room")

        

"""
def curiosity_trap():

def cavern_fight():

def riddle_room():

def armoury_fight():

def ceiling_trap():

def hall_fight_1():

def hall_fight_2():

def mighty_sword():
"""

bomb_trap()
bomb_trap()
bomb_trap()
bomb_trap()
bomb_trap()
