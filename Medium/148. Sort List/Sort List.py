#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sort List
@time: 2019/8/22 22:31
"""

import sys

sys.path.append('..')
from Tools.LinkedList import *


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        p = q = ListNode(0)
        while arr:
            q.next = ListNode(arr.pop(0))
            q = q.next
        return p.next


ln = LinkedList()
ln.append_list([4, 2, 1, 3])
so = Solution()
res = so.sortList(ln.head)
LinkedList.print_list_node(res)
