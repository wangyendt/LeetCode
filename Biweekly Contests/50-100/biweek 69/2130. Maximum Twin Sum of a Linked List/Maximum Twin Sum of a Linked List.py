#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Twin Sum of a Linked List.py 
@time: 2022/01/08
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        ret = 0
        for i in range(len(res) // 2):
            ret = max(ret, res[i] + res[len(res) - 1 - i])
        return ret
