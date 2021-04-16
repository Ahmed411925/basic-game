# Course: CS 30
# Period: 1
# Date created: 21/04/10
# Date last modified: 21/04/15
# Name: Ahmed Keshta
# Description: Map module for RPG game


import player
from player import Player


# defining function for space station map
def spaceStation():
    separator = " "
    print(f'\n\n\n')
    a = ['▢', '▢', '▢', '▢', '▢', '⧮', '▢', '▢', '▢', '▢']
    b = ['▢', '▢', '▢', '▢', '▢', '⧮', '▢', '▢', '▢', '▢']
    c = ['▢', '▢', '▢', '▢', '▢', '⧮', '▢', '▢', '▢', '▢']
    d = ['▢', '▢', '▢', '▢', '▢', '⧮', '▢', '▢', '▢', '▢']
    e = ['▢', '▢', '▢', '⚿', '▢', '⧮', '▢', '▢', '▢', '◨']
    grid = [a, b, c, d, e]
    grid[player.y][player.x] = '⯐'
    for row in grid:
        print(separator.join(row))
