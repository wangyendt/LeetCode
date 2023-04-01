#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design a Number Container System.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections

from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.A = collections.defaultdict(SortedList)
        self.B = collections.defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if self.B[index] != 0:
            if self.B[index] != number:
                print(index)
                print(self.B[index])
                print(self.A)
                self.A[self.B[index]].remove(index)
                self.A[number].add(index)
        else:
            self.A[number].add(index)

        self.B[index] = number

    def find(self, number: int) -> int:
        res = self.A[number]
        if res: return res[0]
        return -1
