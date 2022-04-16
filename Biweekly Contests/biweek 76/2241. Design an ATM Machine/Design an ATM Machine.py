#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design an ATM Machine.py 
@time: 2022/04/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class ATM:

    def __init__(self):
        self.A = [0, 0, 0, 0, 0]
        self.B = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, b in enumerate(banknotesCount):
            self.A[i] += b

    def withdraw(self, amount: int) -> List[int]:
        c = [0, 0, 0, 0, 0]
        a = self.A.copy()
        for i in range(4, -1, -1):
            if amount >= self.B[i]:
                m, d = divmod(amount, self.B[i])
                if a[i] >= m:
                    c[i] += m
                    a[i] -= m
                    if d == 0:
                        self.A = a[:]
                        return c
                    else:
                        amount = d
                else:
                    amount -= a[i] * self.B[i]
                    c[i] += a[i]
                    a[i] = 0
        return [-1]
