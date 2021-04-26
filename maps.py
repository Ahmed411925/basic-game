# Course: CS 30
# Period: 1
# Date created: 21/04/10
# Date last modified: 21/04/15
# Name: Ahmed Keshta
# Description: Map module for RPG game


import player
import classes
from player import Player
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
    grid[classes.spider.y][classes.spider.x] = 'E'
    grid[classes.alien.y][classes.alien.x] = 'E'
    grid[classes.zombie.y][classes.zombie.x] = 'E'
    grid[key.y][key.x] = key.marker
    if player.y > 4:
        player.y = 4
    grid[player.y][player.x] = '⯐'
    for row in grid:
        if Fire.check == 1:
            grid[0][Fire.x] = '⧮'
            grid[1][Fire.x] = '⧮'
            grid[2][Fire.x] = '⧮'
            grid[3][Fire.x] = '⧮'
            grid[4][Fire.x] = '⧮'
        print(separator.join(row))
