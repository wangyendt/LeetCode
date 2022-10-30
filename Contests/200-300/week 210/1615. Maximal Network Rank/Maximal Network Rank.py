#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximal Network Rank
@time: 2020/10/11 12:03
"""

from typing import *
import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        A = collections.defaultdict(set)
        cnt = collections.defaultdict(int)
        for road in roads:
            cnt[road[0]] += 1
            cnt[road[1]] += 1
            A[road[0]].add(road[1])
            A[road[1]].add(road[0])
        ret = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    cur = cnt[i] + cnt[j]
                    if j in A[i]:
                        cur -= 1
                    ret = max(ret, cur)
        return ret
