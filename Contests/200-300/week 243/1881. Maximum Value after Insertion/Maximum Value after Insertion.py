#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Value after Insertion.py 
@time: 2021/05/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import sys


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        m = len(n)
        if n[0] == '-':
            for i in range(1, m):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i in range(m):
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)


so = Solution()
print(so.maxValue("-9942658573228629141573597132374463682568616882794268877657345133381914", 4))
print(so.maxValue("-132", 3))
print(so.maxValue("28824579515", 8))
