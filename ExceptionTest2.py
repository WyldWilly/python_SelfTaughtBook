#!/usr/bin/env python3

try:
    a = input("type a number:")
    b = input("Type another:")
    a = int(a)
    b = int(b)

    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid Input.")