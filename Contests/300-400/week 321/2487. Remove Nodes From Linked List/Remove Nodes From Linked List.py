"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Remove Nodes From Linked List.py
@time: 20221127
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        queue = collections.deque()
        for i, a in enumerate(arr):
            while queue and arr[queue[-1]] < a:
                queue.pop()
            queue.append(i)
        ret = cur = ListNode(0)
        for q in queue:
            cur.next = ListNode(arr[q])
            cur = cur.next
        return ret.next
