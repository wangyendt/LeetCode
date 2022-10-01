"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Number of Good Paths.py
@time: 20220930
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ret = n = len(vals)
        f = list(range(n))
        count = [collections.Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v, i, j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            ret += ci * cj
            f[fj] = fi
            count[fi] = collections.Counter({v: ci + cj})
        return ret
