#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Minimum Time to Finish All Jobs.py 
@time: 2021/01/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)

        def fn(i):
            """Assign jobs to worker and find minimum time."""
            nonlocal ans
            if i == len(jobs):
                ans = max(time)
            else:
                for kk in range(k):
                    if not kk or time[kk - 1] > time[kk]:
                        time[kk] += jobs[i]
                        if max(time) < ans: fn(i + 1)
                        time[kk] -= jobs[i]

        ans = float('inf')
        time = [0] * k
        fn(0)
        return ans
