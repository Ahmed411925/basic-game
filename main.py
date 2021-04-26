# Course: CS 30
# Period: 1
# Date created: 21/03/11
# Date last modified: 21/03/16
# Name: Ahmed Keshta
# Description: RPG Game Mock


import data
import maps
import player
import classes
from classes import key
from menu import menu


clear = '\n' * 200
win = 0


print(f'\nHello {player.name.title()}, you are stuck in a burning space')
print(f'station and must make your way to the escape pod.')
print(f'Watch out for tiles on fire, they will look like')
print(f'this "⧮". You are here ⯐.')
input(f'input anything to enter:\n')
print(clear)


# loop for running through program until win condition is achieved
while win < 1:
    maps.spaceStation()
    print(f'{player.name.title()} has {player.health} hit points')
    menu()
    print(player.y)
    if player.x == classes.Fire.x and classes.Fire.check == 1:
        print('You can\'t go there without a fire extinguisher!'
        '\nObtain one by killing all 3 enemies')
        player.x = player.x - 1
    if player.x == classes.spider.x and player.y == classes.spider.y:
        combat = 1
        print('A giant spider jumped at you from the dark!')
    if player.x == classes.alien.x and player.y == classes.alien.y:
        combat = 2
    if player.x == classes.zombie.x and player.y == classes.zombie.y:
        combat = 3
    if player.x == key.x and player.y == key.y:
        key.grab()
    if player.x == 9 and player.y == 4:
        win = 3


print(f'Congratulations! You have escaped the burning space station!')
