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
    print("With that, you accept your quest and")
    print("step through the shimmering portal...")
    time.sleep(1)
    main_hall()


def main_hall():
    print("You find yourself in a great hall with lots of flavour text.")
    time.sleep(1)
    print("There appears to be three exits from this place;")
    time.sleep(1)
    print("a large door at the end of the hall,")
    time.sleep(0.5)
    print("a door to your left,")
    time.sleep(0.5)
    print("and a door to your right.")
    time.sleep(1)
    print("Do you\n (1) go through the door in front of you?")
    print("(2) take the door to your left?")
    print("(3) take the door to your right?")
    p_select = input("select (1), (2) or (3)")

    while p_select != "1" and p_select != "2" and p_select != "3":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print("Do you\n (1) go through the door in front of you?")
        print("(2) take the door to your left?")
        print("(3) take the door to your right?")
        p_select = input("select (1), (2) or (3)")

    if p_select == "1":
        print("you chose 1")
        hall_fight_1()
    elif p_select == "2":
        print("you chose 2")
        curiosity_trap()
    elif p_select == "3":
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
    print("(1) Run for the door")
    print("(2) Take shelter using the table?")
    p_select = input("select (1) or (2)")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print("Do you...")
        print("(1) Run for the door")
        print("(2) Take shelter using the table?")
        p_select = input("select (1) or (2)")

    if p_select == "1":
        print("you sprint for the door")
        chance = random.randint(8, 12)
        if int(chance) > PLAYER_DATA["luck"]:
            print("You were caught in the blast")
            vitality(-3)
            print("Your vitality has been reduced to " + str(PLAYER_DATA["vitality"]))
            time.sleep(1)
            print("You hear Treguard's voice inside the helm")
            time.sleep(0.5)
            print("'Careful adventurer, death is a very real possibility'")
            time.sleep(1)
            print("Your body aches, you can't take too much damage")
            print("or you will surely perish")
            time.sleep(1)
            print("You make your way to the door at the end of the workshop")
            print("and through the door")
            cavern_fight()
        else:
            print("You managed to reach the door before it blew!")
            time.sleep(1)
            print("Luck must be with you today")
            time.sleep(1)
            print("You step through the door")
            cavern_fight()

    elif p_select == "2":
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
        print("The explosion rocks the workshop,")
        print("sending the crates and their contents everywhere")
        time.sleep(1)
        print("Thankfully, the table sheltered you from the blast.")
        time.sleep(1)
        print("Although dazed, you make your way to the door")
        print("at the end of the workshop and step through")
        cavern_fight()


def hall_fight_1():
    print("flavour text of room")
    time.sleep(1)
    print("Blocking your way is a menacing goblin")
    time.sleep(1)
    print("You have no choice but to fight it")
    time.sleep(1)
    print("You swing your sword at the goblin")
    chance = random.randint(8, 12)
    if int(chance) > PLAYER_DATA["luck"]:
        print("You strike down the foul beast")
        print("but not before it hit you first")
        vitality(-3)
        print("Your vitality has been reduced to " + str(PLAYER_DATA["vitality"]))
        print("You make your way to the next room")
        hall_fight_2()
    else:
        print("you are unscathed")
        print("You make your way to the next room")
        hall_fight_2()


def curiosity_trap():


def hall_fight_2():


def cavern_fight():


# def riddle_room():

# def armoury_fight():

# def ceiling_trap():


# def mighty_sword():


hall_fight_1()
hall_fight_1()
hall_fight_1()
hall_fight_1()
hall_fight_1()
