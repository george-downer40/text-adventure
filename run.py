import time
import random

PLAYER_DATA = {
    "vitality": 20,
    "luck": 10
}


def vitality(vitality_level: int):
    """
    function allows player's vitality to be altered during the game
    1 paramater fed into the function: vitality_level: int
    this is used in the function itself
    """
    PLAYER_DATA["vitality"] = PLAYER_DATA["vitality"] + (vitality_level)


def luck(luck_level: int):
    """
    function allows player's luck to be altered during the game
    1 paramater fed into the function: luck_level: int
    this is used in the function itself
    """
    PLAYER_DATA["luck"] = PLAYER_DATA["luck"] + (luck_level)


def check_vitality():
    if PLAYER_DATA["vitality"] >= 4 and PLAYER_DATA["vitality"] < 10:
        print("You hear Treguards voice")
        time.sleep(1)
        print("'Careful adventurerer, your vitality is not great")
    elif PLAYER_DATA["vitality"] >= 1 and PLAYER_DATA["vitality"] < 4:
        print("Vitality critical! Be careful!")
    elif PLAYER_DATA["vitality"] < 1:
        game_over()


def game_over():
    """
    runs when player loses all vitality
    prints a game over message then calls
    replay_game() function
    """
    print("Ooh, nasty...")
    time.sleep(1)
    print("You have lost all your vitality")
    time.sleep(1)
    print("please try again")
    replay_game()


def enter_castle():
    """
    first function run in main() function
    starts the game
    """
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
    """
    function is called after enter_castle()
    gives player 3 options. Depending on what they select
    either hall_fight_1(), curiosity_trap() or bomb_trap()
    functions are called
    """
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
    """
    function called if user selects (3) in main_hall() function.
    Depending on player selection, they will either lose
    vitality or continue without taking damage.
    Both selections lead to cavern_fight() function being
    called
    """
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
            print("Your vitality level has been reduced to ")
            print(PLAYER_DATA["vitality"])
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
    """
    function called if player selects (1) in main_hall()
    function. Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    hall_fight_2() is called at end of function.
    """
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
        print("but not before it hits you first")
        vitality(-3)
        print("Your vitality level has been reduced to ")
        print(PLAYER_DATA["vitality"])
        print("You make your way to the next room")
        hall_fight_2()
    else:
        print("you are unscathed")
        print("You make your way to the next room")
        hall_fight_2()


def curiosity_trap():
    """
    function provides player with 2 options. If player selects (1)
    vitality() function is called and vitality is reduced by -100
    which calls the check_vital() function and guarantees a game over.
    If player selects (2), the armoury_fight() function is called.
    """
    print("flavour text of room. Mention classical gold statues and pillars")
    time.sleep(1)
    print("An insciption is marked on the largest pillar.")
    time.sleep(1)
    print("It reads:")
    print("UTI INTERPRES LATINE")
    time.sleep(1)
    print("There are two doors to choose from:")
    time.sleep(1)
    print("An ornate door with gold filigree in front of you")
    print("and gold letters reading 'omne quod nitet non est aurum'")
    time.sleep(1)
    print("and a weathered stone door to your right")
    print("with a wooden sign reading 'tutum (icis)'")
    time.sleep(1)
    print("Which door do you choose?")
    time.sleep(1)
    print("(1) the ornate gold door?")
    print("(2) the weathered stone door?")
    p_select = input("select (1) or (2)")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        time.sleep(1)
        print("Which door do you choose?")
        print("(1) the ornate gold door?")
        print("(2) the weathered stone door?")
        p_select = input("select (1) or (2)\n")

    if p_select == "1":
        print("You try to push the ornate door open")
        time.sleep(1)
        print("It seems to be jammed")
        time.sleep(1)
        print("You push harder against the door, using both hands")
        time.sleep(1)
        print("You can feel it starting to budge")
        time.sleep(1)
        print("It finally swings open!")
        print("You're bathed in a warm golden light")
        time.sleep(1)
        print("You try to walk through the door but your legs wont move!")
        time.sleep(1)
        print("You look down to see your feet are now solid gold!")
        time.sleep(0.5)
        print("It spreads up your legs and your torso")
        time.sleep(0.5)
        print("Where once you felt warmth from the golden light")
        print("emanating from the doorway,")
        time.sleep(0.5)
        print("now you just feel an intense cold and a")
        print("creeping sense of horror")
        time.sleep(1)
        print("The gold spreads up your neck and over your face")
        time.sleep(1)
        print("There's nothing you can do...")
        vitality(-100)
        check_vitality()

    elif p_select == "2":
        print("You push the stone door open and walk through")
        armoury_fight()


