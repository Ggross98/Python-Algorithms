# -*- coding: utf-8 -*-
"""
@Time: 2024/2/20 15:32
@Author: GU Linghao
@File: activity_select.py
@Description: 活动选择问题。假定n个活动，分别具有开始时间s及结束时间f。活动使用同一资源，该资源在某个时刻只能供一个活动使用。
若两个活动时间不重合，则称二者兼容。求最大兼容活动集。
"""

class Activity():

    def __init__(self, idx, s, f):
        self.idx = idx
        self.s = s
        self.f = f


class GreedySelector():
    def __init__(self):
        pass

    def select(self, data):
        i = 0
        f_last = 0
        ans = []
        while i < len(data):
            if data[i].s >= f_last:
                ans.append(data[i])
                f_last = data[i].f
            i += 1

        return ans


data = [Activity(1, 1, 4), Activity(2, 3, 5),
        Activity(3, 0, 6), Activity(4, 5, 7),
        Activity(5, 3, 9), Activity(6, 5, 9),
        Activity(7, 6, 10), Activity(8, 8, 11),
        Activity(9, 8, 12), Activity(10, 2, 16),
        Activity(11, 12, 14)]
# 活动数组应当已按照结束时间排序

selector = GreedySelector()
ans = selector.select(data=data)
for a in ans:
    print("{0}: {1}-{2}".format(a.idx, a.s, a.f))
