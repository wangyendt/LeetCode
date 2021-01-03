#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Ways to Split Array Into Three Subarrays.py 
@time: 2021/01/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if min(nums) == max(nums):
            return ((n - 1) * (n - 2) // 2) % (10 ** 9 + 7)
        s = sum(nums)
        pre = [0]
        post = [0]
        for m in nums:
            pre.append(pre[-1] + m)
        for m in nums[::-1]:
            post.append(post[-1] + m)

        ret = 0
        mem_bl = dict()
        mem_br = dict()

        def br(j, x):
            if (j, x) not in mem_br:
                mem_br[(j, x)] = bisect.bisect_right(post, x, hi=min(j, start_last))
            return mem_br[(j, x)]

        def bl(j, x):
            if (j, x) not in mem_bl:
                mem_bl[(j, x)] = bisect.bisect_left(post, x, hi=min(j, end_last))
            return mem_bl[(j, x)]

        start_last = 2 * n
        end_last = 2 * n
        for i in range(1, n - 1):
            if pre[i] > s / 3:
                break
            rest = s - pre[i]
            start = br(n - i, rest - pre[i])
            end = bl(n - i, rest / 2)
            if start == 1:
                continue
            if start > end:
                ret += start - end
            start_last = start
            end_last = end
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.waysToSplit(nums=[1, 2, 2, 2, 5, 0]))
print(so.waysToSplit([0, 3, 3]))
a = list(range(100000))
print(so.waysToSplit(a))
