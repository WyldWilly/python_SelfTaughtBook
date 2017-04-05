#!/usr/bin/env python3

print()
print()
# Print each item in the following list:
# ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

print("#1")
print("----------------")
print()
movies = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for movie in movies:
    print(movie)


print()
print()
# Print all the numbers from 25 to 50

print("#2")
print("----------------")
print()
for i in range(25, 51):
    print(i)




print()
print()
# Print each item in the list from the first challenge and their indexes

print("#3")
print("----------------")
print()
movies = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, movie in enumerate(movies):
    print(index, " ", movie)



print()
print()
# Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers. Each time through the loop ask the user to guess a number on the list and
# tell them whether or not they guessed correctly.

print("#4")
print("----------------")
print()

numbers = [11,32,33,15,1]

while True:
    answer = input("Guess a number or type q to quit: ")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit: ")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly")



print()
print()
# Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in
# in the list [9, 1, 33, 83], and append each result to a third list.

print("#5")
print("----------------")
print()

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
products = []
for i in list1:
    for j in list2:
        products.append(i * j)
print(products)
