#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/11 1:19
@Author:  wang121ye
@File: Number of Ways of Cutting a Pizza.py
@Software: PyCharm
"""


class Solution:
    def ways(self, pizza: list, k: int) -> int:
        def hasApple(si: int, ei: int, sj: int, ej: int) -> int:
            if any(pizza[i][j] == 'A' for i in range(si, ei) for j in range(sj, ej)):
                return True

        def dfs(si: int, ei: int, sj: int, ej: int, k: int) -> int:
            if si >= ei or sj >= ej:  # invalid boundary
                return 0
            if k == 0:  # run out of cuts
                return 1
            if (si, ei, sj, ej, k) in memo:  # we've calculated before
                return memo[(si, ei, sj, ej, k)]

            ans = 0

            # cut horizontally
            for i in range(si + 1, ei):
                if hasApple(si, i, sj, ej) and hasApple(i, ei, sj, ej):
                    # dfs search the lower part
                    ans += dfs(i, ei, sj, ej, k - 1)

            # cut vertically
            for j in range(sj + 1, ej):
                if hasApple(si, ei, sj, j) and hasApple(si, ei, j, ej):
                    # dfs search the right part
                    ans += dfs(si, ei, j, ej, k - 1)

            memo[(si, ei, sj, ej, k)] = ans

            return ans

        memo = {}

        return dfs(0, len(pizza), 0, len(pizza[0]), k - 1) % int(1e9 + 7)
