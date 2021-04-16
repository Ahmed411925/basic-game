# Course: CS 30
# Period: 1
# Date created: 21/04/10
# Date last modified: 21/04/15
# Name: Ahmed Keshta
# Description: Menu module for RPG game


import player
import data


h = player.hunger
mh = player.maxHung
y = player.y
x = player.x


# defining function for printing inventory
def printInv():
    separator = " "
    print('Inventory:')
    print(f'\n{separator.join(data.inv)}\n')


# creating menu function for selecting actions
def menu():
    print('Available options:')
    print('1) Move')
    print('2) Inventory')
    print('3) Use item')
    print('4) Quit')
    choice = input(f'What would you like to do?\n')

# creating option to move around the map
    if choice == "1" or choice.lower() == 'move':
        print('Where would you like to move:')
        print('1) Up')
        print('2) Down')
        print('3) Left')
        print('4) Right')
        choice = input()

        if choice == '1' and y > 0 or choice.lower() == 'up' and y > 0:
            y = y - 1
            choice = ''

        elif choice == '2' and y < 4 or choice.lower() == 'down' and y < 4:
            y = y + 1
            choice = ''

        elif choice == '3' and x > 0 or choice.lower() == 'left' and x > 0:
            x = x - 1
            choice = ''

        elif choice == '4' and x < 9 or choice.lower() == 'right' and x < 9:
            x = x + 1
            choice = ''

        else:
            print("That is not a valid option!")

# creating option to view inventory
    elif choice == "2" or choice.lower() == 'inventory':
        printInv()

# creating option to use an item
    elif choice == "3" or choice.lower() == 'use an item':
        a = 1
        for item in data.inv:
            print(f'{a}) {item.title()}')
            a += 1
        choice = input(f'What would you like to use?\n')
        if choice == '1' or choice.lower() == 'sword':
            if player.combat == 1:
                print(f'{player.name.title()} used their Sword')
                enemy.health = enemy.health - data.sword('damage')
            else:
                print('You cannot use this while not in combat')
            choice = ''

        elif choice == '2' or choice.lower() == 'shield':
            if player.combat == 1:
                print(f'{player.name.title()} used their Shield')
                player.shield = 1
            else:
                print('You cannot use this while not in combat')
            choice = ''

        elif choice == '3' or choice.lower() == 'bandage':
            if player.health < player.maxHealth:
                player.heal(data.bandage('heal'))
                if player.health > player.maxHealth:
                    player.health = player.maxHealth
                
            else:
                print(f'{player.name.title()} is already at maximum health')
            choice = ''

        elif choice == '4' or choice.lower() == 'apple':
            if h < mh:
                player.hunger = player.hunger + data.apple('hunger')
                if h > mh:
                    h = mh
            else:
                print(f'{player.name.title()} is full')
            choice = ''

        else:
            print("That is not a valid option!")

# creating option to quit game
    elif choice == "4" or choice.lower() == 'quit':
        exit()

    else:
        print("That is not a valid option!")
