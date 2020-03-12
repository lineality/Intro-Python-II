# v2 using room descriptions from class

# template for repl from RockPaperScissers
import random

# Specification
# The /src directory contains the files adv.py, which is where the main logic for the game should live, room.py, which will contain the definition of the Room class, and player.py, which will contain the definition of the Player class.

# Add a REPL parser to adv.py that accepts directional commands to move the player

# After each move, the REPL should print the name and description of the player's current room
# Valid commands are n, s, e and w which move the player North, South, East or West
# The parser should print an error if the player tries to move where there is no room.
# Put the Room class in room.py based on what you see in adv.py.

# The room should have name and description attributes.

# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

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

# Player Location
x = 0
y = 0

# moving in the cardinal directions
movement_direction_choices = ['n', 's', 'e', 'w']


#stats1:
health = 0
strength = 0
stamina = 0
magica = 0
character_class_modifier = 0


#stats2:
earth = 0
air = 0
fire = 0
metal = 0
wood = 0

elemnt_choices = ['e', 'a', 'f', 'm', 'w']


# room names automatically adjuct to coordinates
room_choices = ['room0_0', 'room0_1']

# variable
new_room_description = ''

# preliminary test (not yet all mapped)
# Room descriptions
room0_0 = "outside: Outside Cave Entrance, North of you, the cave mount beckons"
room0_1 = 'The narrow passage bends here from west to north. The smell of gold permeates the air.'


# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }

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

    # X and Y vectors translate into:
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

    # The updated vectors are turned into the coordinates of the room
    # which is the same as the room-id
    new_room_location = (x, y)

    # this output the id of the new room, as coordinates in a tuple
    return new_room_location


# this function updates the global (or desired)
#  variable of the player location
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

    # returns updated location values
    return x,y


# LOOP
while True:
    # PRINT
    # print("These are your current stats.")
    # print(f"Stats: Health:{health} / Strength:{strength} / Stamina:{stamina} / Magica:{magica} / Character Class Modifier:{character_class_modifier}")
    # print(f"Elemental Stats: {earth} / {air} / {fire} / {metal} / {wood}")

    # print the current location of the player
    print(f"You are now in room{x}_{y}. Where do you want to go next?")

    # READ

    # this is what the player will do
    player_move = input("-> ")


    # EVALUATE
    # If player enter "quit", then quit the loop
    if player_move == "quit":
        print("Goodbye!")
        break

    elif player_move in movement_direction_choices:

        # find out where the player moved:
        starting_location = (x, y)
        
        # updates room and player location to where the player
        # chose to move, if a valid move.
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