#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Spiral Matrix IV.py 
@time: 2022/07/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys

sys.path.append('../..')
from Tools.LinkedList import *


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        direction = 'r'
        dirs = ['r', 'd', 'l', 'u']
        res = res + [-1] * (m * n - len(res))
        ret = [[0 for _ in range(n)] for _ in range(m)]
        cur = (0, 0)
        seen = {cur}
        print(res)
        dir_next = lambda x, y: {'r': (x, y + 1), 'd': (x + 1, y), 'l': (x, y - 1), 'u': (x - 1, y)}
        direction_next = {'l': 'u', 'u': 'r', 'r': 'd', 'd': 'l'}
        for i, r in enumerate(res):
            cur_r = cur[0]
            cur_c = cur[1]
            ret[cur_r][cur_c] = r
            seen.add((cur_r, cur_c))
            cur_next = dir_next(cur_r, cur_c)[direction]
            if not (0 <= cur_next[0] < m and 0 <= cur_next[1] < n and (cur_next[0], cur_next[1]) not in seen):
                direction = direction_next[direction]
                cur_next = dir_next(cur_r, cur_c)[direction]
            cur = cur_next
        return ret
