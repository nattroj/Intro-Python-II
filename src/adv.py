import os, sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item('torch', 'light up the way')]
                    ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

clear = 'cls' if 'win' in sys.platform else 'clear'
os.system(clear)
player_name = input('Enter your name: ')
player = Player(player_name, room['outside'])

os.system(clear)
print(f'Welcome, {player.name}!')
print()
print('press ENTER to continue')
input()

while True:
    os.system(clear)
    print(f'Room: {player.current_room.name}')
    print()
    print(f'Description: {player.current_room.description}')
    print()
    player.current_room.viewContents()

    cmd = input('command> ').strip().lower()
    os.system(clear)

    if cmd in ['n','e','s','w']:
        if cmd == 'n' and player.current_room.n_to:
            player.current_room = player.current_room.n_to
        elif cmd == 'e' and player.current_room.e_to:
            player.current_room = player.current_room.e_to
        elif cmd == 's' and player.current_room.s_to:
            player.current_room = player.current_room.s_to
        elif cmd == 'w' and player.current_room.w_to:
            player.current_room = player.current_room.w_to
        else:
            print('Error: There is no room there!')
            print()
            input('press ENTER to continue')
        continue
    
    if cmd in ['i', 'inventory']:
        player.viewInventory()
        print()
        input('press ENTER to continue')
        continue
    
    if len((cmds := cmd.split(' '))) == 2:
        if cmds[0] == 'get':
            item = cmds[1]
            obtained = None

            for i, _item in enumerate(player.current_room.items):
                if item == _item.name:
                    obtained = player.current_room.items.pop(i)
                    break

            if obtained:
                player.inventory.append(obtained)
                obtained.on_take()
            else:
                print('Error: that item does not exist in this room')

        elif cmds[0] == 'drop':
            item = cmds[1]
            dropped = None
            for i, _item in enumerate(player.inventory):
                if item == _item.name:
                    dropped = player.inventory.pop(i)
                    break
            
            if dropped:
                dropped.on_drop()
            else:
                print('Error: that item is not in the inventory')

        else:
            print(f'Error: action "{cmds[0]}" not found...')

        print()
        input('press ENTER to continue')
        continue

            
    if cmd in ['q', 'quit', 'exit']:
        quit()

    print(f'Error: command "{cmd}" is invalid')