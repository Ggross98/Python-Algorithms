# _*_ coding: utf-8 _*_
# @Time : 2022/9/15 17:18 
# @Author : Ggross
# @Version：V 0.1
# @File : bucket_sort.py
# @Description : 桶排序

class BucketSort():
    def __init__(self):
        pass

    def sort(self, nums, k):
        """
        假设数据服从均匀分布（本例子中的区间是[0,1]），以常数时间进行排序。划分出若干个区间，对每个区间的数进行插入排序，最后将其合并。
        桶的数量越多，空间复杂度越高，时间复杂度越低；反之则空间复杂度降低、时间复杂度升高
        计数排序、基数排序均可看作一种桶排序
        :param nums: 待排序数组
        :param k: 桶（区间）的数量
        :return: 排序的数组
        """

        bucket = [[] for _ in range(k)]
        for i in range(len(nums)):
            index = int(k * nums[i])
            j = 0
            while j < len(bucket[index]):
                if nums[i] > bucket[index][j]:
                    j += 1
                else:
                    break
            bucket[index].insert(j, nums[i])

        ans = []
        for b in bucket:
            for num in b:
                ans.append(num)

        return ans


sorter = BucketSort()

input = [0.03, 0.31, 0.98, 0.24, 0.24, 0.35, 0.86, 0.68]
output = sorter.sort(input, 10)
print(output)
