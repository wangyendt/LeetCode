"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count Zero Request Servers.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        res, cnt = [0] * len(queries), Counter()
        i, j, used = 0, 0, 0
        logs.sort(key=lambda l: l[1])
        for [t, id] in sorted([t, id] for id, t in enumerate(queries)):
            while i < len(logs) and logs[i][1] <= t:
                cnt[logs[i][0]] += 1
                used += cnt[logs[i][0]] == 1
                i += 1
            while j < i and logs[j][1] < t - x:
                cnt[logs[j][0]] -= 1
                used -= cnt[logs[j][0]] == 0
                j += 1
            res[id] = n - used
        return res
