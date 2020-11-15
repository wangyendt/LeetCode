#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Reduce X to Zero.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        mp = {0: 0}
        prefix = 0
        for i, num in enumerate(nums, 1):
            prefix += num
            mp[prefix] = i
        inf = float('inf')
        ans = mp.get(x, inf)
        for i, num in enumerate(reversed(nums), 1):
            x -= num
            if x in mp and mp[x] + i <= len(nums): ans = min(ans, i + mp[x])
        return ans if ans < inf else -1


so = Solution()
print(so.minOperations([1, 1, 4, 2, 3], 5))
