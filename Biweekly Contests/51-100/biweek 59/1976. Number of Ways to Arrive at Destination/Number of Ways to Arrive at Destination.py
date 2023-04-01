#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Arrive at Destination.py 
@time: 2021/08/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        inf = float('inf')
        g = [[inf for _ in range(n)] for _ in range(n)]
        for v1, v2, d in roads:
            g[v1][v2] = d
            g[v2][v1] = d
        source_node = 0
        dis_list = g[source_node]
        node_nums = n
        visited = [0 for _ in range(node_nums)]
        visited[source_node] = 1
        counts = [1] * n
        for i in range(node_nums - 1):
            min_dis = inf
            # 选择距离最近的那个节点
            for j in range(node_nums):
                if visited[j] == 0 and dis_list[j] < min_dis:
                    min_dis = dis_list[j]
                    w = j
            visited[w] = 1
            # update
            for v in range(node_nums):
                if visited[v] == 0 and g[w][v] < inf:
                    if dis_list[v] > dis_list[w] + g[w][v]:
                        dis_list[v] = dis_list[w] + g[w][v]
                        counts[v] = counts[w]
                    elif dis_list[v] == dis_list[w] + g[w][v]:
                        counts[v] += counts[w]
        #     print("dis_list", dis_list, visited)
        # print(counts)
        return counts[-1]


so = Solution()
print(so.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                                [0, 4, 5], [4, 6, 2]]))
# v = [0] * n
# path = [0] * n
# cost = [0] * n
# for i in range(n):
#     if i == 0:
#         v[i] = 1
#     else:
#         cost[i] = g[i][i]
#         path[i] = (i if cost[i] < inf else -1)
# for i in range(1, n):
#     min_c = inf
#     cur = -1
#     for w in range(n):
#         if v[w] == 0 and cost[w] < min_c:
#             min_c = cost[w]
#             cur = w
#     if cur == -1: break
#     v[cur] = 1
#     for w in range(n):
#         if v[w] == 0 and (g[cur][w] + cost[cur] < cost[w]):
#             cost[w] = g[cur][w] + cost[cur]
#             path[w] = cur
# return path

# g = collections.defaultdict(list)
# for v1,v2,d  in roads:
#     g[v1].append((v2,d))
#     g[v2].append((v1,d))
# seen = set()
# no_seen = set()
# for i in range(n):
#     if i != 0:
#         no_seen.add(i)
# inf = float('inf')
# dp = [inf] * n
# counts  = [1] *n
# minh = [0]
# seen.add(0)
# while True:
#     if not no_seen:
#         break
#     m = min(dp[i] for i in no_seen)
#
