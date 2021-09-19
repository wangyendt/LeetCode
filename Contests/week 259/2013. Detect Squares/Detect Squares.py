#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Detect Squares.py 
@time: 2021/09/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class DetectSquares:

    def __init__(self):
        self.all_pt = collections.defaultdict(int)
        self.ys = collections.defaultdict(set)
        self.xs = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.all_pt[(x, y)] += 1
        self.xs[x].add(y)
        self.ys[y].add(x)

    def count(self, point: List[int]) -> int:
        x, y = point
        ret = 0
        for xx in self.ys[y]:
            if xx != x:
                yy = y + (x - xx)
                if yy in self.xs[x]:
                    if (xx, yy) in self.all_pt:
                        ret += self.all_pt[(xx, y)] * self.all_pt[(xx, yy)] * self.all_pt[(x, yy)]
                yy = y - (x - xx)
                if yy in self.xs[x]:
                    if (xx, yy) in self.all_pt:
                        ret += self.all_pt[(xx, y)] * self.all_pt[(xx, yy)] * self.all_pt[(x, yy)]
        return ret
