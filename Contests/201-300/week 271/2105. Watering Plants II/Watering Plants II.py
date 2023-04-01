#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Watering Plants II.py 
@time: 2021/12/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        p = 0
        q = n - 1
        cur_a = capacityA
        cur_b = capacityB
        ret = 0
        while True:
            if p < q:
                if cur_a >= plants[p]:
                    cur_a -= plants[p]
                else:
                    ret += 1
                    cur_a = capacityA - plants[p]
                if cur_b >= plants[q]:
                    cur_b -= plants[q]
                else:
                    ret += 1
                    cur_b = capacityB - plants[q]
            elif p == q:
                if max(cur_a, cur_b) >= plants[p]:
                    break
                else:
                    ret += 1
            else:
                break
            p += 1
            q -= 1
        return ret
