#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Merge In Between Linked Lists
@time: 2020/11/28 22:41
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1 = []
        l2 = []
        h = list1
        while h:
            l1.append(h.val)
            h = h.next
        h = list2
        while h:
            l2.append(h.val)
            h = h.next
        l1[a:b + 1] = l2

        def list2link(list_):
            head = ListNode(list_[0])
            p = head
            for i in range(1, len(list_)):
                p.next = ListNode(list_[i])
                p = p.next
            return head

        return list2link(l1)
