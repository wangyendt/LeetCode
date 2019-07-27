#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Largest Unique Number.py 
@time: 2019/07/27
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def largestUniqueNumber(self, A: list) -> int:
        return max([c[0] for c in collections.Counter(A).items() if c[1] == 1] or [-1])


so = Solution()
print(so.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
print(so.largestUniqueNumber([5, 5, 3, 9, 3, 9, 8, 3, 8]))
print(so.largestUniqueNumber([]))
print(so.largestUniqueNumber([1]))
