#!/usr/bin/env python3

print()
print()
# Change the Square class so that when you print a Square Object,
# a message prints telling you the Len of each of the four sides
# of the shape. For example, if you create a square with Square(29),
# and print it, Python should print 29 by 29 by 29 by 29.

print("Chp 14 #2")
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

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1)

a_square = Square(29)
print(a_square)
b_square = Square(93)
print(b_square)