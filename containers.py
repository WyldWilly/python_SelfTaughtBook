#!/usr/bin/env python3

#containers

lists = []
rap = ["Kanye West","Jay Z","Eminem","Nas"]
rock = ["Bob Dylan","The Beatles","Led Zeppelin"]
djs = ["Zeds Dead","Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

print()
print()
rap = lists[0]
print(rap)

print()
print()
rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print()
print()
print(lists)