import random
import time
import math

# classes


class Player:
    def __init__(self, p_name, p_health, p_attack, p_armour, p_luck):
        self.name = p_name
        self.health = p_health
        self.attack = p_attack
        self.armour = p_armour
        self.luck = p_luck

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


class Minion:
    def __init__(self, m_name, m_health, m_attack, m_armour):
        self.name = m_name
        self.health = m_health
        self.attack = m_attack
        self.armour = m_armour


    def get_name(self):
        return self.name
        
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_armour(self):
        return self.armour

        
    def set_health(self, new_health):
        self.health = new_health
        
    def set_attack(self, new_attack):
        self.attack = new_attack
        
    def set_armour(self, new_armour):
        self.armour = new_armour







# functions

def choose_player():
    player_select_display = ("do you wish to play as\n (1) The Lord?\n ",
                             "(2) The + Adventurer?\n (3) The Vagabond?\n")
    player_select = input(player_select_display)
    while player_select != "1" and player_select != "2" and player_select != "3":
        print("unrecognised input. Please try again and select from the options given")
        player_select = input("do you wish to play as\n (1) The Lord?\n (2) The Adventurer?\n (3) The Vagabond?\n")

    if player_select == "1":
        playerName = "Lord"
        playerHealth = 110
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
        playerHealth = 90
        playerAttack = 50
        playerArmour = 40
        playerLuck = 5
        print(f"You have chosen the {playerName}")
    enter_castle()

    return (playerName, playerAttack, playerArmour, playerLuck)


def generate_minion():
    minion_name_list = [
        "Goblin",
        "Skeleton",
        "Kobold",]
    name = random.choice(minion_name_list)
    health = random.randint(20, 40)
    attack = random.randint(20, 40)
    armour = random.randint(10, 20)

    print(name)
    print(health)
    print(attack)
    print(armour)

    return minion(name, health, attack, armour)


def minion_attack(hitChance, attackValue, name, defence):
    print(name, "swings at you...")
    hit = random.randint(0,10)
    if hitChance >= hit:
        print("and strikes!")
        loss = attackValue - defence
        print(f"You stagger losing {loss} health")
        return math.ceil(loss)
    else:
        print("They miss!")
        return 0


def hitChance(luck):
    hit = random.randint(0,4)
    if luck < hit:
        print("MISS!")
        return False
    else:
        print("You hit!")
        return True


def isDead(health):
    if health < 1:
        return True
    else:
        return False


def gameOver(enemyDead):
    if enemyDead == True:
        print("you slew the foul minion")
    else:
        print("You have been slain!")
        exit()


def battle(genEnemy, genCharacter):
    print("You fight the", genEnemy.get_name(), "are you ready?")
    print("The stats are")
    print(vars(genEnemy))
    print("You attack the enemy")

    battle = True

    while battle == True:
        print("(1) attack\n (2) attack\n (3) attack\n")
        choice = input()

        while choice != "1" and choice != "2" and choice != "3":
            print("input wrong. Try again")
            print("(1) attack\n (2) attack\n (3) attack\n")
            choice = input()
    
        if choice == "1":
            damage = genCharacter.get_attack()
        elif choice == "2":
            damage = genCharacter.get_attack()
        elif choice == "3":
            damage = genCharacter.get_attack()
    
        print("swing!")
        hit = hitChance(genCharacter.get_luck())

        if hit:
            genEnemy.set_health(genEnemy.get_health() - damage)
            print("You hit!")
            print("Their health is now", genEnemy.get_health())
    
        else:
            print("You missed")
    
        enemyDead = isDead(genEnemy.get_health())

        if not enemyDead:
            genCharacter.set_health(genCharacter.get_health() - minion_attack(genEnemy.get_attack(), genEnemy.get_name(), genCharacter.get_armour()))

            characterDead = isDead(genCharacter.get_health())
        
            if characterDead == True:
                battle = False
                return False
        
            else:
                print("Your health is", genCharacter.get_health())
    
        else:
            battle = False
            print("You defeated it")

            return True
    

    

















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
    



def minion_room(generate_minion):
    print(f"as you enter the room, you see before you a {name}!")
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

"""

def fight(chosen_minion):
    print(f"you swing your weapon at the {chosen.minion.name}")



# def death():


def generate_minion():
    minion_list = [
    goblin = minion("Goblin", 25, 25, 25),
    skeleton = minion("Skeleton", 50, 50, 50),
    kobold = minion("Kobold", 75, 75, 75),
    ]
    random_minion = random.choice(minion_list)
    print(vars(random_minion))


 

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

"""

genCharacter = player("Test", 100, 20, 20, 6)

whoDied = battle(generate_minion(), genCharacter)
gameOver(WhoDied)

whoDied = battle(generate_minion(), genCharacter)
gameOver(WhoDied)

whoDied = battle(generate_minion(), genCharacter)
gameOver(WhoDied)