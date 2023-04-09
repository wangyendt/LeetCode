"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Merge Two 2D Arrays by Summing Values.py
@time: 20230331
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
from typing import *


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = collections.defaultdict(int)
        for idx, num in nums1 + nums2:
            res[idx] += num
        return list(sorted(list(res.items())))


so = Solution()
print(so.mergeArrays(nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]))
