# -*- coding: utf-8 -*-
"""
@Time: 2023/9/13 16:41
@Author: GU Linghao
@File: longest_common_subsequence.py
@Description:   子序列的定义：一个字符串去掉任意字符后得到的结果；
                给定两个字符串X, Y，若字符串Z同时是X、Y的子序列，则称其为X与Y的公共子序列；
                现给定两个字符串，求它们的最长子序列
"""

test_text1 = "abcde"
test_text2 = "ace"

def len_lcs(text1, text2):
    m, n = len(text1), len(text2)
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a, b = text1[i - 1], text2[j - 1]
            if a == b:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    return c[m][n]

def print_lcs(text1, text2):
    '''
    在求出LCS长度基础上，返回其中一个LCS字符串
    :param text1:
    :param text2:
    :return:
    '''

    m, n = len(text1), len(text2)
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a, b = text1[i - 1], text2[j - 1]
            if a == b:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    ans = []
    i, j = m, n
    while i > 0 and j > 0:
        if c[i][j] == c[i-1][j-1] + 1 and c[i][j] > c[i-1][j] and c[i][j] > c[i][j-1]:
            ans.append(text1[i-1])
            i, j = i - 1, j - 1
        elif c[i-1][j] > c[i][j-1]:
            i -= 1
        else:
            j -= 1

    ans.reverse()
    return str(ans)

print(len_lcs(test_text1, test_text2))
print(print_lcs(test_text1, test_text2))