"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Handling Sum Queries After Update.py
@time: 20230330
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        l = len(nums1)
        init = 1 << l
        nums1 = int("".join(map(str, nums1)), 2)
        cur = sum(nums2)
        ans = []
        for f, s, t in queries:
            if f == 1:
                a = (init >> s) - 1
                b = (init >> (t + 1)) - 1
                nums1 = nums1 ^ a ^ b
            elif f == 2:
                cnt = nums1.bit_count()
                cur += s * cnt
            else:
                ans.append(cur)
        return ans
