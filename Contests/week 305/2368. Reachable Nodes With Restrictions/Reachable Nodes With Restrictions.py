#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Reachable Nodes With Restrictions.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        post = collections.defaultdict(list)
        for e1, e2 in edges:
            post[e1].append(e2)
            post[e2].append(e1)
        seen = {0} | set(restricted)
        stack = [0]
        ret = 1
        while stack:
            s = stack.pop()
            for leaf in post[s]:
                if leaf not in seen:
                    ret += 1
                    stack.append(leaf)
                    seen.add(leaf)
        return ret


so = Solution()
print(so.reachableNodes(n=7, edges=[[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted=[4, 5]))
