#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Construct K Palindrome Strings.py 
@time: 2020/04/08
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= sum([1 for k, v in collections.Counter(s).items() if v % 2 == 1])


so = Solution()
print(so.canConstruct(s="annabelle", k=2))
print(so.canConstruct(s="leetcode", k=3))
print(so.canConstruct(s="true", k=4))
print(so.canConstruct(s="yzyzyzyzyzyzyzy", k=2))
print(so.canConstruct(s="cr", k=7))
