#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find All Lonely Numbers in the Array.py 
@time: 2022/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


from typing import *
import collections


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ret = []
        cnter = collections.Counter(nums)
        for n in nums:
            if cnter[n] == 1 and n - 1 not in cnter and n + 1 not in cnter:
                ret.append(n)
        return ret
