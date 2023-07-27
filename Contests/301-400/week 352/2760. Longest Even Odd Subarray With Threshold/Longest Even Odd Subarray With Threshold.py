"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Longest Even Odd Subarray With Threshold.py
@time: 20230718
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ret = 0
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                sub_array = nums[l:r + 1]
                # print(sub_array)
                prev = 1
                for n in sub_array:
                    if n % 2 == prev % 2 or n > threshold:
                        break
                    prev = n
                else:
                    ret = max(ret, len(sub_array))
        return ret


so = Solution()
print(so.longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5))
