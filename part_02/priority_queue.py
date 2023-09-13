# _*_ coding: utf-8 _*_
# @Time : 2022/9/6 14:52 
# @Author : Ggross
# @Version：V 0.1
# @File : priority_queue.py
# @Description : 使用最大堆实现最大优先队列

class Heap():
    def __init__(self, nums=None):
        if nums is None:
            nums = []
        self.nums = nums
        self.size = len(nums)

        for i in range(len(self.nums) // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        """
        维护最大堆的性质：假定i的左右子树为最大堆，但nums[i]可能小于其左右节点
        让nums[i]逐级下降
        :param i: 元素所在位置
        :return:
        """
        left, right = 2 * i, 2 * i + 1
        if left < self.size and self.nums[left] > self.nums[i]:
            self.nums[i], self.nums[left] = self.nums[left], self.nums[i]
            self.max_heapify(left)
        if right < self.size and self.nums[right] > self.nums[i]:
            self.nums[i], self.nums[right] = self.nums[right], self.nums[i]
            self.max_heapify(right)


class PriorityQueue():
    def __init__(self):
        self.heap = Heap()

    def max(self):
        return self.heap.nums[0]

    def extract_max(self):
        if self.heap.size < 1:
            print("Heap underflow!")
            return None
        else:
            m = self.heap.nums[0]
            if self.heap.size == 1:
                self.heap.size = 0
                self.heap.nums = []
            else:
                self.heap.size -= 1
                self.heap.nums[0] = self.heap.nums[self.heap.size]
                self.heap.nums.pop(-1)
                self.heap.max_heapify(0)
            return m

    def increase(self, i, n):
        """
        将索引位置的值提升
        :param i: 索引
        :param n: 键值
        :return:
        """
        if i >= self.heap.size:
            print("Heap index error!")
        elif self.heap.nums[i] >= n:
            print("New key is smaller than current key!")
        else:
            self.heap.nums[i] = n
            while i > 0:
                parent_index = i // 2
                if self.heap.nums[parent_index] < self.heap.nums[i]:
                    self.heap.nums[parent_index], self.heap.nums[i] = self.heap.nums[i], self.heap.nums[parent_index]
                    i = parent_index
                else:
                    break

    def insert(self, n):
        self.heap.nums.append(-1)
        self.heap.size += 1
        self.increase(self.heap.size - 1, n)


pq = PriorityQueue()
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)
pq.insert(5)
print(pq.max())
print(pq.extract_max())
print(pq.extract_max())
pq.increase(2, 999)
print(pq.max())
