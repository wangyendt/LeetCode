#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/26 19:43
@Author:  wang121ye
@File: Maximum Score After Splitting a String.py
@Software: PyCharm
"""


class Solution:
    def maxScore(self, s: str) -> int:
        l, r, ret = 0, sum(map(int, s)), 0
        for i in range(1, len(s)):
            # print(l,r)
            if s[i - 1] == '0':
                l += 1
            else:
                r -= 1
            ret = max(ret, l + r)
        return ret


so = Solution()
print(so.maxScore('011101'))
print(so.maxScore('00111'))
print(so.maxScore('1111'))
