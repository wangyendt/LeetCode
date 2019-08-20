#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Dice Rolls With Target Sum
@time: 2019/8/16 18:10
"""

import collections


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        methods = collections.defaultdict(int)

        def helper(m, n, s):
            # print(m, n, s)
            if (m, n, s) in methods:
                ret = methods[(m, n, s)]
            else:
                if m == 1 and 0 < s <= n:
                    ret = 1
                elif s <= 0 or m * n < s:
                    ret = 0
                else:
                    ret = sum([helper(m - 1, n, s - i) for i in range(1, n + 1)])
            methods[(m, n, s)] = ret
            return ret

        return helper(d, f, target) % 1000000007


so = Solution()
# print(so.numRollsToTarget(1, 6, 3), 1)
# print(so.numRollsToTarget(2, 6, 7), 6)
# print(so.numRollsToTarget(2, 5, 10), 1)
# print(so.numRollsToTarget(1, 2, 3), 0)
print(so.numRollsToTarget(30, 30, 500), 222616187)
