#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Total Beauty of the Gardens.py 
@time: 2022/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        A, new, t, full, part = flowers, newFlowers, target, full, partial
        A = [min(t, a) for a in A]
        A.sort()

        # Two edge cases
        if min(A) == t: return full * len(A)
        if new >= t * len(A) - sum(A):
            return max(full * len(A), full * (len(A) - 1) + part * (t - 1))

        # Build the array `cost`.
        cost = [0]
        for i in range(1, len(A)):
            pre = cost[-1]
            cost.append(pre + i * (A[i] - A[i - 1]))

        # Since there might be some gardens having `target` flowers already, we will skip them.
        j = len(A) - 1
        while A[j] == t:
            j -= 1

        # Start the iteration
        ans = 0
        while new >= 0:
            # idx stands for the first `j` gardens, notice a edge case might happen.
            idx = min(j, bisect.bisect_right(cost, new) - 1)

            # bar is the current minimum flower in the incomplete garden
            bar = A[idx] + (new - cost[idx]) // (idx + 1)

            ans = max(ans, bar * part + full * (len(A) - j - 1))

            # Now we would like to complete garden j, thus deduct the cost for garden j
            # from new and move on to the previous(next) incomplete garden!
            new -= (t - A[j])
            j -= 1

        return ans
