#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Move Pieces to Obtain a String.py 
@time: 2022/07/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        res_start, res_target = [], []
        for s in start:
            if s in 'LR':
                res_start.append(s)
        for t in target:
            if t in 'LR':
                res_target.append(t)
        if res_start != res_target:
            return False

        cnt_start = collections.defaultdict(dict)
        num_l, num_r = 0, 0
        for i, s in enumerate(start):
            if s == 'L':
                cnt_start[s].update({num_l: i})
                num_l += 1
            elif s == 'R':
                cnt_start[s].update({num_r: i})
                num_r += 1

        cnt_end = collections.defaultdict(dict)
        num_l, num_r = 0, 0
        for i, s in enumerate(target):
            if s == 'L':
                cnt_end[s].update({num_l: i})
                num_l += 1
            elif s == 'R':
                cnt_end[s].update({num_r: i})
                num_r += 1

        for (k1, v1), (k2, v2) in zip(cnt_start['L'].items(), cnt_end['L'].items()):
            if v1 < v2:
                return False
        for (k1, v1), (k2, v2) in zip(cnt_start['R'].items(), cnt_end['R'].items()):
            if v1 > v2:
                return False
        return True


so = Solution()
print(so.canChange(start="_L__R__R_", target="L______RR"))
