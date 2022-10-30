#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Process Tasks Using Servers.py 
@time: 2021/05/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n, m = len(servers), len(tasks)
        ret = []
        server_heap = []
        task_heap = []
        for i, s in enumerate(servers):
            heapq.heappush(server_heap, (s, i))
        cur_time = 0
        for i, t in enumerate(tasks):
            cur_time = max(cur_time, i)
            while task_heap:
                end_time, s, si = task_heap[0]
                if end_time <= cur_time:
                    heapq.heappush(server_heap, (s, si))
                    heapq.heappop(task_heap)
                else:
                    break
            if not server_heap:
                end_time, s, si = task_heap[0]
                cur_time = end_time
                heapq.heappush(server_heap, (s, si))
                heapq.heappop(task_heap)
            s, si = server_heap[0]
            heapq.heappop(server_heap)
            end_time = t + cur_time
            heapq.heappush(task_heap, (end_time, s, si))
            ret.append(si)
            # print(server_heap)
        return ret


so = Solution()
print(so.assignTasks(servers=[3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]))
