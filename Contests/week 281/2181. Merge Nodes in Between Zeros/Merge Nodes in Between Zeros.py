#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Merge Nodes in Between Zeros.py 
@time: 2022/02/20
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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        stack = []
        ret = []
        for r in res:
            if r == 0:
                if stack:
                    ret.append(sum(stack))
                stack.clear()
            else:
                stack.append(r)
        ret_q = ret_h = ListNode(0)
        for r in ret:
            ret_h.next = ListNode(r)
            ret_h = ret_h.next
        return ret_q.next
