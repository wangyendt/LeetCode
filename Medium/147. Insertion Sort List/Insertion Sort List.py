#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Insertion Sort List
@time: 2019/8/22 18:19
"""

import sys

sys.path.append('..')
from Tools.LinkedList import *


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        has = ListNode(0)
        new_head = has

        while head:
            while has.next and head.val > has.next.val:
                has = has.next
            nex = head.next
            head.next = has.next
            has.next = head
            head = nex
            has = new_head

        return new_head.next


so = Solution()
linked_list = LinkedList()
linked_list.append_list([4, 2, 1, 3])
linked_list.print_list()
ln = linked_list.head
LinkedList.print_list_node(so.insertionSortList(ln))
