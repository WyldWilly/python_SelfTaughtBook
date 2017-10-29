#!/usr/bin/env python3

def palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(palindrome("Mother"))
print(palindrome("Mom"))
print(palindrome("sword"))
print(palindrome("God"))
