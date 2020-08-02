#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find the Winner of an Array Game
@time: 2020/08/03 03:49
"""

import collections


class Solution:
    def getWinner(self, arr: list, k: int) -> int:
        def find_m_slide_max(A: list, m: int):
            max_queue = collections.deque()
            ret = []
            for i, a in enumerate(A):
                while max_queue and a >= A[max_queue[-1]]: max_queue.pop()
                max_queue.append(i)
                if i - max_queue[0] >= m: max_queue.popleft()
                ret.append(A[max_queue[0]])
            return ret

        n = len(arr)
        assert n >= 2
        if k == 1: return max(arr[0], arr[1])
        if k >= n - 1: return max(arr)
        if arr[0] > max(arr[1:k + 1]): return arr[0]
        res = find_m_slide_max(arr[::-1], k - 1)[::-1]
        for i in range(1, n):
            if i + 1 <= len(res) - 1 and arr[i] > res[i + 1]:
                return arr[i]
        return max(arr)


so = Solution()
print(so.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2))
print(so.getWinner(arr=[3, 2, 1], k=10))
print(so.getWinner(arr=[1, 9, 8, 2, 3, 7, 6, 4, 5], k=7))
print(so.getWinner(arr=[1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000))
