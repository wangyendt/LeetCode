#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 18:37
@Author:  wang121ye
@File: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.py
@Software: PyCharm
"""


class Solution:
    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i