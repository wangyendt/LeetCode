# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Make Sum Divisible by P.py
@time: 2020/09/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections
import bisect


class Solution:
    def minSubarray(self, A: List[int], p: int) -> int:
        def helper(nums: List[int]) -> int:
            nums = [n % p for n in nums]
            rem = sum(nums) % p
            if rem == 0: return 0
            if rem in nums: return 1
            pre_sum = [0]
            post_sum = [0]
            for n in nums:
                pre_sum.append((pre_sum[-1] + n) % p)
            for n in nums[::-1]:
                post_sum.append((post_sum[-1] + n) % p)
            post_sum.reverse()
            post_sum_dict = collections.defaultdict(list)
            for i, post in enumerate(post_sum):
                post_sum_dict[post].append(i + 1)

            res = len(nums)
            for i, pre in enumerate(pre_sum):
                if i > 0:
                    tmp = (p - pre) % p
                    if tmp not in post_sum_dict:
                        continue
                    else:
                        if i + 1 > post_sum_dict[tmp][-1]:
                            continue
                        else:
                            ind = bisect.bisect_right(post_sum_dict[tmp], i)
                            next_ind = post_sum_dict[tmp][ind]
                            res = min(res, next_ind - i - 1)
            return res if res < len(nums) else len(nums)

        ret = len(A)
        ret = min(ret, helper(A))
        A.reverse()
        ret = min(ret, helper(A))
        return ret if ret < len(A) else -1


so = Solution()
print(so.minSubarray(A=[3, 1, 4, 2], p=6))
print(so.minSubarray(A=[6, 3, 5, 2], p=9))
print(so.minSubarray(A=[1, 2, 3], p=3))
print(so.minSubarray(A=[1, 2, 3], p=7))
print(so.minSubarray(A=[1000000000, 1000000000, 1000000000], p=3))
print(so.minSubarray(A=list(range(100000)), p=10000000000))
print(so.minSubarray([8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2], 148))
