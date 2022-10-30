#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 2:08
@Author:  wang121ye
@File: Increasing Decreasing String.py
@Software: PyCharm
"""

import collections


class Solution:
    def sortString(self, s: str) -> str:
        stack = set()
        count = collections.defaultdict(int)
        for ss in s:
            count[ss] += 1
            stack.add(ss)
        stack = sorted(list(stack))
        ret = ''
        while True:
            for s in stack:
                if s in count:
                    if count[s] > 0:
                        ret += s
                        count[s] -= 1
                    if count[s] == 0:
                        count.pop(s)
            for s in stack[::-1]:
                if s in count:
                    if count[s] > 0:
                        ret += s
                        count[s] -= 1
                    if count[s] == 0:
                        count.pop(s)
            if not count: return ret


so = Solution()
print(so.sortString(s="aaaabbbbcccc"))
print(so.sortString(s="rat"))
print(so.sortString(s="leetcode"))
print(so.sortString(s="ggggggg"))
print(so.sortString(s="spo"))
