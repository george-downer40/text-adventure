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

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_armour(self):
        return self.armour

    def get_luck(self):
        return self.luck
        

    def set_name(self):
        self.name = new_name
        
    def set_health(self):
        self.health = new_health
        
    def set_attack(self):
        self.attack = new_attack
        
    def set_armour(self):
        self.armour = new_armour
        
    def set_luck(self):
        self.luck = new_luck



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


    def get_name(self):
        return self.name
        
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_armour(self):
        return self.armour

        
    def set_health(self):
        self.health = new_health
        
    def set_attack(self):
        self.attack = new_attack
        
    def set_armour(self):
        self.armour = new_armour




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
        playerName = "Lord"
        playerHealth = 100
        playerAttack = 50
        playerArmour = 40
        playerLuck = 5
        print(f"You have chosen the {playerName}")
    elif player_select == "2":
        playerName = "Adventurer"
        playerHealth = 100
        playerAttack = 50
        playerArmour = 40
        playerLuck = 5
        print(f"You have chosen the {playerName}")
    elif player_select == "3":
        playerName = "Vagabond"
        playerHealth = 100
        playerAttack = 50
        playerArmour = 40
        playerLuck = 5
        print(f"You have chosen the {playerName}")
    enter_castle()

    return (playerName, playerAttack, playerArmour, playerLuck)


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
        minion_room()
    elif player_select == "2":
        print("you chose 2")
    elif player_select == "3":
        print("you chose 3")
    



def minion_room():
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
        fight(chosen_minion)
    elif player_select == "2":
        print("you attempt to sneak past the creature")
    
    return chosen_minion



def fight(chosen_minion):
    print(f"you swing your weapon at the {chosen.minion.name}")



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



choose_player()