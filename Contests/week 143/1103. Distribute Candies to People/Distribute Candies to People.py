#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Distribute Candies to People.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import math


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list:
        a1 = (1 + num_people) * num_people // 2
        d = num_people ** 2
        # (a1+a1+(m-1)*d)*m / 2 < candies
        # dm^2+(2a1-d)m-2candies < 0
        # m < (d-2a1 + sqrt((2a1-d)^2+8d*candies)) / (2d)
        nGroup = int((d - 2 * a1 + math.sqrt((2 * a1 - d) ** 2 + 8 * d * candies)) // (2 * d))
        ret = [0] * num_people
        for i in range(num_people):
            ret[i] = (i + 1 + i + 1 + (nGroup - 1) * num_people) * nGroup // 2
        rest = candies - sum(ret)
        p = 0
        while rest > 0:
            diff = min(rest, p + 1 + nGroup * num_people)
            ret[p] += diff
            rest -= diff
            p += 1
        return ret


so = Solution()
print(so.distributeCandies(10, 3), [5, 2, 3])
print(so.distributeCandies(7, 4), [1, 2, 3, 1])
print(so.distributeCandies(1000, 10), [105, 110, 115, 120, 90, 84, 88, 92, 96, 100])
