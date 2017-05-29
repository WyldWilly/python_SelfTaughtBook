#!/usr/bin/env python3

print()
print()
# Create Rectangle and Square classes with a method called
# calculate_perimeter that calculates the perimeter of the
# shapes they represent. Create Rectangle and Square objects
# and call the method on both of them.

print("#1")
print("----------------")
print()


class Rectangle:
    def __init__(self, lg, wd):
        self.length = lg
        self.width = wd
        print("Created Rectangle")

    def Rec_calculate_perimeter(self):
        return (2*(self.length + self.width))
        


class Square:
    def __init__(self, s1):
        self.side = s1
        print("Created Square")
        
    def Sq_calculate_perimeter(self):
        return (4 * self.side)


a_rectangle = Rectangle(5,10)
print()
a_square = Square(5)
print()

print(a_rectangle.Rec_calculate_perimeter())
print(a_square.Sq_calculate_perimeter())


