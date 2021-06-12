#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Cost to Change the Final Value of Expression
@time: 2021/06/13 00:30
"""


class Solution:
    def minOperationsToFlip(self, E):
        def corr(s):
            stack, d = [], {}
            for i, elem in enumerate(s):
                if elem == "(":
                    stack.append(i)
                elif elem == ")":
                    last = stack.pop()
                    d[i] = last
            return d

        def dfs(beg, end):
            if beg == end: return (int(E[beg]), 1)
            if E[end] in "01":
                p1, c1 = dfs(beg, end - 2)
                p2, c2 = dfs(end, end)
                op = E[end - 1]
            else:
                if d[end] == beg: return dfs(beg + 1, end - 1)
                p1, c1 = dfs(beg, d[end] - 2)
                p2, c2 = dfs(d[end], end)
                op = E[d[end] - 1]

            if op == "|":
                c3 = 1 if p1 + p2 == 1 else min(c1, c2) + p1
                return (p1 | p2, c3)
            else:
                c3 = 1 if p1 + p2 == 1 else min(c1, c2) + 1 - p1
                return (p1 & p2, c3)

        d = corr(E)
        return dfs(0, len(E) - 1)[1]
