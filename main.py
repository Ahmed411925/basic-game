# Course: CS 30
# Period: 1
# Date created: 21/03/11
# Date last modified: 21/03/16
# Name: Ahmed Keshta
# Description: RPG Game Mock


import data
import maps
import char
import UI
from char import combat
import classes
from classes import key
from UI import menu
from UI import inCombat
from UI import fight


clear = '\n' * 200
win = 0


print(f'\nHello {char.player.name.title()}, you are stuck in a burning space')
print(f'station and must make your way to the escape pod.')
print(f'Watch out for tiles on fire, they will look like')
print(f'this "⧮". You are here ⯐.')
input(f'input anything to enter:\n')
print(clear)


# loop for running through program until win condition is achieved
while win < 1:
    maps.spaceStation()
    print(f'{char.player.name.title()} has {char.player.health} hit points')
    if char.combat > 0:
        inCombat()
    
    elif char.combat == 0:
        menu()

    if char.player.x == classes.Fire.x and classes.Fire.check == 1:
        print('You can\'t go there without a fire extinguisher!'
        '\nObtain one by killing all 3 enemies')
        char.player.x = char.player.x - 1

    if char.player.x == classes.spider.x and char.player.y == classes.spider.y:
        char.combat = 1
        print('A giant spider jumped at you from the dark!')
        classes.spider.y = 20
        print(char.combat)

    if char.player.x == classes.alien.x and char.player.y == classes.alien.y:
        char.combat = 2
        print('A bloodthirsty alien ambushed you!')
        pass

    if char.player.x == classes.zombie.x and char.player.y == classes.zombie.y:
        char.combat = 3
        print('A hungry zombie is right in front of you!')
        classes.zombie.y = 20
        pass

    if char.player.x == key.x and char.player.y == key.y:
        key.grab()

    if char.player.x == 9 and char.player.y == 4:
        win = 3
    
    if char.player.health <= 0:
        print('You lose!')
        exit()

    if UI.death == 3:
        UI.death += 1
        print('You obtained the fire extinguisher and put out the fire!')
        classes.Fire.check = 0


print(f'Congratulations! You have escaped the burning space station!')
