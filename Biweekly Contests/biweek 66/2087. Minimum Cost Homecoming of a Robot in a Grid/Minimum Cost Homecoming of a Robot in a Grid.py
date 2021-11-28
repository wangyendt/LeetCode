#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Cost Homecoming of a Robot in a Grid.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ret = 0
        if startPos[0] > homePos[0]:
            ret += sum(rowCosts[i] for i in range(homePos[0], startPos[0]))
        else:
            ret += sum(rowCosts[i] for i in range(startPos[0] + 1, homePos[0] + 1))
        if startPos[1] > homePos[1]:
            ret += sum(colCosts[j] for j in range(homePos[1], startPos[1]))
        else:
            ret += sum(colCosts[j] for j in range(startPos[1] + 1, homePos[1] + 1))
        return ret
