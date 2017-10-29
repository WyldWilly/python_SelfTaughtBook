#!/usr/bin/env python3


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
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.size())
item = stack.pop()
print(item)
print(stack.is_empty())

stack2 = Stack()
for i in range(0,6):
    stack2.push(i)

print(stack2.peek())
print(stack2.size())

