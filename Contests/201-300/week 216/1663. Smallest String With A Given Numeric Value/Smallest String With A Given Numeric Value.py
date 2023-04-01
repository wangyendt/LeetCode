#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Smallest String With A Given Numeric Value
@time: 2020/11/22 10:33
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        letters = {l: i + 1 for i, l in enumerate(abc)}
        ret = ''
        for i in range(n):
            if k <= 26 * (n - 1 - i):
                ret += 'a'
            else:
                ret += abc[k - 26 * (n - 1 - i) - 1]
            k -= letters[ret[-1]]
        return ret


so = Solution()
print(so.getSmallestString(3, 27))
