#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Delete the Middle Node of a Linked List.py 
@time: 2021/12/05
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        p = head
        while p:
            res.append(p.val)
            p = p.next
        res[len(res) // 2:len(res) // 2 + 1] = []
        s = q = ListNode(0)
        for r in res:
            q.next = ListNode(r)
            q = q.next
        return s.next
