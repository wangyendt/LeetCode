#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Stock Price Fluctuation.py
@time: 2021/10/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import bisect
from sortedcontainers import SortedDict, SortedList


class StockPrice:

    def __init__(self):
        self.A = SortedDict()
        self.mx = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.A:
            self.mx.add(price)
        else:
            idx = self.mx.bisect_left(self.A[timestamp])
            # self.mx[idx:idx + 1] = []
            del self.mx[idx]
            self.mx.add(price)
        self.A.update({timestamp: price})

    def current(self) -> int:
        return self.A.values()[-1]

    def maximum(self) -> int:
        return self.mx[-1]

    def minimum(self) -> int:
        return self.mx[0]
