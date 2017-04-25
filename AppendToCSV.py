#!/usr/bin/env python3

#Append to the CSV
import csv

ListToWrite = [["Alien", "Aliens"],
    ["Predator", "Predator 2", "Aliens vs Predator", "Alien vs Predator Requiem", "Predators"]]

F1 = open("E:/Git/python_SelfTaughtBook/Chp9/Mylist.csv", "a")
wr = csv.writer(F1, delimiter=",")
for movie_list in ListToWrite:
    wr.writerow(movie_list)
F1.close

