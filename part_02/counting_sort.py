# _*_ coding: utf-8 _*_
# @Time : 2022/9/15 16:05 
# @Author : Ggross
# @Version : V 0.1
# @File : counting_sort.py
# @Description : 计数排序

class CountingSort():
    def __init__(self):
        pass

    def sort(self, nums, k):
        """
        计数排序：一种常数时间的非原位排序算法，要求输入的所有数为不大于k的整数，即[0,k]
        :param nums: 待排序数组
        :param k: 数组中最大值（包含）
        :return: 排序后的新数组
        """
        temp = [0] * (k + 1)
        size = len(nums)
        ans = [-1] * size

        # 统计各个数出现次数
        for i in range(size):
            temp[nums[i]] += 1

        # 将次数转变为：小于等于该数的元素出现次数
        for j in range(1, k + 1):
            temp[j] += temp[j - 1]

        # 从后向前遍历，保持其稳定性
        # 即大小相同的元素，排序后的顺序与排序前相同
        for i in range(size - 1, -1, -1):
            ans[temp[nums[i]] - 1] = nums[i]
            temp[nums[i]] -= 1

        return ans


sorter = CountingSort()

input = [2, 5, 3, 0, 2, 3, 0, 3]
output = sorter.sort(input, 5)
print(output)
