#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Partition Array Into Two Arrays to Minimize Sum Difference.py
@time: 2021/10/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools
import bisect


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2  # Note this is N/2, ie no. of elements required in each.

        def get(nums):  # generate all combinations sum of k elements
            ans = {}
            for k in range(1, N):  # takes k element for nums
                b = []
                for a in itertools.combinations(nums, k):
                    s = sum(a)
                    b.append(s)
                ans[k] = b
            return ans

        left_part, right_part = nums[:N], nums[N:]
        left, right = get(left_part), get(right_part)
        ans = abs(
            sum(left_part) - sum(right_part))  # the case when taking all N from left_part for left_ans, and vice versa
        total = sum(nums)
        half = total // 2  # the best sum required for each, we have to find sum nearest to this
        for k in range(1, N):
            a = left[k]  # if taking k no. from left
            b = right[N - k]  # then we have to take remaining N-k from right.
            b = sorted(set(b))
            for x in a:
                r = half - x  # remaining, how much we need to add in x to bring it closer to half.
                p = bisect.bisect_left(b, r)
                for q in [p, p - 1]:
                    if 0 <= q < len(b):
                        left_ans_sum = x + b[q]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        ans = min(ans, diff)
        return ans


so = Solution()
print(so.minimumDifference([256, -262, -750, -151, 121, 636, 64, 834] * 3))
print(so.minimumDifference([3, 9, 7, 3]))
