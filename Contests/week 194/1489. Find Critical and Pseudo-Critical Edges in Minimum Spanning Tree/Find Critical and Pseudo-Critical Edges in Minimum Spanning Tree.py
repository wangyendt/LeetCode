#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
@time: 2020/06/21 12:13
"""


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, e: list(list())) -> list(list()):
        for i in range(len(e)):
            e[i].append(i)
        e.sort(key=lambda v: v[2])

        def mst(a, ig):
            def root(n):
                if a[n] == n:
                    return n
                a[n] = root(a[n])
                return a[n]

            w = 0
            for vv in e:
                if vv[3] == ig:
                    continue
                u, v = root(vv[0]), root(vv[1])
                if u == v:
                    continue
                w += vv[2]
                a[u] = v
            for i in range(n):
                if root(i) != root(0):
                    return 1 << 30
            return w

        self.ms = mst([k for k in range(n)], -1)
        print(self.ms)

        def cric():
            ans = []
            for i in range(len(e)):
                a = [j for j in range(n)]
                v = mst(a, i)
                if self.ms < v:
                    # print(a,i,v)
                    ans.append(i)
            return ans

        def pcric():
            ans = []
            for vv in e:
                a = [j for j in range(n)]
                a[vv[0]] = vv[1]
                if self.ms == mst(a, vv[3]) + vv[2]:
                    ans.append(vv[3])
            return ans

        cr = cric()
        pcr = pcric()
        d = {x for x in cr}
        ppcr = []
        for x in pcr:
            if x in d:
                continue
            ppcr.append(x)
        return [cr, ppcr]
