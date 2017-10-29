#!/usr/bin/env python3

# Print every character in the sting "Camus"
print("#1")
print("----------------")
print()
print()

a = "Camus"
for index in range(len(a)):
    print(a[index])

print()
print()
# Write a program that collects two strings from a user
# inserts them into the string "Yesterday I wrote a [response_one].
# I sent it to [response_two]!" and prints a new string.
print("#2")
print("----------------")
print()

response_one = input("Enter a word: ")
response_two = input("Enter another word: ")

w = "Yesterday I wrote a {}. I sent it to {}!".format(response_one, response_two)
print(w)


print()
print()
# Use a method to make the string "aldous Huxley was born in 1894." gramatically
# correct by capitalizing the first letter in the sentence.
print("#3")
print("----------------")
print()

a = "aldous Huxley was born in 1894."
print(a.capitalize())

print()
print()


# Take the string "Where now? Who now? When now?" and call a method that returns
# a list that looks like:
# ["Where now?", "Who now?", "When now?"].
print("#4")
print("----------------")
print()
j = 'Where now? Who now? When now?'.split('?')
print(j)



print()
print()
# Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it
# into a grammatically correct string. There should be a space between each word,
# but no space between the word fence and the period that follows it.
# (Dont forget you learned a method that turns a list of strings into a single string.)
print("#5")
print("----------------")
print()

saying = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(saying)
print(one)

print()
print()
# Replace every instance of "s" in "A screaming comes across the sky." with a $
print("#6")
print("----------------")
print()

saying2 = "A screaming comes across the sky.".replace("s", "$")
print(saying2)

print()
print()
# Use a method to find the first index of the character "m" in the string "Hemingway"
print("#7")
print("----------------")
print()

a = "Hemingway"
print(a.index("m"))


print()
print()
# Find dialouge in your favorite book (containing quotes) and turn it into a string
print("#8")
print("----------------")
print()

a = "That's no moon!"
b = "Use the Force Luke!"
c = "Come to the Dark Side!"

d = a + " " + b + " " + c
print(d)

print()
print()
# Create the string "three three three" using concatenation, then again using multiplication.
print("#9")
print("----------------")
print()

print("three" * 3)
print()
a = "three"
b = " "
print(a + b + a + b +a)


print()
print()
# Slice the string "It was a bright cold day in April, and the clocks were striking thirteen."
# to only include the characters before the comma.
print("#10")
print("----------------")
print()

st = "It was a bright cold day in April, and the clocks were striking thirteen."
a = len(st)
dot = st.index(",")
print(st[0:dot])
