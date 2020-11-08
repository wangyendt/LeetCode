#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sort Array by Increasing Frequency.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnter = collections.Counter(nums)
        ret = sorted(nums, key=lambda x: (cnter[x], -x))
        return ret


so = Solution()
print(so.frequencySort([3, 1, 2, 1, 1, 2]))
