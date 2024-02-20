# -*- coding: utf-8 -*-
"""
@Time: 2023/9/13 16:16
@Author: GU Linghao
@File: rod_cutting.py
@Description: 钢条切割问题：给定一段长度为n的钢条和一个价格表pi(i = 1, 2, ..., n)，求切割钢条方案，使销售额最大
"""

test_n = 7
test_p = {0: 0, 1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}


def bottom_up(n, p):
    '''
    自底向上，将问题分为更小的子问题
    :param n:
    :param p:
    :return:
    '''
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        ri = p[i]
        for j in range(1, i):
            ri = max(ri, r[j] + p[i - j])
        r[i] = ri

    return r[n]

def extended_bottom_up(n, p):
    '''
    在自底向上方法基础上进行扩展，可同时输出切割方案
    :param n:
    :param p:
    :return:
    '''
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        ri = p[i]
        si = i
        for j in range(1, i):
            if ri < r[j] + p[i - j]:
                ri = r[j] + p[i - j]
                si = i - j
        r[i] = ri
        s[i] = si

    pos = n
    cut = []
    while pos > 0:
        cut.append(s[pos])
        pos -= s[pos]

    return r[n], cut

# print(bottom_up(test_n, test_p))
ans, cut = extended_bottom_up(test_n, test_p)
print(ans)
print(cut)