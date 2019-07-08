# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/8 10:18
# software: PyCharm

class Solution:
    def candy(self, ratings: list) -> int:
        n = len(ratings)
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp1[i] = dp1[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                dp2[i - 1] = dp2[i] + 1
        dp = [max(d1, d2) for d1, d2 in zip(dp1, dp2)]
        return sum(dp)


so = Solution()
print(so.candy([1, 0, 2]))
