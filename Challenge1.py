#!/usr/bin/env python3

print("#1")
print("Hello World")
print("Another fine day")
print("Lets go Pens!!!")
print()

x = 40

print("#2")
if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is greater than 10")
print(x)
print()

print("#3")
y =45
if y <= 10:
    print("y is less than or equal to 10")
elif y > 10 and y <= 25:
    print("y is greater then 10 but less then or equal to 25")
elif y > 25:
    print("y is greater than 25")
print(y)
print()

a = 5
b = 10
c = 22
d = 3

print("#4")
d1 = (b/a)
print(d1)
print()
print("#5")
d2 = (c%d)
d3 = (c//d)
print(d3, d2)
print()


print("#6")

age = 26

if age <= 13:
    print("You're too young (10 or under)")
elif age > 13 and age <= 19:
    print("Teenager (13 to 19)")
elif age > 19 and age <= 40:
    print("Welcome to life")
elif age > 40 and age <= 61:
    print("Time to start thinking about retirement (between 40 and 61)")
elif age >61:
    print("Time to retirement (over 61)")
    
print()
print(age)


