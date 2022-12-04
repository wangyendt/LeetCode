"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Divide Nodes Into the Maximum Number of Groups.py
@time: 20221204
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        components = []
        seen = set()
        for i in range(1, n + 1):
            if i in seen:
                continue
            queue = collections.deque([i])
            visited = set([i])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in visited:
                            continue
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(visited)
            seen = seen.union(visited)
        longest = [-1] * len(components)
        for k in range(len(components)):
            for i in components[k]:
                longest[k] = max(longest[k], self.bfs(graph, i))
        if min(longest) < 0:
            return -1
        return sum(longest)

    def bfs(self, graph, i):
        queue = collections.deque([i])
        seen = set([i])
        seenLevel = set()
        ans = 0
        while queue:
            ans += 1
            nextLevel = set()
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in seenLevel:
                        return -1
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    nextLevel.add(neighbor)
                    queue.append(neighbor)
            seenLevel = nextLevel
        return ans


so = Solution()
print(so.magnificentSets(n=6, edges=[[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]))
