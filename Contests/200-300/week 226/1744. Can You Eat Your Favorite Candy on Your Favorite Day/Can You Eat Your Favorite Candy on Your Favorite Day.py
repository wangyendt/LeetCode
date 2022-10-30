#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Can You Eat Your Favorite Candy on Your Favorite Day.py 
@time: 2021/01/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for x in candiesCount: prefix.append(prefix[-1] + x)  # prefix sum
        return [prefix[t] < (day + 1) * cap and day < prefix[t + 1] for t, day, cap in queries]
