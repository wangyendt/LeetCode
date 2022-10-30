#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/26 20:25
@Author:  wang121ye
@File: Constrained Subset Sum.py
@Software: PyCharm
"""

import collections


class Solution:
    def constrainedSubsetSum(self, A, k):
        deque = collections.deque()
        for i in range(len(A)):
            A[i] += deque[0] if deque else 0
            while len(deque) and A[i] > deque[-1]:
                deque.pop()
            if A[i] > 0:
                deque.append(A[i])
            if i >= k and deque and deque[0] == A[i - k]:
                deque.popleft()
        return max(A)
