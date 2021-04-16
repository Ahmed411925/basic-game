# Course: CS 30
# Period: 1
# Date created: 21/03/11
# Date last modified: 21/03/16
# Name: Ahmed Keshta
# Description: RPG Game Mock


import data
import maps
import player
from menu import menu


win = 0


print(f'\nHello {player.name.title()}, you are stuck in a burning space')
print(f'station and must make your way to the escape pod.')
print(f'Watch out for tiles on fire, they will look like')
print(f'this "⧮". You are here ⯐.')
input(f'input anything to enter:\n')


while win < 1:
    maps.spaceStation()
    print(f'{player.name.title()} has {player.health} hit points')
    menu()
    if player.x == 9 and player.y == 4:
        win = 2


print(f'Congratulations! You have escaped the burning space station!')
