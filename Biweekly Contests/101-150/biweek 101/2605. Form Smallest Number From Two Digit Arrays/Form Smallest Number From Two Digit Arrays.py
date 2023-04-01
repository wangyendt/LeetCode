"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Form Smallest Number From Two Digit Arrays.py
@time: 20230402
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s = sorted(set(nums1) & set(nums2))
        if s: return s[0]
        return min(min(nums1) * 10 + min(nums2), min(nums1) + min(nums2) * 10)
