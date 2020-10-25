#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: 1632. Rank Transform of a Matrix
@time: 2020/10/25 12:13
"""

from typing import *


class UF:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}

    def find(self, i):
        if i == self.parents[i]:
            return self.parents[i]
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def merge(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        self.parents[bp] = ap


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        t = [[matrix[j][i] for j in range(m)] for i in range(n)]
        node_lookup = {}
        cur_node = 0

        def dfs(i, j, c):
            node_lookup[i, j] = c

        for i in range(m):
            for j in range(n):
                if (i, j) not in node_lookup:
                    dfs(i, j, cur_node)
                    cur_node += 1

        uf = UF(cur_node)

        for i in range(m):
            row = {}
            for j in range(n):
                if matrix[i][j] in row:
                    uf.merge(row[matrix[i][j]], node_lookup[i, j])
                    # merged[node_lookup[i,j]] = row[matrix[i][j]]
                    # node_lookup[i,j] = row[matrix[i][j]]
                else:
                    row[matrix[i][j]] = node_lookup[i, j]

        for j in range(n):
            col = {}
            for i in range(m):
                if matrix[i][j] in col:
                    uf.merge(col[matrix[i][j]], node_lookup[i, j])
                    # merged[node_lookup[i,j]] = col[matrix[i][j]]
                    # node_lookup[i,j] = col[matrix[i][j]]
                else:
                    col[matrix[i][j]] = node_lookup[i, j]

        for i in range(m):
            for j in range(n):
                node_lookup[i, j] = uf.find(node_lookup[i, j])

        graph = defaultdict(list)

        def add_edge(p, d):
            graph[p].append(d)

        for i in range(m):
            row = matrix[i][:]
            idxs = sorted(range(n), key=lambda idx: row[idx])
            prev = 0
            cur = 0
            while cur < len(idxs):
                while cur < len(idxs) and row[idxs[cur]] == row[idxs[prev]]:
                    cur += 1
                if cur >= len(idxs):
                    break
                # add edge from prev to cur
                add_edge(node_lookup[i, idxs[prev]], node_lookup[i, idxs[cur]])
                prev = cur

        for j in range(n):
            col = t[j][:]
            idxs = sorted(range(m), key=lambda idx: col[idx])
            prev = 0
            cur = 0
            while cur < len(idxs):
                while cur < len(idxs) and col[idxs[cur]] == col[idxs[prev]]:
                    cur += 1
                if cur >= len(idxs):
                    break
                # add edge from prev to cur
                add_edge(node_lookup[idxs[prev], j], node_lookup[idxs[cur], j])
                prev = cur

        seen = set()
        r = []

        # now toposort
        def visit(v):
            if v in seen:
                return
            for nv in graph[v]:
                visit(nv)
            seen.add(v)
            r.append(v)

        for v in node_lookup.values():
            if v not in seen:
                visit(v)

        r = r[::-1]

        graph_r = defaultdict(list)
        for v in graph:
            for nv in graph[v]:
                graph_r[nv].append(v)

        values = {}
        for v in r:
            cv = max([0] + [values[pv] for pv in graph_r[v]]) + 1
            values[v] = cv

        out = [[values[node_lookup[i, j]] for j in range(n)] for i in range(m)]
        return out
