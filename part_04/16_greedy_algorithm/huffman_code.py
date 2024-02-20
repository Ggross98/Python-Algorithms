# -*- coding: utf-8 -*-
"""
@Time: 2024/2/20 16:37
@Author: GU Linghao
@File: huffman_code.py
@Description: 霍夫曼编码
"""

from queue import PriorityQueue


class Node():
    def __init__(self, freq, ch):
        self.freq = freq
        self.ch = ch

        self.left = None
        self.right = None

class HuffmanTree():
    def __init__(self):
        pass

    def build(self, table):
        nodes = {}

        q = PriorityQueue()
        for tmp in table:
            q.put(tmp)
            nodes[tmp] = Node(freq=tmp[0], ch=tmp[1])

        for i in range(len(table)-1):
            x = q.get()
            y = q.get()

            tmp = (x[0] +y[0], None)
            q.put(tmp)

            node = Node(freq=x[0]+y[0], ch=None)
            node.left = nodes[x]
            node.right = nodes[y]
            nodes[tmp] = node

        return nodes[q.get()]

class HuffmanCoder():

    encoder = {}

    def __init__(self, root):
        self.root = root

        def search(node, code):
            if node is None:
                return
            if node.ch is not None:
                self.encoder[node.ch] = code
                print("{0}: {1}".format(node.ch, code))
            else:
                search(node.left, code+"0")
                search(node.right, code+"1")

        search(self.root, "")

    def encode(self, s):
        ans = ""
        for ch in s:
            ans += self.encoder[ch]

        return ans

    def decode(self, s):
        ans = ""
        idx = 0
        while idx < len(s):
            node = self.root

            while node.ch is None:
                ch = s[idx]
                if ch == '0':
                    node = node.left
                else:
                    node = node.right

                if node.ch is None:
                    idx += 1

            ans += node.ch
            idx += 1

        return ans




table = [(5, 'f'), (13, 'd'), (16, 'b'), (34, 'a'), (9, 'e'), (12, 'c')]
root = HuffmanTree().build(table)
coder = HuffmanCoder(root)
s = "aabe"
code = coder.encode(s)
print(code)

print(coder.decode(code))
