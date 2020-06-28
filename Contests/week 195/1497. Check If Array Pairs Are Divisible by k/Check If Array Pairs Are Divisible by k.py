#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Check If Array Pairs Are Divisible by k
@time: 2020/06/28 11:09
"""

import collections


class Solution:
    def canArrange(self, arr: list, k: int) -> bool:
        remains = collections.defaultdict(int)
        for a in arr:
            remains[a % k] += 1
        print(remains)
        for i in range(1, k // 2 + 1):
            if remains[i] != remains[k - i]:
                return False
        if remains[0] % 2 != 0:
            return False
        return True


so = Solution()
print(so.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
