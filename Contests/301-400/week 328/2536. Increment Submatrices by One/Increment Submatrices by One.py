"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Increment Submatrices by One.py
@time: 20230115
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import numpy as np


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = np.zeros((n, n), dtype=int)
        for q1, q2, q3, q4 in queries:
            mat[q1:q3 + 1, q2:q4 + 1] += 1
        return mat.tolist()


so = Solution()
print(so.rangeAddQueries(n=3, queries=[[1, 1, 2, 2], [0, 0, 1, 1]]))
print(so.rangeAddQueries(n=2, queries=[[0, 0, 1, 1]]))
print(so.rangeAddQueries(n=500, queries=[[0, 0, 499, 499] for _ in range(10000)]))
