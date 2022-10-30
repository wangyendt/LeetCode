#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Most Frequent Even Element.py 
@time: 2022/09/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mn = -1
        mv = -1
        nums.sort()
        for k, v in collections.Counter(nums).items():
            if k % 2 == 0 and v > mv:
                mv = v
                mn = k
        return mn


so = Solution()
print(so.mostFrequentEven([8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))
