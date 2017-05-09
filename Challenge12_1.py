#!/usr/bin/env python3

print()
print()
# Define a class called Apple with four instance variables that represtn 4 attributes of an apple

print("#1")
print("----------------")
print()

class Apple:
    def __init__(self, si, co, ty, se, cnt):
        self.size = si
        self.color = co
        self.type = ty
        self.season = se
        self.count = cnt
        print("Created Apple!")

# Instantiating a class

App1 = Apple("Med", "Red", "Red Delicious", "All", 20)
App2 = Apple("Lrg", "Red Yellow", "Honey Crisp", "Fall", 55)
App3 = Apple("Med", "Green", "Granny Smith", "Fall", 55)

for p in range(1,3):
    p = str(p)
    j = "App" + p
    j = str(j)
    print(j)
    print(j.size)
    print(j.color)
    print(j.type)
    print(j.season)
    print(j.count)
    print()
    print()




