#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Deletions to Make Character Frequencies Unique
@time: 2020/11/08 10:37
"""

import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        cnter = sorted(collections.Counter(s).values())
        cnter2 = collections.Counter(cnter)
        # print(cnter, cnter2)
        ret = 0
        while True:
            for k in cnter2.keys():
                if k <= 0: continue
                if cnter2[k] > 1:
                    cnter2[k] -= 1
                    cnter2[k - 1] += 1
                    ret += 1
                    break
            else:
                break
        return ret


so = Solution()
print(so.minDeletions('a'))
print(so.minDeletions('b'))
print(so.minDeletions('aaabbbcc'))
print(so.minDeletions('a' * 2000 + 'b' * 2000 + 'c' * 2000))
