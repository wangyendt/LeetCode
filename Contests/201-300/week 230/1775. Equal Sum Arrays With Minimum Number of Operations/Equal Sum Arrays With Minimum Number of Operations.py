#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Equal Sum Arrays With Minimum Number of Operations.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 < s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
        # nums1.sort()
        # nums2.sort()
        target = s1 - s2
        print(nums1, nums2)
        res = []
        ret = 0
        for n1 in nums1:
            res.append(n1 - 1)
        for n2 in nums2:
            res.append(6 - n2)
        res.sort(reverse=True)
        s = 0
        for r in res:
            if s >= target:
                break
            s += r
            ret += 1
        if s < target: return -1
        return ret
        # for n1 in nums1[::-1]:
        #     res1 += 1
        #     target1 -= (n1 - 1)
        #     if target1 <= 0:
        #         break
        # for n2 in nums2:
        #     res2 += 1
        #     target2 -= (6 - n2)
        #     if target2 <= 0:
        #         break
        # if target1 <= 0:
        #     if target2 <= 0:
        #         return min(res1, res2)
        #     else:
        #         return res1
        # else:
        #     if target2 <= 0:
        #         return res2
        #     else:
        #         return -1


so = Solution()
# print(so.minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]))
print(so.minOperations(nums1=[6, 6], nums2=[1]))
