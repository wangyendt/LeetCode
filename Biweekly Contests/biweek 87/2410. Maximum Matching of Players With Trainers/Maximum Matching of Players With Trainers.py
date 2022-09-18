#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Matching of Players With Trainers.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        m, n = len(players), len(trainers)
        ret = 0
        while i < m and j < n:
            if players[i] <= trainers[j]:
                ret += 1
                i += 1
                j += 1
            else:
                j += 1
        return ret
