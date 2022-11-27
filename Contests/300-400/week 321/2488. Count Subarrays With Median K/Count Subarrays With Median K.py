"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count Subarrays With Median K.py
@time: 20221127
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum_of_balance = Counter([0])  # Dummy value of 0's frequency if 1.
        running_balance = ans = 0
        found = False
        for num in nums:
            if num < k:
                running_balance -= 1
            elif num > k:
                running_balance += 1
            else:
                found = True
            if found:
                ans += prefix_sum_of_balance[running_balance] + prefix_sum_of_balance[running_balance - 1]
            else:
                prefix_sum_of_balance[running_balance] += 1
        return ans
