#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Minimum and Maximum Number of Nodes Between Critical Points.py 
@time: 2021/10/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        if len(res) <= 2: return [-1, -1]
        tmp = []
        for i, r in enumerate(res):
            if 0 < i < len(res) - 1:
                if res[i - 1] < res[i] > res[i + 1] or res[i - 1] > res[i] < res[i + 1]:
                    tmp.append(i)
        if len(tmp) < 2: return [-1, -1]
        diff = [tmp[i] - tmp[i - 1] for i in range(1, len(tmp))]
        return [min(diff), tmp[-1] - tmp[0]]
