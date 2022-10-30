#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Reverse Nodes in Even Length Groups.py 
@time: 2021/11/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        k = 1
        groups = collections.defaultdict(list)
        cur = 0
        while cur < len(res):
            groups[k] = res[cur:cur + k]
            cur = cur + k
            k += 1
        ret = []
        for k, v in groups.items():
            tmp = v[:]
            if len(v) % 2 == 0:
                tmp = tmp[::-1]
            ret.extend(tmp)
        p = ret_h = ListNode(0)
        for r in ret:
            ret_h.next = ListNode(r)
            ret_h = ret_h.next
        return p.next
