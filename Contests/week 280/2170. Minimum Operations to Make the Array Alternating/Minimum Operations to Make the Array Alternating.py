#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Make the Array Alternating.py 
@time: 2022/02/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_even = [n for i, n in enumerate(nums) if i % 2 == 0]
        nums_odd = [n for i, n in enumerate(nums) if i % 2 == 1]
        cnter_even = collections.Counter(nums_even)
        cnter_odd = collections.Counter(nums_odd)
        if len(nums) == 1: return 0
        if len(nums_even) == 1:
            if len(nums_odd) == 1:
                if nums_even[0] == nums_odd[0]: return 1
                return 0
        ret = 1e10
        l1, l2 = len(nums_even), len(nums_odd)
        mc_even, mc_odd = cnter_even.most_common(2), cnter_odd.most_common(2)
        if len(mc_even) == 1:
            if len(mc_odd) == 1:
                if mc_even[0][0] == mc_odd[0][0]:
                    ret = min(ret, mc_even[0][1], mc_odd[0][1])
                else:
                    ret = 0
            else:
                if mc_even[0][0] == mc_odd[0][0]:
                    ret = min(ret, l2 - mc_odd[1][1])
                else:
                    ret = min(ret, l2 - mc_odd[0][1])
        else:
            if len(mc_odd) == 1:
                if mc_even[0][0] == mc_odd[0][0]:
                    ret = min(ret, l1 - mc_even[1][1])
                else:
                    ret = min(ret, l1 - mc_even[0][1])
            else:
                for n1, cn1 in mc_even:
                    for n2, cn2 in mc_odd:
                        if n1 != n2:
                            ret = min(ret, l1 - cn1 + l2 - cn2)
        return ret


so = Solution()
print(so.minimumOperations(nums=[3, 1, 3, 2, 4, 3]))
print(so.minimumOperations([2, 2, 2, 2]))
