"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Difference Between Maximum and Minimum Price Sum.py
@time: 20230115
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections
import functools


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = collections.defaultdict(set)

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        @functools.lru_cache(None)
        def dfs(node, parent):

            curr_price = price[node]
            m = 0  # find the max path from current node via dfs
            for v in g[node]:
                if v == parent: continue
                m = max(m, dfs(v, node))

            return curr_price + m  # return current_price + max_price_path

        m = 0
        for node in range(n):
            max_price = dfs(node, -1)
            min_price = price[node]
            m = max(m, max_price - min_price)

        return m


so = Solution()
# print(so.maxOutput(n=6, edges=[[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]], price=[9, 8, 7, 6, 10, 5]))
print(so.maxOutput(2, [[0, 1]], [12, 12]))
