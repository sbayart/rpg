#!/usr/bin/env python
# -- coding: UTF-8 --

class Item():
    def __init__(self):
        self.weight = Integer

    def use(self):

class Weapon(Item):
    def __init__(self):
        self.dammage = Integer

class Armor(Item):
    def __init__(self):
        self.defend = Integer

class Helmet(Armor):
    def __init__(self):

class Shield(Armor):
    def __init__(self):

class Food(Item)
    def __init__(self):
        self.gain = Integer
