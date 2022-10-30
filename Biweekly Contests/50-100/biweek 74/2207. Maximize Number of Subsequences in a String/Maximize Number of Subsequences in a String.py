#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize Number of Subsequences in a String.py 
@time: 2022/03/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections

import collections


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        text = ''.join(t for t in text if t in pattern)
        if pattern[0] == pattern[1]:
            if pattern[0] in text:
                c = collections.Counter(text)[pattern[0]]
                return c * (c + 1) // 2
            else:
                return 0
        else:
            s1 = pattern[0] + text
            s2 = text + pattern[1]

            def helper(ss):
                n = len(ss)
                res = collections.defaultdict(int)
                for i in range(n)[::-1]:
                    if ss[i] == pattern[1]:
                        res[i] = res[i + 1] + 1
                    else:
                        res[i] = res[i + 1]
                ret = 0
                for i, tt in enumerate(ss):
                    if tt == pattern[0]:
                        ret += res[i]
                return ret

            return max(helper(s1), helper(s2))


so = Solution()
print(so.maximumSubsequenceCount(text="abdcdbc", pattern="ac"))
