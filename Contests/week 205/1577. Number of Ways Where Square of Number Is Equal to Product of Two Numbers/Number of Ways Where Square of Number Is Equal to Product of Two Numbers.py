#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Number of Ways Where Square of Number Is Equal to Product of Two Numbers.py 
@time: 2020/09/06
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def numTriplets(self, nums1: list, nums2: list) -> int:
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        ret = 0
        for n1 in nums1:
            for n2 in nums2:
                d, r = divmod(n1 ** 2, n2)
                if r == 0 and d in c2:
                    ret += c2[d]
                    if n1 == n2:
                        ret -= 1
                d, r = divmod(n2 ** 2, n1)
                if r == 0 and d in c1:
                    ret += c1[d]
                    if n1 == n2:
                        ret -= 1
        return ret // 2


so = Solution()
print(so.numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9]))
