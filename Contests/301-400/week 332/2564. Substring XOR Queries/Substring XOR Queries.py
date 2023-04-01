"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Substring XOR Queries.py
@time: 20230224
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
from typing import *


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        query_set = set()
        res = collections.defaultdict(list)
        for i, (q1, q2) in enumerate(queries):
            query_set.add(q1 ^ q2)
            res[q1 ^ q2].append(i)

        seen = set()
        seen_zero = False
        ret = [[-1, -1]] * len(queries)
        for i in range(len(s)):
            if s[i] == '0' and not seen_zero:
                seen_zero = True
                for k in res[0]:
                    ret[k] = [i, i]
            for j in range(max(0, i - 30), i + 1):
                if '0' == s[j]: continue
                cur = int(s[j:i + 1], 2)
                if cur in seen:
                    continue
                seen.add(cur)
                for k in res[cur]:
                    ret[k] = [j, i]
                # print(i, j, cur)
        return ret


so = Solution()
print(so.substringXorQueries(s="101101", queries=[[0, 5], [1, 2]]))
print(so.substringXorQueries(s="111010110", queries=[[4, 2], [3, 3], [6, 4], [9, 9], [10, 28], [0, 470], [5, 83], [10, 28], [8, 15], [6, 464], [0, 3], [5, 8], [7, 7], [8, 8], [6, 208], [9, 15], [2, 2], [9, 95]]))
print(so.substringXorQueries("01010011000111011011100010111", [[2, 1], [10, 11], [1, 0], [6, 243473], [2, 2340629], [4, 787], [5, 3801]]))
