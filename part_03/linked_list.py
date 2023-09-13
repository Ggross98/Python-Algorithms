# -*- coding: utf-8 -*-
"""
@Time: 2023/9/12 17:00
@Author: GU Linghao
@File: linked_list.py
@Description: 实现双向链表
"""


class LinkedNode():

    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.prev = pre
        self.next = next


class LinkedList():

    def __init__(self, head=None):
        self.head = head

    def search(self, target_val):
        node = self.head
        while node:
            if node.val == target_val:
                return node
            node = node.next
        return None

    def insert(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        node.prev = None

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev


node0, node1, node2, node3 = LinkedNode(val=0), LinkedNode(val=1), LinkedNode(val=2), LinkedNode(val=3)

linked_list = LinkedList(head=node0)
linked_list.insert(node1)
print(linked_list.head.val)
print(linked_list.search(0).val)
linked_list.insert(node2)
linked_list.insert(node3)
node_to_delete = linked_list.search(target_val=2)
linked_list.delete(node_to_delete)
print(linked_list.head.val)
print(linked_list.head.next.val)
