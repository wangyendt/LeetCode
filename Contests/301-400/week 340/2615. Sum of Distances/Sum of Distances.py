#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Distances.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import collections


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def helper(nums):
            res = collections.defaultdict(list)
            for i, num in enumerate(nums):
                res[num].append(i)
            ret = []
            last = collections.defaultdict(int)
            how_much = collections.defaultdict(int)
            for i, num in enumerate(nums):
                if num in last:
                    ret.append(ret[last[num]] + (i - last[num]) * how_much[num])
                else:
                    ret.append(0)
                last[num] = i
                how_much[num] += 1
            return ret

        ret1 = helper(nums)
        ret2 = helper(nums[::-1])[::-1]
        # print(ret1, ret2)
        return [r1 + r2 for r1, r2 in zip(ret1, ret2)]
