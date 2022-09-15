# _*_ coding: utf-8 _*_
# @Time : 2022/9/1 15:44 
# @Author : Ggross
# @Version：V 0.1
# @File : merge_sort.py
# @Description : 归并排序


class MergeSort:

    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            mid = len(nums)//2
            return self.merge(self.sort(nums[:mid]), self.sort(nums[mid:]))

    def merge(self, a, b):
        m,n = len(a), len(b)
        ans = []
        i=j=0
        while i<m or j<n:
            if i==m:
                ans.append(b[j])
                j+=1
            elif j==n:
                ans.append(a[i])
                i+=1
            else:
                if a[i]<b[j]:
                    ans.append(a[i])
                    i += 1
                else:
                    ans.append(b[j])
                    j += 1
        return ans


sorter = MergeSort()

input = [3,2,5,1,8,4,9,6,7]
output = sorter.sort(input)
print(output)