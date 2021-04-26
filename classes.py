# Course: CS 30
# Period: 1
# Date created: 21/04/22
# Date last modified: 21/04/26
# Name: Ahmed Keshta
# Description: Class module for RPG game


import data
from data import inventory
from data import inv


# Enemy base class
class Enemy:
    def __init__(self, name, health, x, y, damage, marker):
        self.health = 100
        self.name = name
        self.x = x
        self.y = y
        self.damage = damage
        self.marker = 'E'
    
    def kill(self):
        combat = 0


# Map tile base class
class mapTile:
    def __init__(self, marker):
        self.marker = marker


# Class for default map tiles
class defTile(mapTile):
    def __init__(self, marker):
        self.marker = '▢'


# tile class containing key
class keyTile(mapTile):

    key = 0
    
    def __init__(self, marker, x, y):
        self.marker = marker
        self.x = x
        self.y = y

    def grab(self):
        '''
        Function for when key is grabbed
        '''
        key = 1
        self.marker = '▢'
        print('You grabbed the key to the escape pod!')
        inv.append('key')


# tile class for tiles on fire
class Fire(mapTile):
    
    check = 1
    x = 5

    def __init__(self, check, x):
        self.x = x
        self.check = check
        self.marker = '⧮'

    def ext(self, check):
        self.check = 0


# spider enemy class
class Spider(Enemy):
    def __init__(self, x, y, health):
        self.health = health
        self.x = x
        self.y = y


# alien enemy class
class Alien(Enemy):
    def __init__(self, x, y, health):
        self.health = health
        self.x = x
        self.y = y


# zombie enemy class
class Zombie(Enemy):
    def __init__(self, x, y, health):
        self.health = health
        self.x = x
        self.y = y


# creation of enemy objects
spider = Spider(2, 1, data.spider['health'])
alien = Alien(3, 3, data.alien['health'])
zombie = Zombie(1, 3, data.zombie['health'])


# creation of key tile object
key = keyTile('⚿', 3, 4)
