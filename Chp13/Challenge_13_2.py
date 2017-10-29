#!/usr/bin/env python3

print()
print()
# Define a method in your Square class called change_size
# that allows you to pass in a number that increases or
# decreases (if the number is negative) each side of a
# Square object by that number.

print("#2")
print("----------------")
print()

class Square:
    def __init__(self, s1):
        self.side = s1
        print("Created Square")
        
    def Sq_calculate_perimeter(self):
        return (4 * self.side)
    
    def Sq_change_size(self, new_size):
        self.side = new_size
        

a_square = Square(100)
print(a_square.side)
print()

a_square.Sq_change_size(200)
print(a_square.side)
