#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Winner of the Circular Game.py 
@time: 2021/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1
