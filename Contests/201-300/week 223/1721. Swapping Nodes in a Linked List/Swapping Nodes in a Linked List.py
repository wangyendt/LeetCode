#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Swapping Nodes in a Linked List.py 
@time: 2021/01/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import sys

sys.path.append('../../..')
from Tools.LinkedList import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res[k] = res[k] + res[~k]
        res[~k] = res[k] - res[~k]
        res[k] = res[k] - res[~k]
        ret = ListNode(0)
        for r in res:
            ret.next = ListNode(r)
        return ret.next


h = [1, 2]
k = 1

l = LinkedList()
l.append_list(h)
l.print_list()
so = Solution()
print(so.swapNodes(l.head, k))
