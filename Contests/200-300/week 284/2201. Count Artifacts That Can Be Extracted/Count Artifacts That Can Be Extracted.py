#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Artifacts That Can Be Extracted.py 
@time: 2022/03/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ret = 0
        dig = set((d1, d2) for d1, d2 in dig)
        for i, a in enumerate(artifacts):
            tlx, tly, brx, bry = a
            b = False
            for x in range(tlx, brx + 1):
                for y in range(tly, bry + 1):
                    if (x, y) not in dig:
                        b = True
                        break
                if b:
                    break
            if not b:
                ret += 1
        return ret
