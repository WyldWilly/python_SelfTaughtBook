#!/usr/bin/env python3

print()
print()
# Add a square_list class variable to a class called Square so that everytime
# you create a new Square object, the new object gets added to the list.

print("Chp 14 #1")
print("----------------")
print()

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a square.")

a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)
