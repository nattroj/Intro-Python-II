import os, sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", 
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

torch = Item('torch', 'light up the way')
sword = Item('sword', 'cut things')
shield = Item('shield', 'block thangs')
towel = Item('towel', 'wipe stuff')
gold_coin = Item('goldcoin', 'buy stuffs')

room['outside'].addItem(torch)
room['foyer'].addItem(sword)
room['foyer'].addItem(shield)
room['overlook'].addItem(towel)
room['treasure'].addItem(gold_coin)

def main():
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

    valid_directions = ('n','e','s','w')

    while True:
        os.system(clear)
        print(player.current_room)

        cmd = input('command> ').strip().lower()
        os.system(clear)

        if cmd in valid_directions:
            player.move(cmd)

        elif cmd in ['i', 'inventory']:
            player.viewInventory()
        
        elif len((cmd_string := cmd.split(' '))) == 2:
            action, obj = cmd_string
            if action == 'get':
                player.getItem(obj)

            elif action == 'drop':
                player.dropItem(obj)

            else:
                print(f'Error: action "{action}" not found...')
                
        elif cmd in ['q', 'quit', 'exit']:
            os.system(clear)
            quit()

        else:
            print(f'Error: command "{cmd}" is invalid')

        print()
        input('press ENTER to continue')

if __name__ == '__main__':
    main()