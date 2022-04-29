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


def check_vitality():
    """
    Function is called whenever player loses vitality.
    It will show two warnings based on the players vitality
    and if vitality is reduced to 0 it will call game_over() function.
    """
    if PLAYER_DATA["vitality"] >= 4 and PLAYER_DATA["vitality"] < 10:
        print_text("You hear Treguards voice")
        print_text("'Careful adventurerer, your vitality level is low'")
    elif PLAYER_DATA["vitality"] >= 1 and PLAYER_DATA["vitality"] < 4:
        print_text("Vitality level critical! Be careful!")
    elif PLAYER_DATA["vitality"] < 1:
        game_over()


def game_over():
    """
    runs when player loses all vitality
    prints a game over message then calls
    replay_game() function
    """
    print_text("Ooh, nasty...")
    print_text("You have lost all your vitality")
    print_text("please try again")
    replay_game()


def enter_castle():
    """
    first function run in main() function
    starts the game.
    If player has chosen to play again after a run through,
    function will also update PLAYER_DATA back to it's original
    values from when the game was first run.
    """
    PLAYER_DATA.update({'vitality': 20, 'luck': 10})
    print_text("You enter the castle and meet Treguard")
    print_text("he gives you your quest...")
    print_text("With that, you accept your quest and")
    print_text("step through the shimmering portal...")
    print_text("Your vitality level is:")
    print(PLAYER_DATA["vitality"])
    main_hall()


def main_hall():
    """
    function is called after enter_castle()
    gives player 3 options. Depending on what they select
    either hall_fight_1(), curiosity_trap() or bomb_trap()
    functions are called.
    """
    print_text("You find yourself in a great hall with lots of flavour text.")
    print_text("There appears to be three exits from this place;")
    print_text("a large door at the end of the hall,")
    print_text("a door to your left,")
    print_text("and a door to your right.")
    print_text("Do you:")
    print_text("(1) go through the door in front of you?")
    print_text("(2) take the door to your left?")
    print_text("(3) take the door to your right?")
    p_select = input("select (1), (2) or (3)")

    while p_select != "1" and p_select != "2" and p_select != "3":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print_text("Do you:")
        print_text("(1) go through the door in front of you?")
        print_text("(2) take the door to your left?")
        print_text("(3) take the door to your right?")
        p_select = input("select (1), (2) or (3)")

    if p_select == "1":
        print_text("you chose 1")
        hall_fight_1()
    elif p_select == "2":
        print_text("you chose 2")
        curiosity_trap()
    elif p_select == "3":
        print_text("you chose 3")
        bomb_trap()


def bomb_trap():
    """
    function called if user selects (3) in main_hall() function.
    Depending on player selection, they will either lose
    vitality or continue without taking damage.
    Both selections lead to cavern_fight() function being
    called.
    """
    print_text("You find yourself in a what seems to be a workshop,")
    print_text("with beaten copper panels lining the wall.")
    print_text("There are crates of nuts and bolts strewn across the floor")
    print_text("and a large wooden table a few paces in front of you")
    print_text("It looks like there's a door on the other side of the workshop")
    print_text("A loud hissing noise emanates from the middle of the workshop...")
    print_text("It's a large bomb! Its fuse is slowly burning down.")
    print_text("You don't have much time to act.")
    print_text("Do you...")
    print_text("(1) Run for the door")
    print_text("(2) Take shelter using the table?")
    p_select = input("select (1) or (2)")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print_text("Do you...")
        print_text("(1) Run for the door")
        print_text("(2) Take shelter using the table?")
        p_select = input("select (1) or (2)")

    if p_select == "1":
        print_text("you sprint for the door")
        chance = random.randint(9, 12)
        if int(chance) > PLAYER_DATA["luck"]:
            print_text("You were caught in the blast")
            vitality(-5)
            check_vitality()
            print_text("Your vitality level has been reduced to")
            print(PLAYER_DATA["vitality"])
            print_text("You hear Treguard's voice inside the helm")
            print_text("'Careful adventurer, death is a very real possibility'")
            print_text("Your body aches, you can't take too much damage")
            print_text("or you will surely perish")
            print_text("You make your way to the door at the end of the workshop")
            print_text("and through the door")
            cavern_fight()
        else:
            print_text("You managed to reach the door before it blew!")
            print_text("Luck must be with you today")
            print_text("You step through the door")
            cavern_fight()

    elif p_select == "2":
        print_text("you throw the table onto its side and hope for the best")
        print_text("You hear the fuse hissing away. It'll blow any second")
        print_text(".")
        print_text("..")
        print_text("...")
        print_text("BOOM")
        print_text("The explosion rocks the workshop,")
        print_text("sending the crates and their contents everywhere")
        print_text("Thankfully, the table sheltered you from the blast.")
        print_text("Although dazed, you make your way to the door")
        print_text("at the end of the workshop and step through")
        cavern_fight()


