# Implement a class to hold room information. This should have name and
# description attributes.

# working room repl

# template for repl from RockPaperScissers
import random

# Create a RPS game where player can type r, p or s, the computer chooses
# a random move, and the game tells you who won.

# You should be able to play multiple games and the game will tell you
# Your score after each round.

# Type quit to quit.

# Create a REPL

# location and direction
# use a coordinate system for the room location and ID
# and use cardinal directions to navigate through the coordinate system

# X and Y vectors translate into
# North
# if n = y += 1
# South
# if s = y -= 1
# East
# if e = x += 1
# West
# if w = x -= 1



x = 0
y = 0

# north
movement_direction_choices = ['n', 's', 'e','w']

# the first 4 rooms are 


#stats1:
health = 0
strength = 0
stamina = 0
magica = 0
character_class_modifier = 0

stat_choices = ['r', 'p', 's']

#stats2:
earth = 0
air = 0
fire = 0
metal = 0
wood = 0

elemnt_choices = ['e', 'a', 'f', 'm', 'w']

# room0_0 = (0, 0)
# room0_1 = (0, 1)
#room_choices = ['room0_0', 'room0_1']
room_choices = ['room0_0', 'room0_1']

new_room_description = ''
room0_0 = 'This is where your adventure starts. It looks like an apple.'
room0_1 = 'This room opens into a peanut shape, and smell like mint.'

#https://www.daniweb.com/programming/software-development/threads/111526/setting-a-string-as-a-variable-name
# food = 'bread'
# vars()[food] = 123
# print(bread)  # --> 123

# Room location system
# when player moves to a new room
# print what room that player moves to
# new_room = '{bread}'
# vars()[new_room] = 123
# print(bread)  # --> 123

# new_room = f'room{new_room_location[0]}_{new_room_location[1]}'
# vars()[new_room]
# print(room0_0)  # --> 123



# Define a function that compares player and cpu moves
# and returns 1 for a win, 0 for tie, -1 for loss



def player_move_and_outcome(player_move,x,y):

    # X and Y vectors translate into
    # North
    # if n = y += 1
    # South
    # if s = y -= 1
    # East
    # if e = x += 1
    # West
    # if w = x -= 1

    # North
    if player_move == "n":
        y += 1
    # South
    elif player_move == "s":
        y -= 1
    # East
    elif player_move == "e":
        x += 1 
    # West
    elif player_move == "w":
        x -= 1

    new_room_location = (x, y)

    return new_room_location

def update_xy(player_move, x,y):
    # North
    if player_move == "n":
        y += 1
    # South
    elif player_move == "s":
        y -= 1
    # East
    elif player_move == "e":
        x += 1 
    # West
    elif player_move == "w":
        x -= 1

    return x,y


# LOOP
while True:
    # PRINT
    print(f"Stats: {health} / {strength} / {stamina} / {magica} / {character_class_modifier}")
    # READ

    # print the current location of the player
    print(f"You are now in room{x}_{y}. Where do you want to go next?")

    player_move = input("-> ")
    # EVALUATE
    # If player enter "quit", then quit the loop
    if player_move == "quit":
        print("Goodbye!")
        break
    elif player_move in movement_direction_choices:

        # find out where the player moved:
        starting_location = (x, y)
        


        new_room_location = player_move_and_outcome(player_move,x,y)
        x, y = update_xy(player_move, x,y)

        # if the new room location is valid, proceed to that room

        #print(f"You have chosen to try to move to room {new_room_location}.")

        # match room location to 
        # mask: getting x vector for name
        x_part_of_room_name = new_room_location[0]
        # mask: getting y vector for name
        y_part_of_room_name = new_room_location[1]
        new_room_name = f"room{x_part_of_room_name}_{y_part_of_room_name}"

        # inspections
        #print(new_room_name, room_choices)


        if new_room_name in room_choices:
            print(f"You have moved to room {new_room_name}.")

            print(x,y)

            # match room location to 
            # mask: getting x vector for name
            x_part_of_room_name = new_room_location[0]
            # mask: getting y vector for name
            y_part_of_room_name = new_room_location[1]
            new_room_description = vars()[f"room{x_part_of_room_name}_{y_part_of_room_name}"]
            #print(f"This room looks like {new_room_description}")
            print(new_room_description)



        # else: show an error and move the play back to where they were
        else:
            new_room_location = starting_location

            print(f"There is no door in that direction. You are still in room {new_room_location}.")

        # find out what room that is:
        # each room will be an...object? randomly generated?
        # 

    else:
        print("I did not understand that command")
        