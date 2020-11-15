#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Defuse the Bomb.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0: return [0] * n
        code *= 3
        ret = []
        for i in range(n, 2 * n):
            if k > 0:
                ret.append(sum(code[i + 1:i + k + 1]))
            else:
                ret.append(sum(code[i + k:i]))
        return ret


so = Solution()
print(so.decrypt(code=[5, 7, 1, 4], k=3))
