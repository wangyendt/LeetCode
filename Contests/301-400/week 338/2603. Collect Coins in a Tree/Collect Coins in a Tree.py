"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Collect Coins in a Tree.py
@time: 20230512
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        if not edges:
            return 0

        n, g = len(coins), collections.defaultdict(set)

        for i, j in edges:
            g[i].add(j)
            g[j].add(i)

        leaves = [i for i in g if len(g[i]) == 1]

        for u in leaves:
            while len(g[u]) == 1 and coins[u] == 0:
                p = g[u].pop()
                del g[u]
                g[p].remove(u)
                u = p

        for _ in range(2):
            leaves = [i for i in g if len(g[i]) == 1]
            for u in leaves:
                p = g[u].pop()
                del g[u]
                g[p].remove(u)
                if len(g) < 2:
                    return 0

        return 2 * (len(g) - 1)
