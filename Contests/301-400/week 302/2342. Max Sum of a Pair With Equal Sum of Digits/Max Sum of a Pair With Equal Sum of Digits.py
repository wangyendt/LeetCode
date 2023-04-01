#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Max Sum of a Pair With Equal Sum of Digits.py 
@time: 2022/07/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
import heapq
from typing import *


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = []
        for i, num in enumerate(nums):
            res.append(sum(int(n) for n in str(num)))
        cnt = collections.defaultdict(list)
        for i, r in enumerate(res):
            heapq.heappush(cnt[r], i)
        ret = -1
        for k, v in cnt.items():
            tmp = heapq.nlargest(2, v, key=lambda x: nums[x])
            if len(tmp) == 2:
                ret = max(ret, sum([nums[t] for t in tmp]))
        return ret


so = Solution()
print(so.maximumSum(nums=[18, 43, 36, 13, 7]))
