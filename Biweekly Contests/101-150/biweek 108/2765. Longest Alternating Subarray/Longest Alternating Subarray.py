"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Longest Alternating Subarray.py
@time: 20230804
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        stack = []
        ret = -1
        for i, n in enumerate(nums):
            if not stack:
                stack.append(n)
            elif len(stack) == 1:
                if n - stack[-1] == 1:
                    stack.append(n)
                else:
                    stack = [n]
            else:
                if (n - stack[-1] == 1 and stack[-1] - stack[-2] == -1) or (n - stack[-1] == -1 and stack[-1] - stack[-2] == 1):
                    stack.append(n)
                else:
                    if abs(n - stack[-1]) == 1:
                        stack = [stack[-1], n]
                    else:
                        stack = [n]
            if len(stack) >= 2:
                ret = max(ret, len(stack))
        return ret


so = Solution()
print(so.alternatingSubarray([21, 9, 5]))
print(so.alternatingSubarray([2, 3, 4, 3, 4]))
print(so.alternatingSubarray([31, 32, 31, 32, 33]))
print(so.alternatingSubarray([14, 30, 29, 49, 3, 23, 44, 21, 26, 52]))
