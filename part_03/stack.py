# -*- coding: utf-8 -*-
"""
@Time: 2023/9/12 16:46
@Author: GU Linghao
@File: stack.py
@Description: 用数组实现堆
"""

class Stack():
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, n):
        self.data.append(n)

    def pop(self):
        if self.is_empty():
            return None
        else:
            tmp = self.data[-1]
            del self.data[-1]
            return tmp

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

stack = Stack()

print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
print(stack.top())
stack.push(2)
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
