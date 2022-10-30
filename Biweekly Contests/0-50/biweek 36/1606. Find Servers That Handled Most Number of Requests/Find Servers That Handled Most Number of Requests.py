#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Servers That Handled Most Number of Requests
@time: 2020/10/04 00:14
"""

from typing import *

from sortedcontainers import SortedList
import heapq


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        to_free = []  # heap (free_time, node) to free up the nodes quickly
        available = []  # heap (nodes) free after current server (reusable)
        next_round = list(range(k))  # for the next round, after the server frees up
        requests_handled = [0] * k

        for i, (arrvl, ld) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0:
                available = next_round
                next_round = []

            while to_free and to_free[0][0] <= arrvl:
                freed_node = heapq.heappop(to_free)[1]
                if freed_node < server_id:
                    heapq.heappush(next_round, freed_node)
                else:
                    heapq.heappush(available, freed_node)

            use_queue = available if available else next_round
            if not use_queue: continue
            using_node = heapq.heappop(use_queue)
            requests_handled[using_node] += 1
            heapq.heappush(to_free, (arrvl + ld, using_node))

        maxi = []
        maxreqs = max(requests_handled)
        for i, hnd in enumerate(requests_handled):
            if hnd == maxreqs:
                maxi.append(i)

        return maxi