def hall_fight_1():
    """
    function called if player selects (1) in main_hall()
    function. Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    hall_fight_2() is called at end of function.
    """
    print_text("flavour text of room")
    print_text("Blocking your way is a menacing goblin")
    print_text("You have no choice but to fight it")
    print_text("You swing your sword at the goblin")
    chance = random.randint(9, 12)

    if int(chance) > PLAYER_DATA["luck"]:
        print_text("You strike down the foul beast")
        print_text("but not before it hits you first")
        vitality(-5)
        check_vitality()
        print_text("Your vitality level has been reduced to")
        print(PLAYER_DATA["vitality"])
        print_text("You make your way to the next room")
        hall_fight_2()
    else:
        print_text("you are unscathed")
        print_text("You make your way to the next room")
        hall_fight_2()


def curiosity_trap():
    """
    function provides player with 2 options. If player selects (1)
    vitality() function is called and vitality is reduced by -100
    which calls the check_vital() function and guarantees a game over.
    If player selects (2), the armoury_fight() function is called.
    """
    print_text("flavour text of room. Mention classical gold statues and pillars")
    print_text("An insciption is marked on the largest pillar.")
    print_text("It reads:")
    print_text("UTI INTERPRES LATINE")
    print_text("There are two doors to choose from:")
    print_text("An ornate door with gold filigree in front of you")
    print_text("and gold letters reading 'omne quod nitet non est aurum'")
    print_text("and a weathered stone door to your right")
    print_text("with a wooden sign reading 'tutum (icis)'")
    print_text("Which door do you choose?")
    print_text("(1) the ornate gold door?")
    print_text("(2) the weathered stone door?")
    p_select = input("select (1) or (2)")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        time.sleep(1)
        print_text("Which door do you choose?")
        print_text("(1) the ornate gold door?")
        print_text("(2) the weathered stone door?")
        p_select = input("select (1) or (2)\n")

    if p_select == "1":
        print_text("You try to push the ornate door open")
        print_text("It seems to be jammed")
        print_text("You push harder against the door, using both hands")
        print_text("You can feel it starting to budge")
        print_text("It finally swings open!")
        print_text("You're bathed in a warm golden light")
        print_text("You try to walk through the door but your legs wont move!")
        print_text("You look down to see your feet are now solid gold!")
        print_text("It spreads up your legs and your torso")
        print_text("Where once you felt warmth from the golden light")
        print_text("emanating from the doorway,")
        print_text("now you just feel an intense cold and a")
        print_text("creeping sense of horror")
        print_text("The gold spreads up your neck and envelops you.")
        print_text("There's nothing you can do...")
        vitality(-100)
        check_vitality()

    elif p_select == "2":
        print_text("You push the stone door open and walk through")
        armoury_fight()


def hall_fight_2():
    """
    Function operates in similar way to hall_fight_1
    Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    mighty_sword() is called at end of function.
    """
    print_text("flavour text of room. Are you back in the same room?")
    print_text("The goblin you slew has risen from the death")
    print_text("You have no choice but to fight it")
    print_text("You swing your sword at the undead goblin")
    chance = random.randint(9, 12)

    if int(chance) > PLAYER_DATA["luck"]:
        print_text("You strike down the foul undead beast")
        print_text("but not before it hits you first")
        vitality(-5)
        print_text("Your vitality level has been reduced to ")
        print(PLAYER_DATA["vitality"])
        print_text("You make your way to the next room")
        riddle_room()
    else:
        print_text("you are unscathed")
        print_text("You make your way to the next room")
        riddle_room()


def cavern_fight():
    """
    Function operates in similar way to hall_fight_1
    Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    riddle_room() is called at end of function.
    """
    print_text("You step through into a large cavern")
    print_text("In front of you is a skeleton")
    print_text("You have no choice but to fight it")
    print_text("You swing your sword at the skeleton")
    chance = random.randint(9, 12)

    if int(chance) > PLAYER_DATA["luck"]:
        print_text("You strike down the skeleton")
        print_text("but not before it hits you first")
        vitality(-5)
        check_vitality()
        print_text("Your vitality level has been reduced to ")
        print(PLAYER_DATA["vitality"])
        print_text("You make your way to the next room")
        riddle_room()
    else:
        print_text("you are unscathed")
        print_text("You make your way to the next room")
        riddle_room()


