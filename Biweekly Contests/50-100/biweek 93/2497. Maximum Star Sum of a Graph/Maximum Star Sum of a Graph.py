#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Star Sum of a Graph.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maxStarSum(self, v: List[int], edges: List[List[int]], k: int) -> int:

        g = collections.defaultdict(set)
        for i, j in edges:
            if v[i] > 0: g[j].add(i)
            if v[j] > 0: g[i].add(j)

        return max(w + sum(sorted([v[j] for j in g[i]])[-k:]) for i, w in enumerate(v))