def hall_fight_2():
    """
    Function operates in similar way to hall_fight_1
    Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    mighty_sword() is called at end of function.
    """
    print("flavour text of room. Are you back in the same room?")
    time.sleep(1)
    print("The goblin you slew has risen from the death")
    time.sleep(1)
    print("You have no choice but to fight it")
    time.sleep(1)
    print("You swing your sword at the undead goblin")
    chance = random.randint(8, 12)

    if int(chance) > PLAYER_DATA["luck"]:
        print("You strike down the foul undead beast")
        print("but not before it hits you first")
        vitality(-3)
        print("Your vitality level has been reduced to ")
        print(PLAYER_DATA["vitality"])
        print("You make your way to the next room")
        mighty_sword()
    else:
        print("you are unscathed")
        print("You make your way to the next room")
        mighty_sword()


def cavern_fight():
    """
    Function operates in similar way to hall_fight_1 
    Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    riddle_room() is called at end of function.
    """
    print("You step through into a large cavern")
    time.sleep(1)
    print("In front of you is a skeleton")
    time.sleep(1)
    print("You have no choice but to fight it")
    time.sleep(1)
    print("You swing your sword at the skeleton")
    chance = random.randint(8, 12)

    if int(chance) > PLAYER_DATA["luck"]:
        print("You strike down the skeleton")
        print("but not before it hits you first")
        vitality(-3)
        print("Your vitality level has been reduced to ")
        print(PLAYER_DATA["vitality"])
        print("You make your way to the next room")
        riddle_room()
    else:
        print("you are unscathed")
        print("You make your way to the next room")
        riddle_room()


def riddle_room():
    print("Flavour text for room")
    time.sleep(1)
    print("The wall at the end of the chamber begins to crack")
    time.sleep(1)
    print("The wall is now a giant carved face made from bricks")
    time.sleep(1)
    print("The face lets out a large yawn, shaking the very room")
    time.sleep(1)
    print("You steel yourself, ready to fight if need be")
    time.sleep(1)
    print("The face starts talking, a booming voice:")
    time.sleep(1)
    print("'Ahhh, it's been so very long since I've had company'")
    time.sleep(1)
    print("'Tell me, what brings you to castle Knightmare?")
    time.sleep(1)
    print("Do you:")
    print("(1) Tell the stone face of your quest?")
    print("(2) Stay silent?")
    time.sleep(1)
    print("select (1) or (2)")
    p_select = input("")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        time.sleep(1)
        print("Do you:")
        print("(1) Tell the stone face of your quest?")
        print("(2) Stay silent?")
        time.sleep(1)
        print("select (1) or (2)")
        p_select = input("")

    if p_select == "1":
        print("You tell the face your quest")
        time.sleep(1)
        print("whatever the quest is")


def mighty_sword():
    print("You find yourself in a circular room")
    time.sleep(1)
    print("before you lies your prize")
    time.sleep(1)
    print("You attempt to pull the sword fron the plinth")
    time.sleep(1)
    print("you feel the sword testing you,")
    print("are you worthy?")
    time.sleep(1)
    print("You feel your vitality draining from you")
    x = 0
    while x < 10:
        vitality(-1)
        check_vitality()
        print(PLAYER_DATA["vitality"])
        x = x + 1

    print("Finally, the sword pulls free from the plinth!")
    time.sleep(1)
    print("You won!")


def replay_game():
    print("Would you like to play again?")
    time.sleep(1)
    print("(1) Yes")
    print("(2) No")
    p_select = input("select (1) or (2)\n")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        time.sleep(1)
        print("Would you like to play again?")
        time.sleep(1)
        print("(1) Yes")
        print("(2) No")
        p_select = input("select (1) or (2)\n")

    if p_select == ("1"):
        print("Great, lets dive back into castle Knightmare")
        vitality(20)
        main()

    elif p_select == ("2"):
        print("You can always try another time adventurer")
        time.sleep(2)
        print("closing game")
        exit()


def main():
    enter_castle()


def armoury_fight():
    print("placeholder")

# def ceiling_trap():


mighty_sword()
