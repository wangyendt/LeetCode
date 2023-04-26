"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Sliding Subarray Beauty.py
@time: 20230425
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq, ans, j = [0] * 51, [], 0

        for i in range(len(nums)):
            # count freq of negative numbers in current sliding windows
            if nums[i] < 0: freq[abs(nums[i])] += 1
            if i - j + 1 >= k:
                cnt = 0
                # calculate xth smallest number in current sliding windows
                for L in reversed(range(51)):
                    cnt += freq[L]
                    if cnt >= x:
                        ans.append(-L)
                        break
                # No xth smallest number present
                if cnt < x: ans.append(0)
                if nums[j] < 0: freq[abs(nums[j])] -= 1
                j += 1

        return ans
