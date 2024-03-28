import random
import time


# prints box 1
def center(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif x < 5 and y == 0:
                print('*', end="")
            elif x > 5 and y == 0:
                print('*', end="")
            elif y < 5 and x == 0:
                print('*', end="")
            elif y > 5 and x == 0:
                print('*', end="")
            elif x < 5 and y == size - 1:
                print('*', end="")
            elif x > 5 and y == size - 1:
                print('*', end="")
            elif y < 5 and x == size - 1:
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
# prints box 1


# prints box 2
def left(sprite_position):
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
            elif y == size - 1:
                print('*', end="")
            elif y < 5 and x == size - 1:
                print('*', end="")
            elif y > 5 and x == size - 1:
                print('*', end="")
            # the box
            # items in room
            elif x == 1 and y == 5:
                print("C", end="")
            elif x == 3 and y == 5:
                print("M", end="")
            elif y in [4, 6]:
                print('*', end="")
            elif y == 5 and x in [4, 6, 8,]:
                print('|', end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()
# prints box 2


# prints box 3
def down(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif x == 0:
                print('*', end="")
            elif x < 5 and y == 0:
                print('*', end="")
            elif x > 5 and y == 0:
                print('*', end="")
            elif y == size - 1:
                print('*', end="")
            elif x == size - 1:
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
# prints box 3


# prints box 4
def right(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('p', end="")
            # the box
            elif y == 0:
                print('*', end="")
            elif y < 5 and x == 0:
                print('*', end="")
            elif y > 5 and x == 0:
                print('*', end="")
            elif y == size - 1:
                print('*', end="")
            elif x == size - 1:
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
# prints box 4


# prints box 5
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
# prints box 5


# the random chest
def chest():
    coins = random.randint(1, 100)  # coin system
    print("Searching for coins...")
    time.sleep(4)
    if coins == 69 or coins == 5 or coins == 89 or coins == 53:
        print(
            "You found loot worth " + str(coins) + " coins!\nHead back to the shop to trade them in for some goodies ")
        print("A spider jumps out at you stinging you and causing " + str(coins / 2) + " damage\n:(")
        spyro.riches("Decrease", coins / 2)
        time.sleep(5)
        return
    else:
        print(
            "You found loot worth " + str(coins) + " coins!\nHead back to the shop to trade them in for some goodies ")
        spyro.riches("Increase", coins)
        time.sleep(3)


# the shop
def shop(message_condition):
    shopitems = ["Health Elixir", "Better Sword", "Piece of Armour", ]

    if message_condition == 1:
        print("welcome to the shop\n", shopitems)
        item = input("what would you like to inspect or type Leave to leave: ")
    else:
        print(shopitems)
        item = input("what would you like to inspect or type Leave to leave: ")

    if item == "Leave":
        if spyro.get_balance() < 10:
            print("you awkwardly leave the shop and smash something on they way out")
            print("you dont have enough coin for the pot you broke so the shop keeper starts roasting you "
                  "then beats you up\n -10 hp and defence for next fight")
            spyro.health("Decrease", 10)
            spyro.defence("Decrease", 10)
            time.sleep(3)
        else:
            print("you awkwardly leave the shop and smash something on they way out\n -10 coin")
            spyro.riches("Decrease", 10)
            time.sleep(3)

    elif item == "Health Elixir":
        print("the health elixir increases your hp by 10 but costs 50 coin")
        outcome = input("B to buy\nL to go back\nEnter option: ")

        if outcome != "L" or outcome != "B":
            while outcome != "L" and outcome != "B":
                outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome == "B":
            if spyro.get_balance() >= 50:
                spyro.health("Increase", 10)
                spyro.riches("Decrease", 50)
            else:
                print("Your broke ass can't afford this")

                outcome2 = input("L to go back: ")
                while outcome2 != "L" and outcome2 != "B":
                    outcome2 = input("L to go back: ")
                time.sleep(1)

                shop(message_condition=0)
        else:
            shop(message_condition=1)

    elif item == "Better Sword":
        print("you spot a shiny sword that is better than yours\nattack increased by 10 but costs 60 coin")
        outcome = input("B to buy\nL to go back\nEnter option: ")

        if outcome != "L" or outcome != "B":
            while outcome != "L" and outcome != "B":
                outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome == "B":
            if spyro.get_balance() >= 60:
                spyro.health("Increase", 10)
                spyro.riches("Decrease", 60)
            else:
                print("Your broke ass can't afford this")

                outcome2 = input("L to go back: ")
                while outcome2 != "L" and outcome2 != "B":
                    outcome2 = input("L to go back: ")
                time.sleep(1)
                shop(message_condition=0)
        else:
            shop(message_condition=1)

    elif item == "Piece of Armour":
        print("you spot a shiny piece of armour to add to yourself\ndefence increased by 10 but costs 40 coins")
        outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome != "L" or outcome != "B":
            while outcome != "L" and outcome != "B":
                outcome = input("B to buy\nL to go back\nEnter option: ")
        if outcome == "B":
            if spyro.get_balance() >= 40:
                spyro.health("Increase", 10)
                spyro.riches("Decrease", 40)
            else:
                print("Your broke ass can't afford this")

                outcome2 = input("L to go back: ")
                while outcome2 != "L" and outcome2 != "B":
                    outcome2 = input("L to go back: ")
                time.sleep(1)
                shop(message_condition=0)
        else:
            shop(message_condition=1)

    else:
        print("you murmur something and the shop attendant asks you to leave "
              "\nyou trip and break your neck, arm and legs on the way out"
              "\n-1 hp")
        spyro.health("decrease", 1)
        time.sleep(2)


# this is the function to move the sprite in boundary and stop him if it's a wall also change maps
def move_sprite(position, direction):
    x, y = position
    # this is for the center map and connections to other worlds
    if direction == "a" and y == 5 and x == 1 and num == 1:  # left map
        maps = "2"
        return maps
    elif direction == "w" and y == 1 and x == 5 and num == 1:  # up map
        if spyro.amount_keys() == 3:
            print("you unlock the bulky door and step through")
            time.sleep(3)
            maps = "5"
            return maps
        else:
            print("you done have the keys to open this door yet\ngo get them monsters!!")
            time.sleep(2)
    elif direction == "d" and y == 5 and x == 9 and num == 1:  # right map
        maps = "4"
        return maps
    elif direction == "s" and y == 9 and x == 5 and num == 1:  # down map
        maps = "3"
        return maps
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
        input("press anything to enter shop: ")
        shop(message_condition=1)
        x += 1
    elif direction == "w" and x == 9 and y == 8 and num == 1:
        input("press anything to enter shop: ")
        shop(message_condition=1)
        y -= 1
    elif direction == "s" and x == 9 and y == 6 and num == 1:
        input("press anything to enter shop: ")
        shop(message_condition=1)
        y += 1
    # this is for the chest
    elif direction == "d" and x == 4 and y == 7 and num == 1:
        input("press anything to open chest: ")
        chest()
        x += 1
    elif direction == "a" and x == 6 and y == 7 and num == 1:
        input("press anything to open chest: ")
        chest()
        x -= 1
    elif direction == "s" and x == 5 and y == 6 and num == 1:
        input("press anything to open chest: ")
        chest()
        y += 1
    elif direction == "w" and x == 5 and y == 8 and num == 1:
        input("press anything to open chest: ")
        chest()
        y -= 1
    # end of the interact chest
    # for wall interact
    elif num == 4 and y == 5 and x in [1, 2, 3, 4, 5, 6] and direction in ["w", "s"]:
        print("that's a wall")
        time.sleep(2)
    elif num == 4 and y in [1, 2, 3, 4, 6, 7, 8, 9] and x == 7 and direction == "a":
        print("that's a wall")
        time.sleep(2)
    elif num == 2 and y == 5 and direction in ["w", "s"]:
        print("that's a wall")
        time.sleep(2)
    elif num == 5 and y == 5 and x in [1, 2, 3, 4, 6, 7, 8, 9] and direction == "w":
        print("that's a wall")
        time.sleep(2)
    elif num == 5 and y == 3 and x in [1, 2, 3, 4, 6, 7, 8, 9] and direction == "s":
        print("that's a wall")
        time.sleep(2)
    elif num == 5 and y == 4 and x == 5 and direction in ["a", "d"]:
        print("that's a wall")
        time.sleep(2)
    elif (num == 3 and y in [1, 5] and x in [2, 3, 4, 5, 6, 7, 8] and direction in ["s", "w"] or num == 3 and y == 5 and
          x == 9 and direction == "s"):
        print("that's a wall")
        time.sleep(2)
    # for wall interact
    # moving code
    elif direction == 'w' and y > 1:
        y -= 1
    elif direction == 's' and y < 9:
        y += 1
    elif direction == 'a' and x > 1:
        x -= 1
    elif direction == 'd' and x < 9:
        x += 1
    # moving code

    # "that's a wall" code
    elif direction == 'a' or "d" and x == 2:  # this is for left
        print("that's a wall")
        time.sleep(3)
    elif direction == 's' or "w" and y == 2 or 8:  # this one is for the bottom and top
        print("that's a wall")
        time.sleep(3)
    # "that's a wall" code

    return x, y
# this is the function to move the sprite in boundary and stop him if it's a wall


# this is for all entity's in game to get assigned stats
class Entity:
    hp = 100
    defe = 100
    att = 100
    bank = 0
    key = 3

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

    def keys(self):
        self.key += 1

    def return_player_stats(self):
        print("your hp is " + str(self.hp))
        print("your defence is " + str(self.defe))
        print("your attack is " + str(self.att))
        print("you have " + str(self.bank) + " coins")
        print("you have " + str(self.key) + "/3 keys")

    def get_balance(self):  # Retrieves the entities account balance
        return self.bank

    def amount_keys(self):
        return self.key

# this is for all entity's in game to get assigned stats


# ---------------------------------------------------------------------------------------------------------
# INITIAL POS
sprite_position = (5, 5)
# difficulty selection
print("You are spyro\nBowser has kidnapped your dog\ngo on a murderous rampage in his dungeon and save that pup\n"
      "Bowser locked the door to his room but his three monster guards have the keys\nkill them to take the keys")
time.sleep(0)
difficulty = input("Enter E to play on easy or H to play on hard: ")
if difficulty != "E" or "H":
    while difficulty != "E" and difficulty != "H":
        difficulty = input("Invalid selection\n Press either H or E then press enter: ")
# entity creation
spyro = Entity()
monster1 = Entity()
monster2 = Entity()
lord_phalp = Entity()
# difficulty activated
if difficulty == "E":
    spyro.health("Increase", 30)
    spyro.attack("Increase", 30)
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
    monster1.defence("Decrease", 15)

    monster2.health("Decrease", 15)
    monster2.attack("Increase", 15)  # speed demon
    monster2.defence("Increase", 15)

    lord_phalp.health("Decrease", 15)
    lord_phalp.attack("Decrease", 15)  # jack of all trades
    lord_phalp.defence("Decrease", 15)

# CORE GAME LOOP
num = 1
while True:
    if num == 1:
        while True:
            center(sprite_position)
            move = input("check stats = stat\nMove sprite (w, a, s, d): ")  # start map
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
    elif num == 2:
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
    elif num == 3:
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
    elif num == 4:
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
    elif num == 5:
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
