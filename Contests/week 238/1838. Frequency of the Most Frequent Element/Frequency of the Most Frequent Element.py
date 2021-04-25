#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Frequency of the Most Frequent Element.py 
@time: 2021/04/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def get_sum(i, j):
            return pres[j + 1] - pres[max(0, i)]

        pres = [0]
        nums.sort()
        ret = 1
        for n in nums:
            pres.append(pres[-1] + n)
        for i, n in enumerate(nums):
            if i > 0:
                res = nums[i] * ret - get_sum(i - ret + 1, i)
                if res < 0:
                    continue
                else:
                    ret2 = 0
                    for cnt in range(1, 1000000):
                        if i - ret + 1 - cnt < 0:
                            break
                        res = nums[i] * (ret + cnt) - get_sum(i - ret + 1 - cnt, i)
                        if res <= k:
                            ret2 = ret + cnt
                        else:
                            break
                    ret = max(ret, ret2)
        return ret


so = Solution()
print(so.maxFrequency([1, 2, 4], 5))
print(so.maxFrequency(nums=[1, 4, 8, 13], k=5))
