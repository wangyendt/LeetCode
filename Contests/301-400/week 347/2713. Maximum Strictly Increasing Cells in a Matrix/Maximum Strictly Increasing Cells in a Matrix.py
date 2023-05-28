"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Maximum Strictly Increasing Cells in a Matrix.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])  # 获取矩阵的行数和列数

        # 哈希表A，键是元素的值，值是元素的坐标
        A = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                A[mat[i][j]].append([i, j])

        # 初始化动态规划数组dp和结果数组res
        dp = [[0] * n for i in range(m)]
        res = [0] * (n + m)

        # 按照元素的值从小到大进行排序
        for a in sorted(A):
            # 对于每个元素，根据它的行和列的最大值更新它可以访问的最大单元格数量
            for i, j in A[a]:
                dp[i][j] = max(res[i], res[~j]) + 1
            # 更新结果数组，为下一轮的计算做准备
            for i, j in A[a]:
                res[~j] = max(res[~j], dp[i][j])
                res[i] = max(res[i], dp[i][j])

        # 返回最大的单元格访问数量
        return max(res)
