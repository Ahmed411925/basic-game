# Course: CS 30
# Period: 1
# Date created: 21/04/10
# Date last modified: 21/04/15
# Name: Ahmed Keshta
# Description: Player data module for rpg game


import data


# starting position for player
startPos = [0, 0]


# defining starting variables for player
maxHealth = 100
name = input(f'What is your name:\n')
x = startPos[0]
y = startPos[1]
health = 100
shield = 0
combat = 0


# creating class for player
class Player:
    def __init__(self, name, health, maxHealth, x, y, shield):
        self.health = health
        self.maxHealth = maxHealth
        self.shield = shield
        self.name = name
        self.x = x
        self.y = y

    def heal(self, amount):
        '''
        heal function for player class using bandages
        '''
        self.health += amount


player = Player(name, health, maxHealth, x, y, shield)
