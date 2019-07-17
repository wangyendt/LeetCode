# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/17 10:13
# software: PyCharm


class Solution:
    def singleNumber(self, nums: list) -> int:
        a, b = 0, 0
        for n in nums:
            a, b, c = a ^ n, b | (a & n), b & n
            a, b = a & ~c, b & ~c
        return a


so = Solution()
print(so.singleNumber([2, 2, 3, 2]))