def riddle_room():
    """
    Function provides player with 3 options.
    2 options reduces their vitality and 1 option increases it.
    If player selects (1) or (3), the vitality() function is called and
    reduces vitality by 10, followed by the check_vitality() function.
    if player selects (2), the vitality function is called
    and increases vitality by 5.
    mighty_sword() function is called at the end.
    """
    print_text("Flavour text for room")
    print_text("The wall at the end of the chamber begins to crack")
    print_text("The wall is now a giant carved face made from bricks")
    print_text("The face lets out a large yawn, shaking the very room")
    print_text("You steel yourself, ready to fight if need be")
    print_text("The face starts talking, a booming voice:")
    print_text("'Ahhh, it's been so very long since I've had company'")
    print_text("'Why don't we play a little game?")
    print_text("'If you can answer my riddle, then you can continue on your way'")
    print_text("'I may even grant you a boon, it's been so long'")
    print_text("'However, if you get it wrong, there will be consequences'")
    print_text("'Okay adventurer, riddle me this'")
    print_text("'I am not alive, but I grow'")
    print_text("'I don't have lungs, but I need air'")
    print_text("'I don't have a mouth, but water kills me'")
    print_text("'What am I?'")
    print_text("what is your answer?")
    print_text("(1) Earth")
    print_text("(2) Fire")
    print_text("(3) Spirit")
    print_text("select (1), (2) or (3)")
    p_select = input("")

    while p_select != "1" and p_select != "2" and p_select != "3":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print_text("what is your answer?")
        print_text("(1) Earth")
        print_text("(2) Fire")
        print_text("(3) Spirit")
        print_text("select (1), (2) or (3)")
        p_select = input("")

    if p_select == "1":
        print_text("You answer 'earth'")
        print_text("The stone face frowns")
        print_text("'Incorrect!")
        print_text("The stone face opens it's mouth wide and a billowing black cloud pours out")
        print_text("It fills the room and you start to choke")
        print_text("You feel your vitality draining from you")
        vitality(-10)
        check_vitality()

    elif p_select == "2":
        print_text("You answer 'fire'")
        print_text("The stone face smiles")
        print_text("'Correct!")
        print_text("The stone face opens it's mouth wide and a vibrant green cloud pours out")
        print_text("It fills the room and you envelops you")
        print_text("You feel stronger, boosting your vitality")
        vitality(10)
    
    elif p_select == "3":
        print_text("You answer 'spirit'")
        print_text("The stone face frowns")
        print_text("'Incorrect!")
        print_text("The stone face opens it's mouth wide and a billowing black cloud pours out")
        print_text("It fills the room and you start to choke")
        print_text("You feel your vitality draining from you")
        vitality(-10)
        check_vitality()

    print_text("The stone face chuckles")
    print_text("'Well, I've had my fun with you, you best be on your way'")
    print_text("The stone face closes its eyes")
    print_text("Its mouth opens even wider until it's large enough for you to pass through")
    print_text("You step through the mouth into darkness")
    mighty_sword()



def mighty_sword():
    """
    function runs a while loop that reduces the player's vitality and
    calls the check_vitality() function. If the player's vitality is not
    reduced below 1, then the player wins and the replay_game() function
    is called.
    """
    print_text("You find yourself in a circular room")
    print_text("before you lies your prize")
    print_text("You attempt to pull the sword fron the plinth")
    print_text("you feel the sword testing you,")
    print_text("are you worthy?")
    print_text("You feel your vitality draining from you")

    x = 0
    while x < 3:
        vitality(-4)
        check_vitality()
        print_text("Your vitality is:")
        print(PLAYER_DATA["vitality"])
        x = x + 1

    print_text("Finally, the sword pulls free from the plinth!")
    print_text("You won!")
    replay_game()


def replay_game():
    """
    function is called if the player wins the game or if the game_over()
    function is called. If the player selects (1), the game will call the main() function
    and restart. If the player selects (2), the script will stop running.
    """
    print_text("Would you like to play again?")
    print_text("(1) Yes")
    print_text("(2) No")
    p_select = input("select (1) or (2)\n")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print_text("Would you like to play again?")
        print_text("(1) Yes")
        print_text("(2) No")
        p_select = input("select (1) or (2)\n")

    if p_select == ("1"):
        print_text("Great, lets dive back into castle Knightmare")
        main()

    elif p_select == ("2"):
        print_text("You can always try another time adventurer")
        print_text("closing game")
        exit()


def main():
    """
    function that starts the game in the script.
    calls enter_castle() function to begin game.
    """
    enter_castle()


def armoury_fight():
    """
    Function operates in similar way to hall_fight_1().
    Player will encounter an enemy and the function uses
    the luck key from the PLAYER_DATA dictionary as well as a random
    integer to determine if they lose vitality.
    ceiling_trap() is called at end of function.
    """
    print_text("You step through into an armoury")
    print_text("In front of you is a ghostly knight")
    print_text("You have no choice but to fight it")
    print_text("You swing your sword at the knight")
    chance = random.randint(9, 12)

    if int(chance) > PLAYER_DATA["luck"]:
        print_text("You strike down the foul apparition")
        print_text("but not before it hits you first")
        vitality(-5)
        print_text("Your vitality level has been reduced to ")
        print(PLAYER_DATA["vitality"])
        print_text("You make your way to the next room")
        ceiling_trap()
    else:
        print_text("you are unscathed")
        print_text("You make your way to the next room")
        ceiling_trap()


