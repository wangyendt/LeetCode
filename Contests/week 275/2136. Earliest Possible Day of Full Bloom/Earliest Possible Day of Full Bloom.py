#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Earliest Possible Day of Full Bloom.py 
@time: 2022/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def earliestFullBloom(self, P: List[int], G: List[int]) -> int:
        pairs = sorted((g, p) for g, p in zip(G, P))
        P = [p for _, p in pairs]
        G = [g for g, _ in pairs]
        ans, Q = sum(P), sum(P)
        p_acc = [0] + list(itertools.accumulate(P))
        for i in range(len(pairs)):
            ans = max(ans, Q - p_acc[i] + G[i])
        return ans
