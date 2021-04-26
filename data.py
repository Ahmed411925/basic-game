# Course: CS 30
# Period: 1
# Date created: 21/03/11
# Date last modified: 21/03/16
# Name: Ahmed Keshta
# Description: Data module for game


# stats for entities
player = {'name': 'bill', 'health': 100, 'strength': 10, 'hunger': 9}
alien = {'name': 'alien', 'health': 100, 'strength': 10, 'points': 15}
spider = {'name': 'spider', 'health': 10, 'strength': 5, 'points': 5}
zombie = {'name': 'zombie', 'health': 50, 'strength': 10, 'points': 10}


# Item names, descriptions and stats
sword = {
  'name': 'Sword',
  'damage': 10,
  'description': 'Useful for close range enemies'
}


shield = {
  'name': 'Shield',
  'description': 'Reduces incoming damage when equipped'
}


bandage = {
  'name': 'Bandage',
  'description': 'Restores 10 hp to player',
  'heal': 10
}


apple = {
  'name': 'apple',
  'description': 'Restores 2 hunger points',
  'hunger': 2
}


inventory = [sword, shield, bandage, apple]
enemies = [alien, spider, zombie]
inv = []


for item in inventory:
    inv.append(item['name'])


class Inventory:
    def __init__(self, items):
        self.items = inventory
