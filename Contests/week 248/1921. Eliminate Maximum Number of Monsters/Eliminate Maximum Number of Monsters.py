#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Eliminate Maximum Number of Monsters.py 
@time: 2021/07/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        t = [d / s for d, s in zip(dist, speed)]
        t.sort()
        ret = 0
        for i, tt in enumerate(t):
            if tt <= i:
                break
            ret += 1
        return ret


so = Solution()
print(so.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))
