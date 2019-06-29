#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: The Earliest Moment When Everyone Become Friends.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def earliestAcq(self, logs: list(list()), N: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])
        rootDict = {k: v for k, v in enumerate(range(N))}

        def connect(p, q, root, n):
            if p > q:
                p, q = q, p
            if root[q] != root[p]:
                qInd = root[q]
                for k, v in root.items():
                    if v == qInd:
                        root[k] = root[p]
                n -= 1
            return n

        m = N
        for l in logs:
            m = connect(l[1], l[2], rootDict, m)
            print(l, rootDict, m)
            if m == 1:
                return l[0]
        return -1


so = Solution()
print(so.earliestAcq(
    logs=[[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3],
          [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
          [20190312, 1, 2], [20190322, 4, 5]], N=6
))
