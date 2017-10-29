#!/usr/bin/env python3

print()
print()
# create a triangle class with a method called area that calculates and returns
# its area. Then create a triangle object, call area on it, and print the result
# 

import math

print("#3")
print("----------------")
print()

#------ Methods -------------------------
# Area = ((Height*Base)/2)
def CalcTrArea(Height,Base):
    A = ((Height*Base)/2)
    return A


#----------------------------------------


class Triangle:
    def __init__(self, bas, ht, ang):
        self.base = bas
        self.height = ht
        self.angle = ang
        print("Created Triangle!")

Tri1 = Triangle(10,25,90)
Tri2 = Triangle(15,30,90)
Tri3 = Triangle(25,50,90)

Set = [Tri1,Tri2,Tri3]

for T in Set:
    A = CalcTrArea(T.height,T.base)
    A = str(A)
    T = str(T)
    print("Area of " + T + " is " + A)
    print()
