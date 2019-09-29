# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 17:09
# software: PyCharm
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        l, r = 1, max(a, b, c) * n

        def gcd(x, y):
            if x == 0:
                return y
            return gcd(y % x, x)

        def lcm(x, y):
            return x * y // gcd(x, y)

        def count(m):
            return m // a + m // b + m // c - (m // lcm(a, b) + m // lcm(a, c) + m // lcm(b, c)) + \
                   m // lcm(a, lcm(b, c))

        while l < r:
            mid = (l + r) // 2
            if count(mid) < n:
                l = mid + 1
            else:
                r = mid

        return r


so = Solution()
print(so.nthUglyNumber(n=3, a=2, b=3, c=5))
