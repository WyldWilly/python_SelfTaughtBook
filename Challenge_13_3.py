#!/usr/bin/env python3

print()
print()
# Create a class called Shape. Define a method in it called
# what_am_i that prints "I am a shape" when called. Change your
# Square and Rectangle classes from the previous challenges to inherit
# from Shape, create Square and Rectangle objects, and
# call the new method on both of them.


print("#3")
print("----------------")
print()


class Shape:
    def what_am_i(self):
        print("I am a shape.")
        

class Rectangle(Shape):
    def __init__(self, lg, wd):
        self.length = lg
        self.width = wd
        print("Created Rectangle")

    def Rec_calculate_perimeter(self):
        return (2*(self.length + self.width))
        

class Square(Shape):
    def __init__(self, s1):
        self.side = s1
        print("Created Square")
        
    def Sq_calculate_perimeter(self):
        return (4 * self.side)


a_rectangle = Rectangle(20,50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()
print()
print(a_rectangle.Rec_calculate_perimeter())
print(a_square.Sq_calculate_perimeter())
