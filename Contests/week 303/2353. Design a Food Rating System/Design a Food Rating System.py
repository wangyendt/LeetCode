#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design a Food Rating System.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
import sys
from typing import *

sys.path.append('../..')
from sortedcontainers import SortedList


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.A = collections.defaultdict(SortedList)
        self.T = collections.defaultdict(str)
        self.I = collections.defaultdict(tuple)
        for f, c, r in zip(foods, cuisines, ratings):
            self.A[c].add((-r, f))
            self.T[f] = c
            self.I[f] = (-r, f)

    def changeRating(self, food: str, newRating: int) -> None:
        # print(self.A)
        self.A[self.T[food]].remove(self.I[food])
        self.A[self.T[food]].add((-newRating, food))
        self.I[food] = (-newRating, food)

    def highestRated(self, cuisine: str) -> str:
        return self.A[cuisine][0][1]
