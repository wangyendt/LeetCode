#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Lattice Points Inside a Circle.py 
@time: 2022/04/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ret = 0
        res = set()
        for cx, cy, cr in circles:
            for x, y in itertools.product(range(cx - cr, cx + 1), range(cy - cr, cy + 1)):
                if (x - cx) ** 2 + (y - cy) ** 2 <= cr ** 2:
                    res.add((x, y))
                    res.add((2 * cx - x, y))
                    res.add((x, 2 * cy - y))
                    res.add((2 * cx - x, 2 * cy - y))
        return len(res)
