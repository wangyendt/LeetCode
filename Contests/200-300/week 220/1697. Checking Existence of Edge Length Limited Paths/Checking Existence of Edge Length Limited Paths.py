#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Checking Existence of Edge Length Limited Paths
@time: 2020/12/20 12:04
"""


class Solution:
    def distanceLimitedPathsExist(self, n, E, Q):
        # this part is union-find
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y: return 0
            root[x] = y
            return 1

        root = list(range(n))

        # this will be the answer
        ans = [False] * len(Q)

        # sort edges based on cost
        i = 0
        E.sort(key=lambda x: x[2])

        # don't sort Q, but get the sorted list of queries in ix_all
        q = [x[2] for x in Q]
        ix_all = sorted(range(len(q)), key=q.__getitem__)
        for ix in ix_all:  # loop over sorted indices of Q
            # add all edges that satisfy cost requirement
            while i < len(E) and E[i][2] < Q[ix][2]:
                x, y = E[i][0], E[i][1]
                i += 1
                uni(x, y)

            # check if the query nodes are connected
            if find(Q[ix][0]) == find(Q[ix][1]):
                ans[ix] = True

        return ans
