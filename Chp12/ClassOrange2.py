#!/usr/bin/env python3

def PrintObs(or1):
    print()
    print(or1.weight)
    print(or1.color)
    print(or1.warpdrive)
    print(or1.power)
    print(or1.shields)
    print()




# Creating a class
class Orange:
    def __init__(self, w, c):
        """weights are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
        
    def rot(self, days, temp):
        self.mold = days * temp

# Instantiating a class

orange = Orange(6, "orange")
print(orange.mold)
print()
orange.rot(10,98)
print(orange.mold)