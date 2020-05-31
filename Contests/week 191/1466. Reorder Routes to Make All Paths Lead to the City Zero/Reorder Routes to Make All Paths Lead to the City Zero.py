#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reorder Routes to Make All Paths Lead to the City Zero
@time: 2020/05/31 10:47
"""

import collections


class City:
    def __init__(self, ind):
        self.ind = ind
        self.prev = []
        self.post = []


class Solution:
    def minReorder(self, n: int, connections: list(list())) -> int:
        cons = {i: City(i) for i in range(n)}
        for conp, conq in connections:
            cons[conp].post.append(conq)
            cons[conq].prev.append(conp)
        stack = [0]
        ret = 0
        flag = collections.defaultdict(int)
        while stack:
            stack_ = []
            while stack:
                s = stack.pop()
                # print(stack)
                flag[s] = 1
                for post in cons[s].post:
                    if not flag[post]:
                        ret += 1
                        stack_.append(post)
                        # flag[post] = 1
                for prev in cons[s].prev:
                    if not flag[prev]:
                        stack_.append(prev)
                        # flag[prev] = 1
                # print(stack, s, cons[s].post, cons[s].prev, stack_)
            for s in stack_:
                # print(stack_, flag[s])
                if not flag[s]:
                    stack.append(s)
        return ret


so = Solution()
print(so.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(so.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
print(so.minReorder(n=3, connections=[[1, 0], [2, 0]]))
