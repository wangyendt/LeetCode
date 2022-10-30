#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Array Pairs Divisible by K.py 
@time: 2022/02/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import math


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        divs = []
        for kk in range(1, k + 1):
            if k % kk == 0:
                divs.append(kk)
        ret = 0
        cnter = collections.Counter()
        for i in range(len(nums)):
            rem = k // (math.gcd(nums[i], k))
            ret += cnter[rem]
            for div in divs:
                if nums[i] % div == 0:
                    cnter[div] += 1
        return ret

    def coutPairs2(self, nums: List[int], k: int) -> int:
        cnter = collections.Counter(math.gcd(num, k) for num in nums)
        # print(cnter)
        ret = 0
        for cnt1 in cnter:
            for cnt2 in cnter:
                if cnt1 < cnt2:
                    if cnt1 * cnt2 % k == 0:
                        ret += cnter[cnt1] * cnter[cnt2]
                elif cnt1 == cnt2:
                    if cnt1 * cnt2 % k == 0:
                        ret += (cnter[cnt1] - 1) * cnter[cnt1] // 2
        return ret


so = Solution()
print(so.coutPairs([1, 2, 3, 4, 5], 3))
print(so.coutPairs([1, 2, 3, 3, 3, 4, 5], 3))
print(so.coutPairs([3, 5, 6, 7, 9], 3))
