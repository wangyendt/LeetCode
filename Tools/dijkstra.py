#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: dijkstra.py 
@time: 2022/03/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import heapq


def Dijkstra(graph, K, n):
    """

    refer to week 284/Minimum Weighted Subgraph With the Required Paths

    :param graph:  graph
    :param K: starting point
    :param n: number of nodes
    :return:
    """
    q, t = [(0, K)], {}
    while q:
        time, node = heapq.heappop(q)
        if node not in t:
            t[node] = time
            for v, w in graph[node]:
                heapq.heappush(q, (time + w, v))
    return [t.get(i, float("inf")) for i in range(n)]


def dijkstra2(successors, s):
    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'

    # Iterate through the V/{s}-nodes and set L[j] to infinity and P[j] to s.
    for o in range(0, n):
        if o != s:
            L[o] = float('inf')
            P[o] = s

    # Visited vector.
    visited = [False] * n

    # Heapq
    queue = [(0, s)]

    while queue:
        par_len, v = heapq.heappop(queue)
        # v is unvisited
        if visited[v] is False:
            visited[v] = True
            for w, edge_len in successors[v].items():
                # Check if the child is unvisited and compute the distance.
                if visited[w] is False and edge_len + par_len < L[w]:
                    heapq.heappush(queue, (edge_len + par_len, w))
                    L[w] = edge_len + par_len
                    P[w] = v

    return L, P
