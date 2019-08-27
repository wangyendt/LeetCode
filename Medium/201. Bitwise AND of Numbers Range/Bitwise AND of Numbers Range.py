# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/27 16:27
# software: PyCharm


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        p = n
        while p and p > m:
            p = p & (p - 1)
        return p


so = Solution()
print(so.rangeBitwiseAnd(5, 7))
print(so.rangeBitwiseAnd(0, 1))
print(so.rangeBitwiseAnd(2, 3))
