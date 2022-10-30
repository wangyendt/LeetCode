#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Arithmetic Triplets.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        ret = 0
        for n in nums:
            if n not in nums_set: continue
            cnt = 1
            nums_set.remove(n)
            while n + diff in nums_set:
                cnt += 1
                nums_set.remove(n + diff)
                n += diff
            ret += max(0, cnt - 2)
        return ret


so = Solution()
print(so.arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3))
