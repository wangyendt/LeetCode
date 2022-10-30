#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Substrings With Only 1s
@time: 2020/07/12 10:34
"""


class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        ret = 0
        for t in s:
            if t == '0':
                ret += (1 + cnt) * cnt // 2
                cnt = 0
            else:
                cnt += 1
        ret += (1 + cnt) * cnt // 2
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.numSub('101'))
