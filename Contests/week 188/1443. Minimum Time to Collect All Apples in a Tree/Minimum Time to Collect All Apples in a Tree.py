#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/11 1:09
@Author:  wang121ye
@File: Minimum Time to Collect All Apples in a Tree.py
@Software: PyCharm
"""

import collections


class Solution:
    def minTime(self, n: int, edges: list(list()), hasApple: list) -> int:
        tree = collections.defaultdict(list)
        for u, v in edges:
            tree[u].append(v)

        def helper(node):
            if node not in tree:
                return hasApple[node], 0
            cur, apple_found = 0, hasApple[node]
            for child in tree[node]:
                found, dist = helper(child)
                cur += 2 + dist if found else 0
                apple_found |= found
            return apple_found, cur

        return helper(0)[1]


so = Solution()
print(so.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                 hasApple=[False, False, True, False, True, True, False]))
print(so.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                 hasApple=[False, False, True, False, False, True, False]))
print(so.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                 hasApple=[False, False, False, False, False, False, False]))
