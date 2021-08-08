#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Product of the Length of Two Palindromic Substrings.py 
@time: 2021/08/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import itertools


class Solution:
    def maxProduct(self, s):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z[2:-2:2]

        n = len(s)
        man = manachers(s)
        ints = [(i - man[i] // 2, i + man[i] // 2) for i in range(n)]

        arr1 = [0] * n
        for a, b in ints:
            arr1[b] = max(arr1[b], b - a + 1)

        for i in range(n - 2, -1, -1):
            arr1[i] = max(arr1[i], arr1[i + 1] - 2)

        arr2 = [0] * n
        for a, b in ints:
            arr2[a] = max(arr2[a], b - a + 1)

        for i in range(1, n):
            arr2[i] = max(arr2[i], arr2[i - 1] - 2)

        t1 = list(itertools.accumulate(arr1, max))
        t2 = list(itertools.accumulate(arr2[::-1][:-1], max))[::-1] + [0]
        return max(x * y for x, y in zip(t1, t2))
