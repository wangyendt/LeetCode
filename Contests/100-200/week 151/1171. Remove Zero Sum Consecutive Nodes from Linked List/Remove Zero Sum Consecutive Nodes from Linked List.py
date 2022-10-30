# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 16:01
# software: PyCharm


import sys

sys.path.append('..')
from Tools.LinkedList import *


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        p = head
        stack = []
        while p:
            if p.val == 0:
                if stack:
                    prev = stack[-1][0]
                    prev.next = p.next
                else:
                    head.next = p.next
                p = p.next
                continue
            if not stack:
                stack.append((p, p.val))
                p = p.next
            else:
                target = p.val
                for qi, (qt, q) in enumerate(stack[::-1]):
                    if q + target == 0:
                        for _ in range(qi + 1):
                            stack.pop()
                        if stack:
                            prev = stack[-1][0]
                            prev.next = p.next
                        else:
                            head = p.next
                        p = p.next
                        break
                    else:
                        target += q
                else:
                    stack.append((p, p.val))
                    p = p.next
        return head


ll = LinkedList()
# ll.append_list([1, 2, 3, -3, -2, 4])
ll.append_list([2, 0])
so = Solution()
LinkedList.print_list_node(so.removeZeroSumSublists(ll.head))
