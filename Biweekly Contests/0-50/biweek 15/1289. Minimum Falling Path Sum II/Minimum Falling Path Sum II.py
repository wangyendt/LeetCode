#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Falling Path Sum II
@time: 2019/12/16 16:43
"""

import sys


class Solution:
    def minFallingPathSum(self, arr: list(list())) -> int:
        n = len(arr)
        dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        min_last_row = [sys.maxsize for _ in range(n)]
        for j in range(n):
            dp[0][j] = arr[0][j]

        for i in range(1, n):
            for j in range(n):
                min_last_row[j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:])
            for j in range(n):
                dp[i][j] = min_last_row[j] + arr[i][j]
                # print(f'i={i},j={j},arr[{i}][{j}]={arr[i][j]},'
                #       f'{dp[i-1][:j]+dp[i-1][j+1:]},last row:{min_last_row},'
                #       f'dp:{dp}')
        return min(dp[-1])


so = Solution()
print(so.minFallingPathSum(arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
