"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Longest Semi-Repetitive Substring.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import itertools


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ret = 0
        for i, j in itertools.product(range(len(s)), range(len(s))):
            t = s[i:j + 1]
            res, prev = 0, '_'
            for l, tt in enumerate(t):
                if tt == prev:
                    res += 1
                if res >= 2:
                    ret = max(ret, l)
                    break
                prev = tt
            else:
                ret = max(ret, len(t))
        return ret


so = Solution()
print(so.longestSemiRepetitiveSubstring(s="52233"))
print(so.longestSemiRepetitiveSubstring(s="5494"))
