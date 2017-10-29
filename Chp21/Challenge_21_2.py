#!/usr/bin/env python3

# Use a stack to create a new list with the
# items in the following list: [1, 2, 3, 4, 5]

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.item) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

List1 = [1, 2, 3, 4, 5]
List2 = []

stack = Stack()
for item in List1:
    stack.push(item)

for i in range(len(stack.items)):
    List2.append(stack.pop())

print(List1)
print("---------------")
print(List2)
