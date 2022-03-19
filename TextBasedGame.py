# Garrett Dunn
# Project 2
# IT140
# Southern New Hampshire University
# 02/21/2021
# a dictionary containing all rooms and their
# possible directions



import os

name = os.name

rooms = {
    'Slimy Room': {
        'East': 'Mezzanine'
    },
    'Mezzanine': {
        'North': 'Room full of Alien eggs',
        'East': 'Server Room',
        'South': 'Study',
        'West': 'Slimy Room'
    },
    'Room full of Alien eggs': {
        'East': 'Lab',
        'South': 'Mezzanine',
        'West': 'Weapon Room'
    },
    'Lab': {
        'West': 'Room full of Alien eggs'
    },
    'Weapon Room': {
        'East': 'Room full of Alien eggs'
    },
    'Server Room': {
        'East': 'Control Room',
        'West': 'Mezzanine'
    },
    'Control Room': {
        'West': 'Server Room'
    },
    'Study': {
        'North': 'Mezzanine',
        'East': 'Storage Room'
    },
    'Storage Room': {
        'West': 'Study'
    }
}
# dictionary of items
items = {
    'Slimy Room': 'Journal',
    'Mezzanine': '',
    'Room full of Alien eggs': '',
    'Lab': 'Phone',
    'Weapon Room': 'Plasma Gun',
    'Study': 'Alien Book',
    'Storage Room': 'Wallet',
    'Server Room': 'Souvenir',
    'Control Room': 'Alien'
}
# set current room variable
state = 'Slimy Room'
# variable for item list
inventory = []
# print welcome message/instructions
print('Welcome to the Alien Adventure game!\n'
      'Move through the rooms by typing North, East, South, and West.\n'
      'Collect 4 items to defeat the Alien in the Control Room!\n'
      'Good luck!')
# defining movement function
def get_new_state(state, direction):
    new_state = state
    for i in rooms:
        if i == state:
            if direction in rooms[i]:
                new_state = rooms[i][direction]
    return new_state
# establishing gameplay loop
while 1:
    print('\nYou are in the', state)
    if state == 'Control Room':
        print('You are battling the Alien!', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print("-", end='', flush=True)
        print()
        if len(inventory) >= 4:
            print('You have defeated the Alien! Congratulations!')
        else:
            print("You didn't have enough items and failed to defeat the Alien.\n"
                  "Better luck next time!")
        break
    # establishing available items/current inventory/direction variable
    print('Items available in this room:', items[state])
    print('Items in your inventory:', inventory)
    direction = input('Enter item you want OR direction to go OR exit to give up: ')
    # item acquisition statement
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    # direction statement
    direction = direction.capitalize()
    if direction == 'Exit':
        exit(0)
    elif direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':
        new_state = get_new_state(state, direction)
        if new_state == state:
            print('\nYou sense something dark in that direction, enter another direction fast!')
        else:
            state = new_state
    else:
        print('\nInvalid command!')

addPause = input("\nPress any key to continue")
