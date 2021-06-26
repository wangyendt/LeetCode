#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design Movie Rental System.py 
@time: 2021/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys

sys.path.append('../..')
from Tools.API_utils import *
import collections
from sortedcontainers import SortedList


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.A = collections.defaultdict(SortedList)
        self.B = collections.defaultdict(int)
        self.R = SortedList()
        for sh, m, p in entries:
            self.A[m].add((p, sh))
            self.B[(sh, m)] = p

    def search(self, movie: int) -> List[int]:
        return [v for _, v in self.A[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.B[(shop, movie)]
        self.A[movie].remove((p, shop))
        self.R.add((p, movie, shop))

    def drop(self, shop: int, movie: int) -> None:
        p = self.B[(shop, movie)]
        self.R.remove((p, movie, shop))
        self.A[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        return [[s, m] for p, m, s in self.R[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
call_me(
    MovieRentingSystem,
    ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"],
    [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]],
     [1], [0, 1], [1, 2], [], [1, 2], [2]]
)
