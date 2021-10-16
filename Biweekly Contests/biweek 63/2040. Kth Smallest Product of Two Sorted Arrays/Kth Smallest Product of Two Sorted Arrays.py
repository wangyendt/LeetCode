#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Kth Smallest Product of Two Sorted Arrays.py 
@time: 2021/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        neg1, pos1 = [], []
        for x in nums1:
            if x < 0:
                neg1.append(x)
            else:
                pos1.append(x)
        neg2, pos2 = [], []
        for x in nums2:
            if x < 0:
                neg2.append(x)
            else:
                pos2.append(x)
        neg = len(neg1) * (len(nums2) - len(neg2)) + (len(nums1) - len(neg1)) * len(neg2)

        if k <= neg:
            lo, hi = -10 ** 10, 0
        else:
            k -= neg
            lo, hi = 0, 10 ** 10
        while lo < hi:
            mid = lo + hi >> 1
            cnt = 0
            if mid < 0:
                for x in neg1: cnt += len(pos2) - bisect.bisect_left(pos2, -((-mid) // x))
                for x in neg2: cnt += len(pos1) - bisect.bisect_left(pos1, -((-mid) // x))
            else:
                for x in neg1: cnt += len(neg2) - bisect.bisect_left(neg2, -(mid // -x))
                for x in pos1:
                    if x == 0:
                        cnt += len(pos2)
                    else:
                        cnt += bisect.bisect_right(pos2, mid // x)
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


so = Solution()
print(so.kthSmallestProduct(nums1=[2, 5], nums2=[3, 4], k=2))
print(so.kthSmallestProduct(nums1=[-4, -2, 0, 3], nums2=[2, 4], k=6))
