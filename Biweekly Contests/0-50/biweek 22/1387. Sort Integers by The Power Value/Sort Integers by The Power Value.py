#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/23 0:08
@Author:  wang121ye
@File: Sort Integers by The Power Value.py
@Software: PyCharm
"""

import collections


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = collections.defaultdict(int)
        for num in range(lo, hi + 1):
            if dp[num] == 0:
                m = num
                cnt = 0
                while m != 1:
                    if m % 2 == 0:
                        m //= 2
                    else:
                        m = 3 * m + 1
                    cnt += 1
                    if dp[m] != 0:
                        cnt += dp[m]
                        break
                dp[num] = cnt
        res = [(n, dp[n]) for n in range(lo, hi + 1)]
        # print(res)
        res = [r[0] for r in sorted(res, key=lambda x: (x[1], x[0]))]
        return res[k - 1]


so = Solution()
print(so.getKth(lo=12, hi=15, k=2))
print(so.getKth(lo=1, hi=1, k=1))
print(so.getKth(lo=7, hi=11, k=4))
print(so.getKth(lo=10, hi=20, k=5))
print(so.getKth(lo=1, hi=1000, k=777))
