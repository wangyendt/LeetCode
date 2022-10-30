# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Number of Achievable Transfer Requests.py
@time: 2020/09/27
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections
import itertools


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(arr: List[List[int]]) -> bool:
            n_in, n_out = collections.defaultdict(int), collections.defaultdict(int)
            for a1, a2 in arr:
                n_out[a1] += 1
                n_in[a2] += 1
            for key in range(n):
                if n_in[key] != n_out[key]:
                    return False
            return True

        m = len(requests)
        for i in range(1, m + 1)[::-1]:
            for a in itertools.combinations(requests, i):
                if check(a):
                    return i
        return 0


so = Solution()
print(so.maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]))
print(so.maximumRequests(n=4, requests=[[0, 3], [3, 1], [1, 2], [2, 0]]))
print(so.maximumRequests(3, [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]))
