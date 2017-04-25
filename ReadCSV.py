#!/usr/bin/env python3

import csv

print("----------------")
print()
F2 = open("E:/Git/python_SelfTaughtBook/Chp9/Mylist.csv", "r")
r = csv.reader(F2, delimiter=",")
for row in r:
    print(", ".join(row))
    
F2.close
