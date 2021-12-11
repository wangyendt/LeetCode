#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sequentially Ordinal Rank Tracker.py 
@time: 2021/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from sortedcontainers import SortedList


class SORTracker:

    def __init__(self):
        self.A = SortedList()
        self.cnt = 0

    def add(self, name: str, score: int) -> None:
        self.A.add((-score, name))

    def get(self) -> str:
        self.cnt += 1
        return self.A[self.cnt - 1][1]
