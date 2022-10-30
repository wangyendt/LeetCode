#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: XOR Operation in an Array
@time: 2020/06/21 10:30
"""

import functools


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = [start + 2 * i for i in range(n)]
        print(res)
        return functools.reduce(
            lambda x, y: x ^ y, res
        )


so = Solution()
print(so.xorOperation(5, 0))
