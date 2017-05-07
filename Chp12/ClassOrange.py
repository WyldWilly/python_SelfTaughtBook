#!/usr/bin/env python3

def PrintObs(or1, or2):
    print(or1.weight)
    print(or1.color)
    print(or1.warpdrive)
    print(or1.power)
    print(or1.shields)
    print()
    print()
    print(or2.weight)
    print(or2.color)
    print(or2.warpdrive)
    print(or2.power)
    print(or2.shields)
    print()
    print()


# Creating a class
class Orange:
    def __init__(self, w, c, wd, pww, sh):
        self.weight = w
        self.color = c
        self.warpdrive = wd
        self.power = pww
        self.shields = sh
        print("Created!")

# Instantiating a class

or1 = Orange(10, "dark orange", 12, 100, 100)
or2 = Orange(12, "light orange", 10, 100, 100)

PrintObs(or1, or2)

or1.weight = 150
or2.power = 90

PrintObs(or1, or2)


