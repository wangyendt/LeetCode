#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/15 17:44
@Author:  wang121ye
@File: Maximum Performance of a Team.py
@Software: PyCharm
"""

import bisect
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: list, efficiency: list, k: int) -> int:
        teams = sorted([(e, s) for e, s in zip(efficiency, speed)], reverse=True)
        pq = []
        max_perf = s = 0
        for i in range(n):
            heapq.heappush(pq, teams[i][1])
            s += teams[i][1]
            if i >= k:
                s -= heapq.heappop(pq)
            max_perf = max(max_perf, s * teams[i][0])
        return max_perf % (10 ** 9 + 7)

    def maxPerformance2(self, n: int, speed: list, efficiency: list, k: int) -> int:
        A = sorted(zip(speed, efficiency), key=lambda x: (x[1], -x[0]))
        B = [x[0] for x in A]
        B.sort(reverse=True)
        modulo = 10 ** 9 + 7
        # last = -1
        dp = [0] * n
        sum_ = 0
        for i in range(n):
            ind = bisect.bisect(B, A[i][0])
            B = B[:ind] + B[ind + 1:]
            # B.remove(A[i][0])
            # if A[i][1] == last:
            #     continue
            dp[i] = A[i][0] * A[i][1]
            # if len(B) >= k - 1:
            # dp[i] += A[i][1] * sum(B[:k - 1])
            if sum_ == 0:
                sum_ = sum(B[:k - 1])
            else:
                if ind < k - 1:
                    sum_ -= A[i][0]
                    if k - 2 < len(B):
                        sum_ += B[k - 2]
            dp[i] += A[i][1] * sum_  # sum(B[:k - 1])
            # last = A[i][1]
        return max(dp) % modulo


so = Solution()
# print(so.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2))
# print(so.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3))
# print(so.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4))
# print(so.maxPerformance(7,
#                         [1, 4, 1, 9, 4, 4, 4],
#                         [8, 2, 1, 7, 1, 8, 4],
#                         6))
n = 100000
speed = list(range(1, 100001))
efficiency = list(range(1, 100001))
k = 86484
print(so.maxPerformance(n, speed, efficiency, k))
