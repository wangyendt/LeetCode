"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Reconstruct Itinerary.py
@time: 20230614
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(list)
        for ts, te in tickets:
            g[ts].append(te)
        for k, v in g.items():
            g[k].sort()
        stack = ['JFK']
        circuit = []
        while stack:
            cur = stack[-1]
            if cur not in g or not g[cur]:
                circuit.append(stack.pop())
            else:
                stack.append(g[cur].pop(0))
        return circuit[::-1]


so = Solution()
print(so.findItinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
