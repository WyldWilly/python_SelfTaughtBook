#!/usr/bin/env python3

print()
print()
# Find a file on your computer and print its contents

print("#1")
print("----------------")
print()
with open("E:/Git/python_SelfTaughtBook/Chp9/HT.txt", "r") as Rr:
    print(Rr.read())
print()
print()
with open("E:/Git/python_SelfTaughtBook/Chp9/HT2.txt", "r") as Sr:
    print(Sr.read())
Sr.close    
Rr.close

print()
print()
# Write a program that asks a user a question and saves the answer to a file.

print("#2")
print("----------------")
print()

Q1 = input("Enter a word: ")
FO = open("E:/Git/python_SelfTaughtBook/Chp9/Writeit.txt", "w")
FO.write(Q1)
FO.close
print("I wrote it")



print()
print()
# Take the items in this list of lists:
# [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# and write them to a csv file. The data from each list should be a row in the file, with each item in the list seperated by a comma.

print("#3")
print("----------------")
print()

import csv
ListToWrite = [["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

F1 = open("E:/Git/python_SelfTaughtBook/Chp9/Mylist.csv", "w")
wr = csv.writer(F1, delimiter=",")
for movie_list in ListToWrite:
    wr.writerow(movie_list)
F1.close

print("----------------")
print()
F2 = open("E:/Git/python_SelfTaughtBook/Chp9/Mylist.csv", "r")
r = csv.reader(F2, delimiter=",")
for row in r:
    print(",".join(row))
    
F2.close
