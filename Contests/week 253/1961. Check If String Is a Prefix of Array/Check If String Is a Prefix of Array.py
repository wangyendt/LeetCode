#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check If String Is a Prefix of Array.py 
@time: 2021/08/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        p = 0
        for w in words:
            lw = len(w)
            # print(lw, n - p)
            if lw <= n - p:
                # print(w, s[p:p + lw])
                if w != s[p:p + lw]:
                    return False
            else:
                return False
            p += lw
            if p == n: return True
        return p == n
        # return True


so = Solution()
print(so.isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"]))
