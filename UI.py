# Course: CS 30
# Period: 1
# Date created: 21/04/10
# Date last modified: 21/04/15
# Name: Ahmed Keshta
# Description: Menu module for RPG game

import char
import classes
import data
import random

y = char.player.y
x = char.player.x
clear = '\n' * 200
death = 0
name = char.player.name.title()


# defining function for printing inventory
def printInv():
    '''
    Function for printing inventory
    '''
    separator = " "
    print(clear)
    print('Inventory:')
    print(f'\n{separator.join(data.inv)}\n')


# creating menu function for selecting actions
def menu():
    '''
    Menu for space station game
    '''
    global name
    global y
    global x

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
        choice = input('\nEnter the number of your choice:')

        if choice == '1' and y > 0 or choice.lower() == 'up' and y > 0:
            print(clear)
            char.player.y = char.player.y - 1
            y -= 1
            choice = ''

        elif choice == '2' and y < 4 or choice.lower() == 'down' and y < 4:
            print(clear)
            char.player.y = char.player.y + 1
            y += 1
            choice = ''

        elif choice == '3' and x > 0 or choice.lower() == 'left' and x > 0:
            print(clear)
            char.player.x = char.player.x - 1
            x -= 1
            choice = ''

        elif choice == '4' and x < 9 or choice.lower() == 'right' and x < 9:
            print(clear)
            char.player.x = char.player.x + 1
            x += 1
            choice = ''

        else:
            print(clear)
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
            if char.player.combat == 1:
                print(clear)
                print(f'{name} used their Sword')
                classes.Enemy.health = classes.Enemy.health - data.sword(
                    'damage')
            else:
                print(clear)
                print('You cannot use this while not in combat')
            choice = ''

        elif choice == '2' or choice.lower() == 'shield':
            if char.player.combat == 1:
                print(clear)
                print(f'{name} used their Shield')
                char.player.shield = 1
            else:
                print(clear)
                print('You cannot use this while not in combat')
            choice = ''

        elif choice == '3' or choice.lower() == 'bandage':
            print(clear)
            if data.bandage['amount'] > 0:
                if char.player.health < char.player.maxHealth:
                    char.player.heal(data.bandage['heal'])
                    data.bandage['amount'] -= 1
                    if char.player.health > char.player.maxHealth:
                        char.player.health = char.player.maxHealth

                else:
                    print(
                        f'{name} is already at maximum health')

            else:
                print('You do not have any more bandages!')
            choice = ''

        else:
            print(clear)
            print("That is not a valid option!")


# creating option to quit game
    elif choice == "4" or choice.lower() == 'quit':
        print(clear)
        exit()

    else:
        print(clear)
        print("That is not a valid option!")


def fight():
    print('What would you like to do?')
    print('1) Swing sword')
    print('2) Equip/Unequip shield')
    print('3) Use bandages')
    print('4) Quit')
    choice = input('\nEnter the number of your choice:')
    print(clear)
    if choice == '1':
        print('You swung your sword!')
        if char.combat == 1:
            classes.spider.health -= 10

        if char.combat == 2:
            classes.alien.health -= 10

        if char.combat == 3:
            classes.zombie.health -= 10

    elif choice == '2':
        if char.shield == 0:
            char.shield = 1
            print('You equipped your shield!')
        else:
            char.shield = 0
            print('You unequipped your shield!')

    elif choice == '3':
        if data.bandage['amount'] > 0:
            print('You healed 10 hitpoints!')
            char.player.heal(10)
            data.bandage['amount'] -= 1

        else:
            print('You don\'t have any more bandages')

        if char.player.health > char.player.maxHealth:
            char.player.health = char.player.maxHealth

    elif choice == '4' or choice.lower() == 'quit':
        exit()

    else:
        print('That is not a valid option!')
        fight()


def inCombat():

    global death

    # combat against a spider
    if char.combat == 1:
        print('\nYou are up against a spider')
        print(f'It has {classes.spider.health} hitpoints remaining\n')
        fight()
        if char.shield == 1:
            char.player.health -= (data.spider['damage']) / 2

        else:
            char.player.health -= (data.spider['damage'])

        if classes.spider.health <= 0:
            char.combat = 0
            classes.spider.kill()
            print('You killed the spider!')
            death += 1

# combat against an alien
    if char.combat == 2:
        print('\nYou are up against an alien')
        print(f'It has {classes.alien.health} hitpoints remaining\n')
        fight()
        if char.shield == 1:
            char.player.health -= (data.alien['damage']) / 2

        else:
            char.player.health -= (data.alien['damage'])

        if classes.alien.health <= 0:
            classes.alien.kill()
            print('The alien has been slain!')
            char.combat = 0
            death += 1


# combat against a zombie
    if char.combat == 3:
        print('\nYou are up against a zombie')
        print(f'It has {classes.zombie.health} hitpoints remaining\n')
        fight()
        if char.shield == 1:
            char.player.health -= (data.zombie['damage']) / 2

        else:
            char.player.health -= (data.zombie['damage'])

        if classes.zombie.health <= 0:
            classes.zombie.kill()
            print('That zombie won\'t be needing any more brains!')
            char.combat = 0
            death += 1