def ceiling_trap():
    """
    Function called after armoury_fight().
    """
    print_text("You step through into long chamber,")
    print_text("the walls made of a dark, obsidian like glass.")
    print_text("There is only one way out, through a dark portal")
    print_text("at the end of the chamber.")
    print_text("scattered across the floor are what seem to be wooden poles")
    print_text("of varying length. Many of them look split and splintered.")
    print_text("As you start to make way to the portal,")
    print_text("You notice scratches carved into the walls, all running")
    print_text("vertically up to the ceiling.")
    print_text("You hear a clicking and whirring sound, as if some")
    print_text("machinery has started to operate.")
    print_text("Over the clicking and whirring, you hear a grinding sound.")
    print_text("You look up and are aghast to see the ceiling has started")
    print_text("to descend. With the speed the ceiling is descending")
    print_text("there is no way you'll reach the end of the chamber in time.")
    print_text("With panic starting to set in you try to assess your options.")
    print_text("Do you:")
    print_text("(1) Grab one of the wooden poles and")
    print_text("try to prop the ceiling up?")
    print_text("(2) Lay flat on the floor and hope for the best?")
    print_text("Select (1) or (2)")
    p_select = input("")

    while p_select != "1" and p_select != "2":
        print("unrecognised input")
        print("Please try again and select from the options given")
        print_text("Do you:")
        print_text("(1) Grab one of the wooden poles and")
        print_text("try to prop the ceiling up?")
        print_text("(2) Lay flat on the floor and hope for the best?")
        print_text("Select (1) or (2)")
        p_select = input("")
    
    if p_select == "1":
        print_text("You grab the nearest wooden pole and try to")
        print_text("wedge it between the ceiling and the floor.")
        print_text("As the ceiling presses down onto the pole")
        print_text("You can hear it creaking and start to splinter.")
        chance = random.randint(8, 12)
        if int(chance) > PLAYER_DATA["luck"]:
            print_text("The ceiling bears down on the pole")
            print_text("as the sound of the whirring machinery intensifies.")
            print_text("Cracks start to run through the pole")
            print_text("and pieces start to fly off it.")
            print_text("You feel a sense of doom taking over you.")
            print_text(".")
            print_text("..")
            print_text("...")
            print_text("The pole splits...")
            print_text("The ceiling, having been held up for a time")
            print_text("descends at an alarming rate")
            print_text("You don't even have time to think as the ceiling")
            print_text("presses into you and continues until it reaches")
            print_text("the floor...")
            vitality(-100)
            check_vitality()
        else:
            print_text("The ceiling bears down on the pole")
            print_text("as the sound of the whirring machinery intensifies.")
            print_text("Cracks start to run through the pole")
            print_text("and pieces start to fly off it.")
            print_text("You feel a sense of doom taking over you.")
            print_text(".")
            print_text("..")
            print_text("...")
            print_text("Suddenly, the sound of the machinery stops.")
            print_text("The wooden pole is still holding,")
            print_text("propped between the ceiling and the floor")
            print_text("The sound of machinery starts again,")
            print_text("But the ceiling is rising back up!")
            print_text("You take a second to calm down,")
            print_text("before making your way to the portal at the")
            print_text("end of the chamber as quickly as possible!")
            print_text("You don't know if the ceiling will start to")
            print_text("descend again!")
            print_text("You step through the portal into darkness.")
            mighty_sword()
    
    elif p_select == "2":
        print_text("You drop to the floor, trying to bring yourself")
        print_text("as low to the floor as possible.")
        print_text("You hear the sound of the machinery intensify")
        print_text("and you can't bring yourself to look up.")
        print_text("You know the ceiling is coming down.")
        print_text("Was this a stupid mistake?")
        print_text("You feel the ceiling now bearing down on you,")
        print_text("the pressure building as well as the pain.")
        vitality(-5)
        check_vitality()
        print_text("Your vitality is:")
        print(PLAYER_DATA["vitality"])
        print_text("By some miracle, the ceiling stops!")
        print_text("After a few seconds it starts to rise back up,")
        print_text("allowing you to stand up.")
        print_text("You feel rather bruised after that close encounter,")
        print_text("but you quickly make your way to portal at the end")
        print_text("of the chamber.")
        print_text("You step through the portal into darkness.")
        mighty_sword()





def print_text(text):
    """
    function combines time.sleep and print statements.
    Will delay by 1 second and then print the text.
    Function is used to refactor and clean up code.
    """
    time.sleep(1)
    print(text)
 


main()
