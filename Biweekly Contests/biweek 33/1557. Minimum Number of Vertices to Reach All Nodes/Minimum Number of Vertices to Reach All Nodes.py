#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Minimum Number of Vertices to Reach All Nodes.py 
@time: 2020/08/22
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list(list())) -> list:
        s1, s2 = set(range(n)), set()
        for e in edges:
            s2.add(e[1])
        return list(s1 - s2)


so = Solution()
print(so.findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(so.findSmallestSetOfVertices(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
