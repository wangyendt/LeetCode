#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Palindrome With Fixed Length.py 
@time: 2022/03/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = 10 ** ((intLength - 1) // 2)
        ret = [q - 1 + base for q in queries]
        for i, a in enumerate(ret):
            a = str(a) + str(a)[-1 - intLength % 2::-1]
            ret[i] = int(a) if len(a) == intLength else -1
        return ret


so = Solution()
print(so.kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3))
