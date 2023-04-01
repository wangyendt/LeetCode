#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Pairs With XOR in a Range.py 
@time: 2021/03/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


import numpy as np


class Solution:
    def countPairs(self, nums: List[int], lo: int, hi: int) -> int:
        numBits = max(max(x.bit_length() for x in nums), lo.bit_length(), hi.bit_length())
        freq = np.bincount(nums, minlength=(1 << numBits))
        targets = np.arange(lo, hi + 1)
        return int(sum(freq[targets ^ x].sum() for x in nums) // 2)
