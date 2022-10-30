#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Restore the Array From Adjacent Pairs.py 
@time: 2021/01/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a1, a2 in adjacentPairs:
            graph[a1].append(a2)
            graph[a2].append(a1)
        start = -1
        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break
        ret = [start]
        last = start
        seen = {start}
        for i in range(len(adjacentPairs) + 1):
            for it in graph[last]:
                if it not in seen:
                    seen.add(it)
                    ret.append(it)
                    last = it
        return ret


so = Solution()
print(so.restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]]))
print(so.restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]))
