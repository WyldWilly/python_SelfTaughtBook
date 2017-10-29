#!/usr/bin/env python3

print()
print()
# Call a different function from teh statistics module

print("#1")
print("----------------")
print()

import statistics
data = [14,3,11,133,4]
result1 = statistics.median_low(data)
print(result1)



print()
print()
# Create a module named cubed with a function that takes a number
# as a parameter, and returns the number cubed. Import and call
# the function from another module.

print("#2")
print("----------------")
print()

import cubed

a = input("enter a number: ")
a = int(a)
result = cubed.cube_it(a)
print(result)
    






