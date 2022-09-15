# _*_ coding: utf-8 _*_
# @Time : 2022/9/6 10:37 
# @Author : Ggross
# @Version：V 0.1
# @File : heap_sort.py
# @Description : 堆和堆排序


class Heap():
    def __init__(self, nums=[]):
        self.nums = nums
        self.size = len(nums)

        for i in range(len(self.nums)//2, -1,-1):
            self.max_heapify(i)

    def max_heapify(self, i):
        """
        维护最大堆的性质：假定i的左右子树为最大堆，但nums[i]可能小于其左右节点
        让nums[i]逐级下降
        :param i: 元素所在位置
        :return:
        """
        left, right = 2*i, 2*i+1
        if left <self.size and self.nums[left]>self.nums[i]:
            self.nums[i], self.nums[left] = self.nums[left],self.nums[i]
            self.max_heapify(left)
        if right<self.size and self.nums[right]>self.nums[i]:
            self.nums[i], self.nums[right] = self.nums[right],self.nums[i]
            self.max_heapify(right)

    def sort(self):
        for i in range(self.size-1, 0, -1):
            self.nums[i], self.nums[0] = self.nums[0], self.nums[i]
            self.size -= 1
            self.max_heapify(0)
        return self.nums


input = [3,2,5,3,9,1,7,0,8]
output = Heap(input).sort()
print(output)




