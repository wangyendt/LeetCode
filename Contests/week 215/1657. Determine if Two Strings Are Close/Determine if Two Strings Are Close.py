#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Determine if Two Strings Are Close.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(collections.Counter(word1).values()) == \
               sorted(collections.Counter(word2).values()) and set(word1) == set(word2)


so = Solution()
print(so.closeStrings('abc', 'bca'))
