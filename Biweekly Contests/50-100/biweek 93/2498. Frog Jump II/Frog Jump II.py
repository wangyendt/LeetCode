#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Frog Jump II.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


from typing import *
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])

        # to simplify logic below
        if len(stones) % 2 == 0:
            stones.append(stones[-1] + 1)

        j = 0

        # -> go forward
        for i in range(0, len(stones) - 2, 2):
            j = max(j, abs(stones[i] - stones[i+2]))

        # <- go backward
        for i in range(1, len(stones) - 2, 2):
            j = max(j, abs(stones[i] - stones[i+2]))

        return j