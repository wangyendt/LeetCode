#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Center of Star Graph.py 
@time: 2021/03/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for e1, e2 in edges:
            g[e1].add(e2)
            g[e2].add(e1)
        for k, v in g.items():
            if len(v) == len(edges):
                return k
