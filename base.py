import random

def print_box1(sprite_position):
    size = 11
    for y in range(size):
        for x in range(size):
            if sprite_position == (x, y):
                print('S', end="")
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
            elif x == 5 and y == 7:
                print("C", end="")
            elif x == 5 and y == 6:
                print("M", end="")
            # items in room
            # the blank space
            else:
                print(' ', end="")
        print()


def move_sprite(position, direction):
    x, y = position
    if direction == "a" and y == 5 and x == 1: # left map
        sprite_position = (9, 5)
        return sprite_position
    elif direction == "w" and y == 1 and x == 5: # up map
        sprite_position = (5, 9)
        return sprite_position
    elif direction == "d" and y == 5 and x == 9: # right map
        sprite_position = (1, 5)
        return sprite_position
    elif direction == "s" and y == 9 and x == 5: # down map
        sprite_position = (5, 1)
        return sprite_position
    # this is for the chest
    elif x == 5 and y == 7:
        i = 0
        ls = ["cannon", "sword", "gun", "dildo"] # fix this next
        while i < len(ls):
            print(ls[0])
            i += 1
        input("what you want: ")

    # end of the interact chest code
    elif direction == 'w' and y > 1:
        y -= 1
    elif direction == 's' and y < 9:
        y += 1
    elif direction == 'a' and x > 1:
        x -= 1
    elif direction == 'd' and x < 9:
        x += 1
    elif direction == 'a' or "d" and x == 2:  # this is for left
        print("that's a wall")
    elif direction == 's' or "w" and y == 2 or 8:  # this one is for the bottom and top
        print("that's a wall turn around dumbass")
    return x, y


# INITIAL POS
sprite_position = (5, 5)

# CORE GAME LOOP
while True:
    print_box1(sprite_position)
    move = input("Move sprite (w, a, s, d): ")
    if move in ['w', 'a', 's', 'd']:
        sprite_position = move_sprite(sprite_position, move)
    else:
        print("Invalid move. Enter w,a,s,d.")