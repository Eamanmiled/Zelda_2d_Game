import random
import time


# environment printing
# prints hub
def center(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif x < 5 and y == 0 or x > 5 and y == 0 or y < 5 and x == 0 or y > 5 and x == 0:
                print('*', end="")
            elif x < 5 and y == size - 1 or x > 5 and y == size - 1 or y < 5 and x == size - 1:
                print('*', end="")
            elif y > 5 and x == size - 1:
                print('*', end="")
            # the box
            # items in room
            elif x == 9 and y == 7:
                print("$", end="")
            elif x == 5 and y == 7:
                print("C", end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()
    print(" H   U   B ")
# prints hub


# prints left
def left(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif y == 0 or x == 0 or y == size - 1 or y < 5 and x == size - 1 or y > 5 and x == size - 1:
                print('*', end="")
            # the box
            # items in room
            elif x == 1 and y == 5:
                print("C", end="")
            elif x == 3 and y == 5:
                print("M", end="")
            elif y in [4, 6]:
                print('*', end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()
# prints left


# prints down
def down(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif x == 0 or x < 5 and y == 0 or x > 5 and y == 0 or y == size - 1 or x == size - 1:
                print('*', end="")
            # the box
            # items in room
            elif x == 9 and y == 4:
                print(" ", end="")
            elif x == 1 and y == 2 or x == 1 and y == 6:
                print(" ", end="")
            elif y == 2 or y == 4 or y == 6:
                print("*", end="")
            elif y == 9 and x == 4 or y == 8 and x == 4:
                print("|", end="")
            elif y == 9 and x == 6 or y == 8 and x == 6:
                print("|", end="")
            elif x == 5 and y == 9:
                print("C", end="")
            elif x == 5 and y == 8:
                print("M", end="")
            elif y == 8:
                print("%", end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()
# prints down


# prints down
def right(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif y == 0 or y < 5 and x == 0 or y > 5 and x == 0 or y == size - 1 or x == size - 1:
                print('*', end="")
            # the box
            # items in room
            elif x == 9 and y in [1, 9]:
                print("C", end="")
            elif x == 6 and y == 5:
                print("M", end="")
            elif y == 4 and x < 7:  # walls in room
                print("*", end="")
            elif y == 6 and x < 7:  # walls in room
                print("*", end="")
            elif x == 6:
                print("*", end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()
# prints down


# prints up
def up(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif y == 0:
                print('*', end="")
            elif x == 0:
                print('*', end="")
            elif x == size - 1:
                print('*', end="")
            elif x < 5 and y == size - 1:
                print('*', end="")
            elif x > 5 and y == size - 1:
                print('*', end="")
            # the box
            # items in room
            elif y == 1 and x in [1, 3, 5, 7, 9]:  # this shortens the code so fucking much
                print("C", end="")
            elif x == 5 and y == 4:
                print("B", end="")
            elif x == 5 and y == 3:
                print("D", end="")
            elif y == 4:
                print('*', end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()
# prints up
# environment printing


# I have created this class to clean up the code
class CodeCleanUp:

    def wall(self):
        print("that's a wall")
        time.sleep(2)

    def spyrodefend(self):
        spyro.health("Increase", 25)
        spyro.defence("Increase", 3)
        print("Your HP is now " + str(spyro.get_specfic("hp")))
        print("Your Defence is now " + str(spyro.get_specfic("defe")))
        time.sleep(1)

    def encounter_with_death(self):
        choice = input("You have died...\nPay the angel of death 25 coins to come back?(Y/N): ")
        if choice not in ["Y", "N"]:
            while choice != "Y" and choice != "N":
                input("please choose Y or N")
        if choice == "Y" and spyro.get_specfic("bank") < 25:
            print("The angel appears, but you reach for your pocket and see you are short changed\nThe angel shakes"
                  "his head, reaches out his hand to your shoulder and leads you to eternal damnation")
            print("THE END\nThank you for playing")
            time.sleep(9999)
        elif choice == "Y":
            print("The angel appears and you hand him 25 coins, he whispers in a chilling voice"
                  "\nT I L L   W E   M E E T   A G A I N")
            spyro.riches("Decrease", 25)
            spyro.health("Increase", 101)
        else:
            print("The dungeon has bested your spirit and you submit\nAtleast you tried")
            print("THE END\nThank you for playing")
            time.sleep(9999)

    def end(self):
        print("The End")
        print("Thanks for playing")
        time.sleep(9999)
# I have created this class to clean up the code


# minigame
class Minigame:
    choice = 0

    def jewel(self):

        self.choice = 1
        self.escape_cave()
    def chain(self):

        self.escape_cave()

    def escape_cave(self):
        if self.choice == 1:


        else:
            blah blah
# minigame


# the random chest
class Chests:
    state = 0
    coins = random.randint(25, 100)

    def chest(self):
        if self.state == 0:
            print("Searching for coins...")
            time.sleep(4)
            if self.coins == 69 or self.coins == 89 or self.coins == 53:
                print(
                    "You found loot worth " + str(
                        self.coins) + " coins!\nHead back to the shop to trade them in for some equipment")
                print("A spider jumps out at you! stinging you and causing " + str(self.coins / 2) + " damage\n:(")
                spyro.health("Decrease", self.coins / 2)
                time.sleep(3)
                self.state += 1
                return
            else:
                print(
                    "You found loot worth " + str(
                        self.coins) + " coins!\nHead back to the shop to trade them in for some equipment ")
                spyro.riches("Increase", self.coins)
                self.state += 1
                time.sleep(3)
        else:
            print("you longingly stare at the empty chest")
            time.sleep(3)
# the random chest


# this is for the shop
def shop(message_condition):
    shopitems = ["Health Elixir", "Better Sword", "Piece of Armour", ]
    if message_condition == 1:
        print("Welcome to the Shop\n", shopitems)
    else:
        print(shopitems)
    item = input("What would you like to inspect or type Leave to leave: ")

    if item == "Leave":
        if spyro.get_specfic("bank") < 10:
            print("You awkwardly leave the shop and break something on the way out")
            print("You don't have enough coin for the pot you broke so the shop keeper starts shouting at you "
                  "then beats you up\n -10 hp and defence")
            spyro.health("Decrease", 10)
            spyro.defence("Decrease", 10)
            time.sleep(3)
        else:
            print("You awkwardly leave the shop and smash something on the way out\n -10 coin")
            spyro.riches("Decrease", 10)
            time.sleep(3)

    elif item == "Health Elixir":
        print("The Health Elixir increases your hp by 10 but costs 50 coin")
        outcome = input("B to buy\nL to go back\nEnter option: ")

        if outcome != "L" or outcome != "B":
            while outcome != "L" and outcome != "B":
                outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome == "B":
            if spyro.get_specfic("bank") >= 50:
                spyro.health("Increase", 10)
                spyro.riches("Decrease", 50)
            else:
                print("You are too poor to afford this")
                outcome2 = input("L to go back: ")
                while outcome2 != "L" and outcome2 != "B":
                    outcome2 = input("L to go back: ")
                time.sleep(1)

                shop(message_condition=0)
        else:
            shop(message_condition=1)

    elif item == "Better Sword":
        print("You spot a shiny sword that is better than yours\nattack increased by 10 but costs 60 coin")
        outcome = input("B to buy\nL to go back\nEnter option: ")

        if outcome != "L" or outcome != "B":
            while outcome != "L" and outcome != "B":
                outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome == "B":
            if spyro.get_specfic("bank") >= 60:
                spyro.health("Increase", 10)
                spyro.riches("Decrease", 60)
            else:
                print("You are too poor to afford this")
                outcome2 = input("L to go back: ")
                while outcome2 != "L" and outcome2 != "B":
                    outcome2 = input("L to go back: ")
                time.sleep(1)
                shop(message_condition=0)
        else:
            shop(message_condition=1)

    elif item == "Piece of Armour":
        print("You spot a shiny piece of armour to add to yourself\ndefence increased by 10 but costs 40 coins")
        outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome != "L" or outcome != "B":
            while outcome != "L" and outcome != "B":
                outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome == "B":
            if spyro.get_specfic("bank") >= 40:
                spyro.health("Increase", 10)
                spyro.riches("Decrease", 40)
            else:
                print("You are too poor to afford this")
                outcome2 = input("L to go back: ")
                while outcome2 != "L" and outcome2 != "B":
                    outcome2 = input("L to go back: ")
                time.sleep(1)
                shop(message_condition=0)
        else:
            shop(message_condition=1)

    else:
        print("You murmur something and the shop attendant asks you to leave"
              "\nyou trip and fall, break your neck, arms and legs on the way out"
              "\n-1 hp")
        spyro.health("decrease", 1)
        time.sleep(2)


# this is for all fights and each function is named after the fight location/boss
def fight1():  # right fight
    while spyro.get_specfic("hp") > 0 and monster1.get_specfic("hp") > 0:
        print("----Combat initiated----")
        print("Your hp is " + str(spyro.get_specfic("hp")))
        print("The monsters health is " + str(monster1.get_specfic("hp")))
        print("Would you like to\nAttack(1)\nBoost-Defence by 3 + Regain 25 Health(2)")
        action = input("Decision(1,2): ")
        if action not in ["1", "2"]:
            while action != "1" and action != "2":
                action = input("Please choose either 1 or 2")
        if action == "1":
            spyrosattackstat = spyro.get_specfic("attack")
            theattack = random.randint(1, spyrosattackstat) - (monster1.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("you do " + str(theattack) + " damage!")
            time.sleep(2)
            monster1.health("Increase", theattack)
        elif action == "2":
            cleanup.spyrodefend()
        monsterchoice = random.randint(1, 2)
        if monsterchoice == 1:
            print("The Monster attacks")
            time.sleep(1)
            monsterattackstat = monster1.get_specfic("attack")
            theattack = random.randint(1, monsterattackstat) - (spyro.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("The Monster Does " + str(theattack) + " Damage!")
            time.sleep(1)
            spyro.health("Increase", theattack)
        elif monsterchoice == 2:
            monster1.health("Increase", 15)
            monster1.defence("Increase", 3)
            print("The monster defended and now his hp is " + str(monster1.get_specfic("hp")))
            print("The monsters defence is now " + str(monster1.get_specfic("defe")))
            time.sleep(1)
# this is for the shop


def fight2():  # left fight
    while spyro.get_specfic("hp") > 0 and monster2.get_specfic("hp") > 0:
        print("----Combat initiated----")
        print("Your hp is " + str(spyro.get_specfic("hp")))
        print("The monsters health is " + str(monster2.get_specfic("hp")))
        print("Would you like to\nAttack(1)\nBoost-Defence by 3 + Regain 25 Health(2)")
        action = input("Decision(1,2): ")
        if action not in ["1", "2"]:
            while action != "1" and action != "2":
                action = input("Please choose either 1 or 2")
        if action == "1":
            spyrosattackstat = spyro.get_specfic("attack")
            theattack = random.randint(1, spyrosattackstat) - (monster2.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("you do " + str(theattack) + " damage!")
            time.sleep(2)
            monster2.health("Increase", theattack)
        elif action == "2":
            cleanup.spyrodefend()
        monsterchoice = random.randint(1, 2)
        if monsterchoice == 1:
            print("The Monster Attacks")
            time.sleep(1)
            monsterattackstat = monster2.get_specfic("attack")
            theattack = random.randint(1, monsterattackstat) - (spyro.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("The Monster Does " + str(theattack) + " Damage!")
            time.sleep(1)
            spyro.health("Increase", theattack)
        elif monsterchoice == 2:
            monster2.health("Increase", 15)
            monster2.defence("Increase", 3)
            print("The monster defended and now his hp is " + str(monster2.get_specfic("hp")))
            print("The monsters defence is now " + str(monster2.get_specfic("defe")))
            time.sleep(1)


def fight3():  # down fight
    while spyro.get_specfic("hp") > 0 and monster3.get_specfic("hp") > 0:
        print("----Combat initiated----")
        print("Your hp is " + str(spyro.get_specfic("hp")))
        print("The monsters health is " + str(monster3.get_specfic("hp")))
        print("Would you like to\nAttack(1)\nBoost-Defence by 3 + Regain 25 Health(2)")
        action = input("Decision(1,2): ")
        if action not in ["1", "2"]:
            while action != "1" and action != "2":
                action = input("Please choose either 1 or 2")
        if action == "1":
            spyrosattackstat = spyro.get_specfic("attack")
            theattack = random.randint(1, spyrosattackstat) - (monster3.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("you do " + str(theattack) + " damage!")
            time.sleep(2)
            monster3.health("Increase", theattack)
        elif action == "2":
            cleanup.spyrodefend()
        monsterchoice = random.randint(1, 2)
        if monsterchoice == 1:
            print("The Monster Attacks")
            time.sleep(1)
            monsterattackstat = monster3.get_specfic("attack")
            theattack = random.randint(1, monsterattackstat) - (spyro.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("The Monster Does " + str(theattack) + " Damage!")
            time.sleep(1)
            spyro.health("Increase", theattack)
        elif monsterchoice == 2:
            monster3.health("Increase", 15)
            monster3.defence("Increase", 3)
            print("The monster defended and now his hp is " + str(monster3.get_specfic("hp")))
            print("The monsters defence is now " + str(monster3.get_specfic("defe")))
            time.sleep(1)


def bossbattle():
    print("This is it, give it your all!")
    while spyro.get_specfic("hp") > 0 and lord_phalp.get_specfic("hp") > 0:
        print("----Combat initiated----")
        print("Your hp is " + str(spyro.get_specfic("hp")))
        print("The monsters health is " + str(lord_phalp.get_specfic("hp")))
        print("Would you like to\nAttack(1)\nBoost-Defence by 3 + Regain 25 Health(2)")
        action = input("Decision(1,2): ")
        if action not in ["1", "2"]:
            while action != "1" and action != "2":
                action = input("Please choose either 1 or 2")
        if action == "1":
            spyrosattackstat = spyro.get_specfic("attack")
            theattack = random.randint(1, spyrosattackstat) - (lord_phalp.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("you do " + str(theattack) + " damage!")
            time.sleep(2)
            lord_phalp.health("Increase", theattack)
        elif action == "2":
            cleanup.spyrodefend()
        monsterchoice = random.randint(1, 2)
        if monsterchoice == 1:
            print("The Monster Attacks")
            time.sleep(1)
            monsterattackstat = lord_phalp.get_specfic("attack")
            theattack = random.randint(1, monsterattackstat) - (spyro.get_specfic("defe") / 2)
            if theattack > 0:
                theattack = theattack * -1
            print("The Monster Does " + str(theattack) + " Damage!")
            time.sleep(1)
            spyro.health("Increase", theattack)
        elif monsterchoice == 2:
            lord_phalp.health("Increase", 15)
            lord_phalp.defence("Increase", 3)
            print("The monster defended and now his hp is " + str(lord_phalp.get_specfic("hp")))
            print("The monsters defence is now " + str(lord_phalp.get_specfic("defe")))
            time.sleep(1)
# this is for all fights and each function is named after the fight location/boss


# this is for all entity's in game to get assigned stats
class Entity:
    hp = 100  # stats
    defe = 50
    att = 70
    bank = 0

    def attack(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.att = self.att + amount
        else:
            self.att = self.att - amount

    def defence(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.defe = self.defe + amount
        else:
            self.defe = self.defe - amount

    def health(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.hp = self.hp + amount
        else:
            self.hp = self.hp - amount

    def riches(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.bank = self.bank + amount
        else:
            self.bank = self.bank - amount

    def return_player_stats(self):
        print("your hp is " + str(self.hp))
        print("your defence is " + str(self.defe))
        print("your attack is " + str(self.att))
        print("you have " + str(self.bank) + " coins")

    def get_balance(self):  # Retrieves the entities account balance
        return self.bank

    def get_specfic(self, item):
        if item == "hp":
            return self.hp
        elif item == "defe":
            return self.defe
        elif item == "attack":
            return self.att
        elif item == "bank":
            return self.bank
# this is for all entity's in game to get assigned stats


# this is the function to move the sprite in boundary and stop him if it's a wall also change maps and interactions
def move_sprite(position, direction):
    x, y = position

    # this is for the center hub -> other worlds
    if direction == "a" and y == 5 and x == 1 and num == 1:  # left map
        maps = "2"
        return maps
    elif direction == "d" and y == 5 and x == 9 and num == 1:  # right map
        maps = "4"
        return maps
    elif direction == "s" and y == 9 and x == 5 and num == 1:  # down map
        maps = "3"
        return maps
    elif direction == "w" and y == 1 and x == 5 and num == 1:  # up map
        if monster1.get_specfic("hp") <= 0 and monster2.get_specfic("hp") <= 0 and monster3.get_specfic("hp") <= 0:
            print("CREEEEEEK\nYou unlock the bulky door and step through")
            time.sleep(3)
            maps = "5"
            return maps
        else:
            print("You don't have the keys to open this door yet\nGo get them monsters!!")
            time.sleep(2)
    # this is for the center map and connections to other worlds

    # this is for returning to hub-world
    elif direction == "d" and y == 5 and x == 9 and num == 2:  # left->hub map
        maps = "1"
        return maps
    elif direction == "w" and y == 1 and x == 5 and num == 3:  # down->hub map
        maps = "1"
        return maps
    elif direction == "a" and y == 5 and x == 1 and num == 4:  # right->hub map
        maps = "1"
        return maps
    # this is for returning to hub-world

    # this is for the shop
    elif direction == "d" and x == 8 and y == 7 and num == 1:
        input("press anything to enter the shop: ")
        shop(message_condition=1)
        x += 1
    elif direction == "w" and x == 9 and y == 8 and num == 1:
        input("press anything to enter the shop: ")
        shop(message_condition=1)
        y -= 1
    elif direction == "s" and x == 9 and y == 6 and num == 1:
        input("press anything to enter the shop: ")
        shop(message_condition=1)
        y += 1
    # this is for the shop

    # this is for monster fights
    elif direction == "d" and x == 5 and y == 5 and num == 4:
        fight1()  # -------right fight
        if spyro.get_specfic("hp") <= 0:
            cleanup.encounter_with_death()
        else:
            x += 1
            print("You stand atop your defeated enemy victorious and with their key now in your safekeeping")
            time.sleep(2)
    elif x == 4 and y == 5 and direction == "a" and num == 2:
        fight2()  # ------left fight
        if spyro.get_specfic("hp") <= 0:
            cleanup.encounter_with_death()
        else:
            x -= 1
            print("You stand atop your defeated enemy victorious and with their key now in your safekeeping")
            time.sleep(2)
    elif x == 5 and y == 7 and direction == "s" and num == 3:
        fight3()  # ------down fight
        if spyro.get_specfic("hp") <= 0:
            cleanup.encounter_with_death()
        else:
            y += 1
            print("You stand atop your defeated enemy victorious and with their key now in your safekeeping")
            time.sleep(2)
    elif x == 5 and y == 5 and direction == "w" and num == 5:
        bossbattle()
        if spyro.get_specfic("hp") <= 0:
            cleanup.encounter_with_death()
        else:
            y += 1
            print("Lord Phalp collapses in front of you dying, with his last breath he lets out\n'all I wanted was"
                  " to feel the love you have.")
            time.sleep(2)
            print("The Dungeon begins to collapse around you, you spot two things. Your Pup chained up and"
                  " bag of gold & jewels that will set you for life you only have time to save one, what do you do?")
            decision = input("Press 1 to save your dog\nPress 2 to get rich")
            if decision not in [1, 2]:
                print("You take too long to decide and the ceiling collapses on you")
                cleanup.end()
            elif decision == 1:
                sub.chain()
                cleanup.end()
            else:
                sub.jewel()
                cleanup.end()

    # this is for monster fight # -------------------------

    # this is for the chests
    elif direction == "d" and x == 4 and y == 7 and num == 1:
        hubchest.chest()
    elif direction == "a" and x == 6 and y == 7 and num == 1:
        hubchest.chest()
    elif direction == "s" and x == 5 and y == 6 and num == 1:
        hubchest.chest()
    elif direction == "w" and x == 5 and y == 8 and num == 1:
        hubchest.chest()
    elif direction == "a" and x == 2 and y == 5 and num == 2:
        leftchest.chest()
    elif direction == "s" and x == 5 and y == 8 and num == 3:
        downchest.chest()
    elif direction == "s" and x == 9 and y == 8 and num == 4 or direction == "d" and x == 8 and y == 9 and num == 4:
        rightchest1.chest()
    elif direction == "w" and x == 9 and y == 2 and num == 4 or direction == "d" and x == 8 and y == 1 and num == 4:
        rightchest2.chest()
    # this is for the chests

    # for wall interact aka you hit a wall dummy
    elif num == 4 and y == 5 and x in [1, 2, 3, 4, 5, 6] and direction in ["w", "s"]:
        cleanup.wall()
    elif num == 4 and y in [1, 2, 3, 4, 6, 7, 8, 9] and x == 7 and direction == "a":
        cleanup.wall()
    elif num == 2 and y == 5 and direction in ["w", "s"]:
        cleanup.wall()
    elif num == 5 and y == 5 and x in [1, 2, 3, 4, 6, 7, 8, 9] and direction == "w":
        cleanup.wall()
    elif num == 5 and y == 3 and x in [1, 2, 3, 4, 6, 7, 8, 9] and direction == "s":
        cleanup.wall()
    elif num == 5 and y == 4 and x == 5 and direction in ["a", "d"]:
        cleanup.wall()
    elif (num == 3 and y in [1, 5] and x in [2, 3, 4, 5, 6, 7, 8] and direction in ["s", "w"] or num == 3 and y == 5 and
          x == 9 and direction == "s"):
        cleanup.wall()
    elif num == 3 and y in [2, 6] and x in [1, 9] and direction == "d" or x == 9 and y == 4 and direction == "a":
        cleanup.wall()
    elif num == 3 and y == 7 and x in [1, 2, 3, 4, 6, 7, 8, 9] and direction == "s":
        cleanup.wall()
    elif num == 3 and y == 5 and x < 9 and direction == "w" or num == 3 and y == 5 and x > 1 and direction == "s":
        cleanup.wall()
    elif num == 3 and y == 7 and x > 1 and direction == "w":
        cleanup.wall()
    elif num == 3 and x == 5 and y in [8, 9] and direction in ["a", "d"]:
        cleanup.wall()
    elif num == 3 and y == 3 and x < 9 and direction == "s" or num == 3 and y == 3 and x > 1 and direction == "w":
        cleanup.wall()
    # for wall interact aka you hit a wall dummy

    # basic moving code
    elif direction == 'w' and y > 1:
        y -= 1
    elif direction == 's' and y < 9:
        y += 1
    elif direction == 'a' and x > 1:
        x -= 1
    elif direction == 'd' and x < 9:
        x += 1
    # basic moving code

    # "that's a wall" code
    elif direction == 'a' or "d" and x == 2:  # this is for left
        cleanup.wall()
    elif direction == 's' or "w" and y == 2 or 8:  # this one is for the bottom and top
        cleanup.wall()
    # "that's a wall" code

    return x, y
# this is the function to move the sprite in boundary and stop him if it's a wall also change maps and interactions


# ---------------------------------------------------------------------------------------------------------


# Where the game starts
sprite_position = (5, 5)
# difficulty selection
print("You are Spyro\nThe Evil Lord Phalp has kidnapped your dog and is holding him ransom\nGo on a murderous rampage "
      "in his Dungeon and save that pup\nThe Evil Lord Phalp locked the door to his vault but his three "
      "monster guards have the keys\nKill them to take the keys and get your dog back!")
time.sleep(3)
difficulty = input("Enter E to play on Easy or H to play on Hard: ")
if difficulty != "E" or "H":
    while difficulty != "E" and difficulty != "H":
        difficulty = input("Invalid selection\n Press either H or E then press enter: ")
# entity creation
spyro = Entity()
monster1 = Entity()
monster2 = Entity()
monster3 = Entity()
lord_phalp = Entity()
hubchest = Chests()
leftchest = Chests()
rightchest1 = Chests()
rightchest2 = Chests()
downchest = Chests()
cleanup = CodeCleanUp()
sub = Minigame()
# difficulty activated
if difficulty == "E":
    spyro.health("Increase", 30)
    spyro.attack("Increase", 300)  # for easy demo-----
    spyro.defence("Increase", 30)

    monster1.health("Decrease", 15)
    monster1.attack("Decrease", 15)
    monster1.defence("Decrease", 15)

    monster2.health("Decrease", 15)
    monster2.attack("Decrease", 15)
    monster2.defence("Decrease", 15)

    lord_phalp.health("Decrease", 15)
    lord_phalp.attack("Decrease", 15)
    lord_phalp.defence("Decrease", 15)
elif difficulty == "H":
    monster1.health("Increase", 15)
    monster1.attack("Decrease", 30)  # a brick
    monster1.defence("Increase", 15)

    monster2.health("Decrease", 30)
    monster2.attack("Increase", 20)  # speed demon
    monster2.defence("Increase", 15)

    monster2.health("Increase", 5)
    monster2.attack("Increase", 5)  # jack of all trades
    monster2.defence("Increase", 5)

    lord_phalp.health("Increase", 35)
    lord_phalp.attack("Increase", 35)  # B O S S
    lord_phalp.defence("Increase", 35)

# CORE GAME LOOP
num = 1  # start in world 1
while True:
    if num == 1:
        while True:
            center(sprite_position)
            move = input("check stats = stat\nMove sprite (w, a, s, d): ")  # Hub map
            if move in ['w', 'a', 's', 'd']:
                sprite_position = move_sprite(sprite_position, move)
                if sprite_position == "2" or sprite_position == "3" or sprite_position == "4" or sprite_position == "5":
                    num = int(sprite_position)
                    break
            elif move == "stat":
                spyro.return_player_stats()
                time.sleep(3)
            else:
                print("Invalid move. Enter w,a,s,d.")
                time.sleep(2)
    elif num == 2:  # switch to left map mode
        sprite_position = (9, 5)
        while True:
            left(sprite_position)
            move = input("check stats = 'stat'\nMove sprite (w, a, s, d): ")  # left map
            if move in ['w', 'a', 's', 'd']:
                sprite_position = move_sprite(sprite_position, move)
                if sprite_position == "1":
                    num = int(sprite_position)
                    sprite_position = (1, 5)
                    break
            elif move == "stat":
                spyro.return_player_stats()
                time.sleep(3)
            else:
                print("Invalid move. Enter w,a,s,d.")
                time.sleep(2)
    elif num == 3:  # switch to down map mode
        sprite_position = (5, 1)
        while True:
            down(sprite_position)
            move = input("check stats = 'stat'\nMove sprite (w, a, s, d): ")  # down map
            if move in ['w', 'a', 's', 'd']:
                sprite_position = move_sprite(sprite_position, move)
                if sprite_position == "1":
                    num = int(sprite_position)
                    sprite_position = (5, 9)
                    break
            elif move == "stat":
                spyro.return_player_stats()
                time.sleep(3)
            else:
                print("Invalid move. Enter w,a,s,d.")
                time.sleep(2)
    elif num == 4:  # switch to right map mode
        sprite_position = (1, 5)
        while True:
            right(sprite_position)
            move = input("check stats = 'stat'\nMove sprite (w, a, s, d): ")  # right map
            if move in ['w', 'a', 's', 'd']:
                sprite_position = move_sprite(sprite_position, move)
                if sprite_position == "1":
                    num = int(sprite_position)
                    sprite_position = (9, 5)
                    break
            elif move == "stat":
                spyro.return_player_stats()
                time.sleep(3)
            else:
                print("Invalid move. Enter w,a,s,d.")
                time.sleep(2)
    elif num == 5:  # switch to up map mode
        sprite_position = (5, 9)
        while True:
            up(sprite_position)
            move = input("check stats = 'stat'\nMove sprite (w, a, s, d): ")  # up map
            if move in ['w', 'a', 's', 'd']:
                sprite_position = move_sprite(sprite_position, move)
            elif move == "stat":
                spyro.return_player_stats()
                time.sleep(3)
            else:
                print("Invalid move. Enter w,a,s,d.")
                time.sleep(2)
