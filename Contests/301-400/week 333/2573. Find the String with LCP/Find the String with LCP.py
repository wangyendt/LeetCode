"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the String with LCP.py
@time: 20230409
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        A = [0] * n
        c = 1
        for i in range(n):
            if A[i]: continue
            if c > 26: return ''
            for j in range(i, n):
                if lcp[i][j]:
                    A[j] = c
            c += 1
        for i in range(n):
            for j in range(n):
                v = lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                v = v + 1 if A[i] == A[j] else 0
                if lcp[i][j] != v:
                    return ''
        return ''.join(chr(ord('a') + i - 1) for i in A)
