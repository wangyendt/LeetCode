#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design Bitset.py 
@time: 2022/02/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Bitset:

    def __init__(self, size: int):
        self.A = ['0'] * size
        self.B = ['1'] * size
        self.cnt = 0
        self.size = size

    def fix(self, idx: int) -> None:
        a = int(self.A[idx])
        self.cnt += 1 - a
        self.A[idx] = '1'
        self.B[idx] = '0'

    def unfix(self, idx: int) -> None:
        a = int(self.A[idx])
        self.cnt -= a - 0
        self.A[idx] = '0'
        self.B[idx] = '1'

    def flip(self) -> None:
        self.cnt = self.size - self.cnt
        self.A, self.B = self.B, self.A

    def all(self) -> bool:
        return self.cnt == self.size

    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return ''.join(self.A)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
