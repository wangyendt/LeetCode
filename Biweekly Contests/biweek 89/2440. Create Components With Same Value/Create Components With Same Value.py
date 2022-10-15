#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Create Components With Same Value.py 
@time: 2022/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        tree = collections.defaultdict(set)
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def check(cur, prev, target):
            val = nums[cur]
            for kid in tree[cur] - {prev}:
                i = check(kid, cur, target)
                if i == -1: return -1
                val += i
            return val % target if val <= target else -1

        tot = sum(nums)
        for n in range(min(tot // max(nums), len(nums)), 0, -1):  # for simplicity, i do not use O(n^1/2) approach to find all factors here
            if not tot % n and check(0, -1, tot // n) == 0:
                return n - 1
