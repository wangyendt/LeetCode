# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 21:47
# software: PyCharm


import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list(list())) -> str:
        """
        O(vlogv)
        O(v)
        graph, dfs to find connected nodes
        sort the nodes and index, assign them back to s
        """
        n = len(s)
        graph = collections.defaultdict(set)
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)  # since it undirected, so build relation for both char

        visited = set()
        res = list(s)

        def dfs(i, tmp_chars):
            visited.add(i)
            tmp_chars.append(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j, tmp_chars)

        for i in range(n):
            if i not in visited:
                # build connected nodes
                chars_idxs = []
                dfs(i, chars_idxs)
                chars_idxs.sort()

                chars = [s[c] for c in chars_idxs]
                chars.sort()

                # assign to correct position by the sorted available index
                for j in range(len(chars_idxs)):
                    res[chars_idxs[j]] = chars[j]

        return ''.join(res)

    def smallestStringWithSwaps2(self, s: str, pairs: list(list())) -> str:
        def find(i):
            if i != uf[i]:
                uf[i] = find(uf[i])
            return uf[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                uf[root_i] = root_j

        n = len(s)
        uf = [i for i in range(n)]

        for i, j in pairs:
            union(i, j)

        group = collections.defaultdict(list)
        for i in range(n):
            group[find(i)].append(i)

        # 3: [0, 3]
        # 2: [1, 2]
        chars = collections.defaultdict(list)
        for i in range(n):
            chars[find(i)].append(s[i])

        res = []
        for k in chars:  # sorted the char group
            chars[k].sort(reverse=True)

        for i in range(len(s)):
            res.append(chars[find(i)].pop())

        return ''.join(res)


so = Solution()
print(so.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
