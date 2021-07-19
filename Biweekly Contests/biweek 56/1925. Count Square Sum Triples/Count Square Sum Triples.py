# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Count Square Sum Triples.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import math


class Solution:
    def countTriples(self, n: int) -> int:
        res = set()
        for i in range(1, n):
            for j in range(1, n):
                r = i ** 2 + j ** 2
                p = round(math.sqrt(r))
                # print(i, j, p)
                if r == p ** 2 <= n ** 2:
                    res.add((i, j, p))
        return len(res)


so = Solution()
print(so.countTriples(5))
