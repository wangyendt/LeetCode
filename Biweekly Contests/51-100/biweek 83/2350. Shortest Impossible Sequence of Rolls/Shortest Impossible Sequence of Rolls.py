#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Shortest Impossible Sequence of Rolls.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ret = 1
        seen = set()
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                seen.clear()
                ret += 1
        return ret
