#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check Whether Two Strings are Almost Equivalent.py 
@time: 2021/11/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import string
import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for letter in string.ascii_lowercase:
            if abs(collections.Counter(word1)[letter] - collections.Counter(word2)[letter]) > 3:
                return False
        return True


so = Solution()
print(so.checkAlmostEquivalent(word1="abcdeef", word2="abaaacc"))
