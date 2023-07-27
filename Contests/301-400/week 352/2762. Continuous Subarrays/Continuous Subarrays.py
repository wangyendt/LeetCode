"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Continuous Subarrays.py
@time: 20230718
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = ret = 0
        cnt = collections.defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ret += right - left + 1
        return ret
