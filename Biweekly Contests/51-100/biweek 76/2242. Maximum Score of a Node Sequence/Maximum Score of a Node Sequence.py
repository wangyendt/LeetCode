#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Score of a Node Sequence.py 
@time: 2022/04/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq
import itertools


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        res = collections.defaultdict(list)
        for e1, e2 in edges:
            heapq.heappush(res[e1], (scores[e2], e2))
            heapq.heappush(res[e2], (scores[e1], e1))
        for k, v in res.items():
            res[k] = heapq.nlargest(3, v)
        ret = -1
        for e1, e2 in edges:
            for (s_nei_1, nei_1), (s_nei_2, nei_2) in itertools.product(res[e1], res[e2]):
                if nei_1 != e2 and nei_2 != e1 and nei_1 != nei_2:
                    ret = max(ret, s_nei_1 + scores[e1] + scores[e2] + s_nei_2)
        return ret


so = Solution()
print(so.maximumScore(scores=[5, 2, 9, 8, 4], edges=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
