# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Find Missing Observations.py
@time: 2021/10/04
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = mean * (n + m) - sum(rolls)
        # print(s / n)
        if s > 6 * n or s < 1 * n: return []
        if s % n == 0:
            return [s // n] * n
        a, b = divmod(s, n)
        ret = [s // n] * n
        p = 0
        while b > 0:
            tmp = min(b, 6 - ret[p])
            b -= tmp
            ret[p] += tmp
            p += 1
        # print(sum(ret) + sum(rolls), mean * (m + n))
        return ret


so = Solution()
print(so.missingRolls([4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5]
                      , 4
                      , 40))
