#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Enemy Forts That Can Be Captured.py 
@time: 2022/12/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ret = 0
        for i in range(len(forts)):
            if forts[i] == 1:
                res1 = 0
                for j in range(i - 1, -1, -1):
                    if forts[j] == 0:
                        res1 += 1
                    elif forts[j] == 1:
                        res1 = 0
                        break
                    elif forts[j] == -1:
                        break
                else:
                    res1 = 0
                res2 = 0
                for j in range(i + 1, len(forts)):
                    if forts[j] == 0:
                        res2 += 1
                    elif forts[j] == 1:
                        res2 = 0
                        break
                    elif forts[j] == -1:
                        break
                else:
                    res2 = 0
                ret = max(ret, res1, res2)
        return ret


so = Solution()
print(so.captureForts(forts=[1, 0, 0, -1, 0, 0, 0, 0, 1]))
