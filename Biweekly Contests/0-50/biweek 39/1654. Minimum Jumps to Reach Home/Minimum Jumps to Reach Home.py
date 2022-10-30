#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Jumps to Reach Home.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import collections


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_val = max([x] + forbidden) + a + b

        jumps = [0] + [float('inf')] * max_val
        for pos in forbidden: jumps[pos] = -1
        queue = collections.deque([0])

        while queue:
            pos = queue.popleft()
            if pos + a <= max_val and jumps[pos + a] > jumps[pos] + 1:
                queue.append(pos + a)
                jumps[pos + a] = jumps[pos] + 1
            if pos - b > 0 and jumps[pos - b] > jumps[pos] + 1:
                jumps[pos - b] = jumps[pos] + 1
                if pos - b + a <= max_val and jumps[pos - b + a] > jumps[pos] + 2:
                    queue.append(pos - b + a)
                    jumps[pos - b + a] = jumps[pos] + 2

        return jumps[x] if jumps[x] < float('inf') else -1
