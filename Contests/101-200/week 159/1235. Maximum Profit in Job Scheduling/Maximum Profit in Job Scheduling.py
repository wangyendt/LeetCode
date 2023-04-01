# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/20 13:03
# software: PyCharm


class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        times = set(startTime)
        for t in endTime:
            times.add(t)

        timemap = {t: i for i, t in enumerate(sorted(times))}

        W = len(timemap)
        graph = [[] for _ in range(W)]
        for i in range(len(startTime)):
            s = startTime[i]
            si = timemap[s]
            e = endTime[i]
            ei = timemap[e]
            graph[ei].append((si, i))

        NINF = -(1 << 50)
        dist = [NINF for _ in range(W + 1)]
        dist[W - 1] = 0
        for ei in range(W - 1, -1, -1):
            if dist[ei + 1] > dist[ei]:
                dist[ei] = dist[ei + 1]
            for si, i in graph[ei]:
                cand = dist[ei] + profit[i]
                if cand > dist[si]:
                    dist[si] = cand
        return dist[0]
