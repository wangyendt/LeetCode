#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Finding Pairs With a Certain Sum.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1, self.nums2 = nums1, nums2
        self.cnter = collections.defaultdict(int)
        for n2 in nums2:
            self.cnter[n2] += 1

    def add(self, index: int, val: int) -> None:
        self.cnter[self.nums2[index]] -= 1
        self.cnter[self.nums2[index] + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ret = 0
        for n1 in self.nums1:
            ret += self.cnter[tot - n1]
        return ret

    # Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
