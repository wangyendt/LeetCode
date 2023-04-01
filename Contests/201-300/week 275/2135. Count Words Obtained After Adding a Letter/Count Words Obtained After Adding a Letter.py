#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Words Obtained After Adding a Letter.py 
@time: 2022/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords:
            m = 0
            for ch in word: m ^= 1 << ord(ch) - 97
            seen.add(m)

        ans = 0
        for word in targetWords:
            m = 0
            for ch in word: m ^= 1 << ord(ch) - 97
            for ch in word:
                if m ^ (1 << ord(ch) - 97) in seen:
                    ans += 1
                    break
        return ans
