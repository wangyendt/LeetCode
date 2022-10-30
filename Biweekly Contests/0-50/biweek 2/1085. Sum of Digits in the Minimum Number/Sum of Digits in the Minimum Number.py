# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/15 23:30
# software: PyCharm


class Solution:
    def sumOfDigits(self, A: list) -> int:
        if not A:
            return 0
        S = min(A)
        su = 0
        while S:
            su += S % 10
            S = S // 10
        return 1 if su % 2 == 0 else 0


so = Solution()
print(so.sumOfDigits([99, 77, 33, 66, 55]))
