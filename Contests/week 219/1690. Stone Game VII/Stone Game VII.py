#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Stone Game VII
@time: 2020/12/13 10:37
"""

from typing import *
import functools
import sys

sys.setrecursionlimit(10000000)


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = [0]
        for stone in stones:
            pre.append(pre[-1] + stone)
        # print(sum(stones[3:5]), pre[5] - pre[3])
        # print(stones, pre)

        @functools.lru_cache(10000)
        def dp(i, j):
            l = j + 1 - i
            if l == 2:
                if n % 2 == 0:
                    ret = max(stones[i], stones[j])
                else:
                    ret = -max(stones[i], stones[j])
            else:
                if l % 2 == n % 2:
                    ret = max(
                        dp(i, j - 1) + pre[j] - pre[i],
                        dp(i + 1, j) + pre[j + 1] - pre[i + 1]
                    )
                else:
                    ret = min(
                        dp(i, j - 1) - pre[j] + pre[i],
                        dp(i + 1, j) - pre[j + 1] + pre[i + 1]
                    )
            # print(i, j, ret)
            return ret

        return dp(0, n - 1)


so = Solution()
print(so.stoneGameVII(stones=[5, 3, 1, 4, 2]))
print(so.stoneGameVII(stones=[7, 90, 5, 1, 100, 10, 10, 2]))
print(so.stoneGameVII(stones=list(range(1000))))
