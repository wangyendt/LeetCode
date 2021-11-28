#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Removing Minimum and Maximum From Array.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        m, M = 1e7, -1e7
        im, iM = -1, -1
        for i, n in enumerate(nums):
            if n < m:
                im = i
                m = n
            if n > M:
                iM = i
                M = n
        lens = (im + 1, len(nums) - im, iM + 1, len(nums) - iM)
        res = min(range(4), key=lambda x: lens[x])
        ret = lens[res]
        # print(im,iM,m,M,ret)
        if res == 0:
            target = [iM - im - 1, len(nums) - iM]
        elif res == 1:
            target = [iM, im - iM]
        elif res == 2:
            target = [im - iM - 1, len(nums) - im]
        elif res == 3:
            target = [im, iM - im]
        # print(res,ret, target)
        ret += min(target[0] + 1, target[1])
        return ret


so = Solution()
print(so.minimumDeletions(nums=[2, 10, 7, 5, 4, 1, 8, 6]))
# print(so.minimumDeletions(nums=[0, -4, 19, 1, 8, -2, -3, 5]))
