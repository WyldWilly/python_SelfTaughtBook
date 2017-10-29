#!/usr/bin/env python3

print()
print()
# Make a Hexagon class with a method called calculate_perimeter that calculates and returns
# its perimeter. Then create a Hexagon object, call calculate_perimeter on it and print the results.
# 

print("#4")
print("----------------")
print()

import math

#------ Methods -------------------------
# Perimeter = side * 6
def calc_per(side):
    A = side * 6
    return A    

#----------------------------------------

class Hexagon:
    def __init__(self, si):
        self.side = si
        print("Created Hexagon Object")

Hexa1 = Hexagon(5)
Hexa2 = Hexagon(10)
Hexa3 = Hexagon(15)
Hexa4 = Hexagon(20)
Hexa5 = Hexagon(25)

List = [Hexa1, Hexa2, Hexa3, Hexa4, Hexa5]


for T in List:
    A = calc_per(T.side)
    A = str(A)
    T = str(T)
    print("The perimeter of " + T + " is " + A)
    print()
    