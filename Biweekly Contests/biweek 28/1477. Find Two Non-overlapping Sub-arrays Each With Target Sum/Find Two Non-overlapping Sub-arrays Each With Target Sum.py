#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Two Non-overlapping Sub-arrays Each With Target Sum
@time: 2020/06/13 22:39
"""

import collections
import bisect
import itertools
import sys


class Solution:
    def minSumOfLengths(self, arr: list, target: int) -> int:
        n = len(arr)
        inf = sys.maxsize
        cumsum = [0] + list(itertools.accumulate(arr))
        D = collections.defaultdict(list)
        for i in range(1, n + 1):
            D[cumsum[i]].append(i)
        res = []
        for i in range(n):
            if cumsum[i] + target in D:
                ind = bisect.bisect_left(D[cumsum[i] + target], i)
                res.append(D[cumsum[i] + target][ind] - i)
            else:
                res.append(inf)
        dp = [inf] * n
        dp[-1] = res[-1]
        for i in range(n - 1)[::-1]:
            if dp[i + 1] == inf:
                dp[i] = res[i]
            else:
                if res[i] == inf:
                    dp[i] = dp[i + 1]
                else:
                    dp[i] = min(dp[i + 1], res[i])
        ret = inf
        for i in range(n):
            if res[i] == inf or i + res[i] >= len(dp): continue
            ret = min(ret, res[i] + dp[i + res[i]])
        if ret == inf: ret = -1
        return ret


so = Solution()
print(so.minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3))
print(so.minSumOfLengths(arr=[7, 3, 4, 7], target=7))
print(so.minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6))
print(so.minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3))
print(so.minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3))
print(so.minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1, 3], target=3))
