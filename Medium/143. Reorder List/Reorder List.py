#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reorder List
@time: 2019/8/22 17:08
"""

import sys

sys.path.append('..')
from Tools.LinkedList import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = pre = None

        while p:
            p.next, pre, p = pre, p, p.next

        p = head
        while pre:
            p.next, pre.next, p, pre = pre, p.next, p.next, pre.next


so = Solution()
ln = LinkedList()
ln.append_list([1, 2, 3, 4, 5])
ln.print_list()
so.reorderList(ln.head)
ln.print_list()
