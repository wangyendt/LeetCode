#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Nice Substring.py 
@time: 2021/02/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return ''
        s_set = set(s)
        for i, ss in enumerate(s):
            if ss.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i + 1:])
                return max(s1, s2, key=len)
        return s


so = Solution()
print(so.longestNiceSubstring('YazaAay'))
print(so.longestNiceSubstring('Bb'))
print(so.longestNiceSubstring('c'))
print(so.longestNiceSubstring('dDzeE'))
