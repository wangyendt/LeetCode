#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Consecutive Floors Without Special Floors.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        top -= bottom
        special = [0] + [s - bottom for s in special]
        ret = 0
        #         print(special,bottom,top)
        for i, s in enumerate(special):
            if i == 1:
                ret = max(ret, s - special[i - 1])
            elif i > 0:
                ret = max(ret, s - special[i - 1] - 1)
        ret = max(top - special[-1], ret)
        return ret
