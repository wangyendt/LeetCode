"""
@author: wangye(Wayne)
@license: Apache Licence
@file: First Completely Painted Row or Column.py
@time: 20230506
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
import itertools
from typing import *


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [0] * m
        col = [0] * n
        res = collections.defaultdict(tuple)
        for i, j in itertools.product(range(m), range(n)):
            res[mat[i][j]] = (i, j)
        for i, a in enumerate(arr):
            r, c = res[a]
            row[r] += 1
            col[c] += 1
            if row[r] == n or col[c] == m:
                return i


so = Solution()
print(so.firstCompleteIndex([1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]]))
