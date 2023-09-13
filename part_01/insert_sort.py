# _*_ coding: utf-8 _*_
# @Time : 2022/9/1 16:05 
# @Author : Ggross
# @Version：V 0.1
# @File : insert_sort.py
# @Description : 插入排序

class InsertSort():
    def __init__(self):
        pass

    def sort(self, nums):
        if len(nums) < 2:
            return nums
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[j + 1:i + 1] = nums[j:i]
                    nums[j] = temp
        return nums


sorter = InsertSort()

input = [5, 1, 4, 2, 6, 7, 9, 8, 0]
output = sorter.sort(input)
print(output)
