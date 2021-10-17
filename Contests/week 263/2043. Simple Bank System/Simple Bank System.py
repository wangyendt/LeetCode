#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Simple Bank System.py
@time: 2021/10/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Bank:

    def __init__(self, balance: List[int]):
        self.A = collections.defaultdict(int)
        for i, b in enumerate(balance):
            self.A[i + 1] = b

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.A and account2 in self.A:
            if self.A[account1] >= money:
                self.A[account1] -= money
                self.A[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.A:
            self.A[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.A:
            if self.A[account] >= money:
                self.A[account] -= money
                return True
        return False
