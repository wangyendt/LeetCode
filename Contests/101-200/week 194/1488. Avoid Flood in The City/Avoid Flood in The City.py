#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Avoid Flood in The City
@time: 2020/06/21 10:52
"""

import collections
import heapq


class Solution:
    def avoidFlood(self, rains: list) -> list:
        ret = []
        ele_last_ind = collections.defaultdict(int)
        res = collections.defaultdict(int)
        for i, r in enumerate(rains):
            if not r: continue
            if r not in ele_last_ind:
                res[i] = -1
            else:
                res[ele_last_ind[r]] = i
            ele_last_ind[r] = i
        h = []
        stack = set()
        for i, r in enumerate(rains):
            if r:
                if r in stack: return []
                ret.append(-1)
                if r in res and res[r] == -1:
                    pass
                else:
                    if res[i] and res[i] != -1:
                        heapq.heappush(h, (res[i], {r: res[i]}))
                stack.add(r)
            else:
                if h:
                    a = heapq.heappop(h)
                    k = a[1].popitem()[0]
                    stack.remove(k)
                    ret.append(k)
                else:
                    ret.append(1)
        return ret


# h = []
# heapq.heappush(h,{1:2})
# heapq.heappush(h,{2:4},)
# print(h)
so = Solution()
# print(so.avoidFlood(rains=[1, 2, 3, 4]))
# print(so.avoidFlood(rains=[1, 2, 0, 0, 2, 1]))
# print(so.avoidFlood(rains=[1, 2, 0, 1, 2]))
# print(so.avoidFlood(rains=[69, 0, 0, 0, 69]))
# print(so.avoidFlood(rains=[10, 20, 20]))
print(so.avoidFlood([1,2,0,2,3,0,1]))