#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Subsequence Repeated k Times.py 
@time: 2021/09/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
import itertools


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        num = collections.Counter(s)
        hot = ''.join(ele * (num[ele] // k) for ele in sorted(num, reverse=True))
        for i in range(len(hot), 0, -1):
            for item in itertools.permutations(hot, i):
                word = ''.join(item)
                ss = iter(s)
                if all(c in ss for c in word * k):
                    return word
        return ''
