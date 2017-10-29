#!/usr/bin/env python3

print()
print()
# Create a Circle class with a method called area that calculates and returns
# its area. then create a Circle object, call area on it, and print the result.
# Use pythons pi function in the built in math method
# 

import math

#------ Methods -------------------------
# Area calculated via Radius
# A = Pi x Rad sq
def CalcRad(Radius):
    A = ((Radius **2) * math.pi)
    return A

# Area calculated via Diameter
# A = (Pi/4) x Diameter sq
def CalcDia(Diameter):
    A = ((math.pi/4)*(Diameter **2))
    return A

# Area calculated via Circumference
# A = Circumferance sq / 4 x Pi
def CalcCirc(Circumference):
    A = ((Circumference **2)/(4 * math.pi))
    return A
#------------------------------------------

print("#2")
print("----------------")
print()

class Crcle:
    def __init__(self, rad, dia, circum):
        self.radius = rad
        self.diameter = dia
        self.circumference = circum
        print("Created Apple!")

Crc1 = Crcle(5,10,25)
Crc2 = Crcle(15,30,100)
Crc3 = Crcle(25,50,300)

Spad = [Crc1, Crc2, Crc3]

# Calc by Radius
for T in Spad:
    A = CalcRad(T.radius)
    A = str(A)
    T = str(T)
    print("The area by Radius for " + T + " is " + A)
print()
print()

# Calc by Diameter
for T in Spad:
    A = CalcRad(T.diameter)
    A = str(A)
    T = str(T)
    print("The area by Diameter for " + T + " is " + A)
print()
print()

# Calc by Circumference
for T in Spad:
    A = CalcRad(T.circumference)
    A = str(A)
    T = str(T)
    print("The area by Circumference for " + T + " is " + A)
print()
print()
