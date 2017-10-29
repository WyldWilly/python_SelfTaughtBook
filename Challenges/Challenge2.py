#!/usr/bin/env python3

print("#1")
def upit(x):
    """
    Takes x and multiples it by itself
    """
    return x * x

a = input("enter a number:") 
a = int(a)
b = upit(a)
print(b)

print()
print()
print("#2")
def stcon(s):
    """
    Takes the string and prints it.
    """
    print(s)
    
s = input("enter a string: ")
s = str(s)
stcon(s)

print()
print()
print("#3")

def Params(x, y, z, a=2, b=4):
    """
    X, Y and Z are Required Parameters
    A and B are Optional Parameters
    """
    return x + y + z + a + b

result = Params(1,2,3,10)
print(result)


print()
print()
print("#4")

def pd2(x):
    """
    Takes the parameter and divides it by 2
    """
    x = int(x)
    return x / 2

def md4(y):
    """
    Takes the parameter passed and multiplies it by 4
    """
    y = int(y)
    return y * 4

a = input("Enter number: ")
b = pd2(a)
c = md4(b)
print(b)
print(c)


print()
print()
print("#5")

def c2s(a):
    """
    Takes the parameter and converts it to a float
    """
    a = float(a)
    return a

try:
    a = input("Enter a number as a string: ")
    a = int(a)
    R = c2s(a)
    print(R)
    
    
except(ValueError):
    print("Not a number!")
    

print()
print()
print("#6")
print("added Doc String to the others")