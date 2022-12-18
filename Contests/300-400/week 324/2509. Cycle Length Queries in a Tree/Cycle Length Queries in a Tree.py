"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Cycle Length Queries in a Tree.py
@time: 20221218
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import math
import functools


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        @functools.lru_cache(None)
        def find_log(m):
            return int(math.log2(m))

        # for i in range(1, 9):
        #     print(find_log(i))
        ret = []
        for q1, q2 in queries:
            res = 1
            while True:
                l1, l2 = find_log(q1), find_log(q2)
                if l1 < l2:
                    q1, q2 = q2, q1
                if l1 == l2:
                    if q1 != q2:
                        q1 //= 2
                        q2 //= 2
                        res += 2
                    else:
                        break
                else:
                    q1 //= 2
                    res += 1
            ret.append(res)

        return ret


so = Solution()
print(so.cycleLengthQueries(n=3, queries=[[5, 3], [4, 7], [2, 3]]))
