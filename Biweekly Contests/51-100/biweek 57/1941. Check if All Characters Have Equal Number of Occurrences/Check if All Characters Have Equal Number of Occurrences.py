#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if All Characters Have Equal Number of Occurrences.py 
@time: 2021/07/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(collections.Counter(s).values())) == 1


so = Solution()
print(so.areOccurrencesEqual('abcabc'))
