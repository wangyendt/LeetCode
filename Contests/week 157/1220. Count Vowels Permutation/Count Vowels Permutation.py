#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Vowels Permutation
@time: 2019/10/8 11:47
"""

import collections


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prevs = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for i in range(1, n):
            cur = collections.defaultdict(int)
            for prev, count in prevs.items():
                if prev == 'a':
                    cur['e'] += count
                elif prev == 'e':
                    for nextch in ['a', 'i']:
                        cur[nextch] += count
                elif prev == 'i':
                    for nextch in ['a', 'e', 'o', 'u']:
                        cur[nextch] += count
                elif prev == 'o':
                    for nextch in ['i', 'u']:
                        cur[nextch] += count
                elif prev == 'u':
                    cur['a'] += count
            prevs = cur
        return sum(prevs.values()) % 1000000007
