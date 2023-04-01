#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Consecutive Integers from a Data Stream.py 
@time: 2023/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class DataStream:

    def __init__(self, value: int, k: int):
        self.A = [-1, -1]
        self.val = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.A[0]:
            self.A[1] += 1
        else:
            self.A[0] = num
            self.A[1] = 1
        return self.A[0] == self.val and self.A[1] >= self.k
