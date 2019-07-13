#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Divide Array Into Increasing Sequences.py 
@time: 2019/07/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

from collections import Counter


class Solution:
    def canDivideIntoSubsequences(self, nums: list, K: int) -> bool:
        if len(set(nums)) < K:
            return False
        cnt = Counter(nums)
        if cnt.most_common(1)[0][1] * K > len(nums):
            return False
        return True


so = Solution()
print(so.canDivideIntoSubsequences(nums=[1, 2, 2, 3, 3, 4, 4], K=3))
