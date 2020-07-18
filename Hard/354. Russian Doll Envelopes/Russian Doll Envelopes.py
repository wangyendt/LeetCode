#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Russian Doll Envelopes
@time: 2020/07/18 14:04
"""

import bisect


class Solution:
    def maxEnvelopes(self, A: list(list())) -> int:
        # A -- envelopes
        def lis(seq: list) -> int:
            if not seq: return 0
            stack = []
            for s in seq:
                ind = bisect.bisect_left(stack, s)
                if ind >= len(stack) or not stack:
                    stack.append(s)
                else:
                    stack[ind] = s
            return len(stack)

        A = sorted(A, key=lambda x: (x[0], -x[1]))
        h = [a[1] for a in A]
        return lis(h)


so = Solution()
# print(so.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
# print(so.maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]))
print(so.maxEnvelopes([[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]))
