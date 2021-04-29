# Course: CS 30
# Period: 1
# Date created: 21/04/10
# Date last modified: 21/04/15
# Name: Ahmed Keshta
# Description: Map module for RPG game


import char
import classes
from char import Player
from char import player
from classes import Fire
from classes import Enemy
from classes import key


# defining function for space station map
def spaceStation():
    '''
    Function for printing map and tiles
    '''
    separator = " "
    print(f'\n\n\n')
    a = ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢']
    b = ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢']
    c = ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢']
    d = ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢']
    e = ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '◨']
    grid = [a, b, c, d, e]
    if classes.spider.y < 5:
        grid[classes.spider.y][classes.spider.x] = classes.spider.marker
    if classes.alien.y < 5:
        grid[classes.alien.y][classes.alien.x] = classes.alien.marker
    if classes.zombie.y < 5:
        grid[classes.zombie.y][classes.zombie.x] = classes.zombie.marker
    grid[key.y][key.x] = key.marker
    if char.player.y > 4:
        char.player.y = 4
    grid[char.player.y][char.player.x] = '⯐'
    for row in grid:
        if Fire.check == 1:
            grid[0][Fire.x] = '⧮'
            grid[1][Fire.x] = '⧮'
            grid[2][Fire.x] = '⧮'
            grid[3][Fire.x] = '⧮'
            grid[4][Fire.x] = '⧮'
        print(separator.join(row))
