# _*_ coding: utf-8 _*_
# @Time : 2022/9/15 16:30 
# @Author : Ggross
# @Version：V 0.1
# @File : radix_sort.py

from collections import defaultdict

class RadixSort():
    def __init__(self):
        pass

    def sort(self, nums, d):
        """
        基数排序，从最低位向最高位依次排序，其排序方法应当是稳定的（此处使用计数排序，k=9）
        :param nums: 待排序数组
        :param d: 最高位数
        :return: 排序后的数组
        """

        # 保存位数信息
        w = 1
        # 保存当前计数排序结果
        temp = defaultdict(list)

        for i in range(d):
            for num in nums:
                temp[(num // w) % 10].append(num)

            nums = []
            for g in range(10):
                for t in temp[g]:
                    nums.append(t)
            temp.clear()
            w *= 10

        return nums


sorter = RadixSort()

input = [2,675,432,141,641,999,16]
output = sorter.sort(input, 3)
print(output)