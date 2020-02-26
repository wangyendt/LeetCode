#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Substrings Containing All Three Characters
@time: 2020/2/26 16:38
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = j = ret = 0
        n, stack = len(s), ''
        while True:
            # print(f'stack:{stack}')
            while stack and all([l in stack for l in 'abc']):
                # print(stack, i, j, n - (len(stack) + i) + 1)
                ret += n - (len(stack) + i) + 1
                i += 1
                stack = stack[1:]
            else:
                if j == n: break
                stack += s[j]
                j += 1
            # print(i, j, stack)
        return ret


so = Solution()
print(so.numberOfSubstrings('abcabc'))
print(so.numberOfSubstrings('aaacb'))
print(so.numberOfSubstrings('abc'))
