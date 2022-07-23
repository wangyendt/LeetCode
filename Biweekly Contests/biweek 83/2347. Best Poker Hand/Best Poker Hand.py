#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Best Poker Hand.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1: return 'Flush'
        res = collections.Counter(ranks).most_common(1)
        # print(res)
        if res[0][1] >= 3: return 'Three of a Kind'
        if res[0][1] == 2: return 'Pair'
        return 'High Card'
