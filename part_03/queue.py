# -*- coding: utf-8 -*-
"""
@Time: 2023/9/12 16:55
@Author: GU Linghao
@File: queue.py
@Description: 用数组实现队列
"""


class Queue():

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, n):
        self.data.append(n)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            tmp = self.data[0]
            del self.data[0]
            return tmp


queue = Queue()

queue.enqueue(4)
queue.enqueue(8)
print(queue.dequeue())
queue.enqueue(1)
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
