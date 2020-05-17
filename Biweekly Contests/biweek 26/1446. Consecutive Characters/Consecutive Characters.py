#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 12:09
@Author:  wang121ye
@File: Consecutive Characters.py
@Software: PyCharm
"""


class Solution:
    def maxPower(self, s: str) -> int:
        ret, cur, last = 1, 1, '?'
        for t in s:
            if t == last:
                cur += 1
                ret = max(ret, cur)
            else:
                cur = 1
            last = t
        return ret


so = Solution()
print(so.maxPower("leetcode"))
print(so.maxPower("abbcccddddeeeeedcba"))
print(so.maxPower("triplepillooooow"))
print(so.maxPower("hooraaaaaaaaaaay"))
print(so.maxPower("tourist"))
