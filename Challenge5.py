#!/usr/bin/env python3

# Create a list of your favorite musicians
print("#1")
print("----------------")
print()
My_Favorite_Actors = ["Geno Reno","Harrison Ford","Tom Hanks","Gary Oldman","Robert Downey Jr","Chris Evans","Chris Pratt"]
print(My_Favorite_Actors)
print()
print()

# Create a list tuples, with each tuple containing
# the longitude and latitude of somewhere you lived or visited
print("#2")
print("----------------")
print()
My_Tuple0 = ("Kansas City", 40.0, 75.2)
My_Tuple1 = ("Pittsburgh", 60.4, 55.2)
My_Tuple2 = ("Orlando", 10.0, 25.2)
print()
print(My_Tuple0[0])
print(My_Tuple1[0])
print(My_Tuple2[0])
print(My_Tuple0)
print()
print()

# Create a dictionary that contains different attributes about
# you: Height, Weight, favorite color, favorite author, etc.
print("#3")
print("----------------")
print()

My_Dict = {"Height":"5ft 11in",
           "Weight":"325lbs",
           "Eyecolor":"Brown",
           "Favorite Color":"Blue",
           "Favorite Author":"Tom Clancy",
           }
print(My_Dict)
print()
print(My_Dict["Height"])
print(My_Dict["Weight"])
print(My_Dict["Eyecolor"])
print(My_Dict["Favorite Color"])
print(My_Dict["Favorite Author"])

print()
print()

# Write a program that lets the user ask your height, favorite color,
# or favorite author and returns the result from the dictionary in challenge 3.
print("#4")
print("----------------")
print()
q = input("Ask your question: ")
q = str(q)
if q in My_Dict:
    print(My_Dict[q])
else:
    print("Not there")


# Create a dictionary mapping your favorite actors to a list of your favorite
# movies by them.
print("#5")
print("----------------")
print()

Mov_Act = {
    "Star Wars":"Harrison Ford",
    "Sum of all Fears":"Harrison Ford",
    "Star Wars":"Mark Hammil",
    "Marvels Avengers":"Robert Downey Jr",
    "Thor":"Chris Hemsworth",
    "Dr Strange":"Benedict Cumberbatch"
}
print(Mov_Act)




# Lists, tuples, and dictionaries are just a few of the containers built
# into Python. Research Python Sets (a type of container). When would you use a set?
print("#6")
print("----------------")
print()