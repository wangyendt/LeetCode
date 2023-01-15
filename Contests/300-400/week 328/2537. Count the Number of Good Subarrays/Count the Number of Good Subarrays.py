"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count the Number of Good Subarrays.py
@time: 20230115
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
from typing import *


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = 0
        ret = 0
        cur = 0
        cnter = collections.defaultdict(int)
        for l in range(n):
            while cur < k:
                r += 1
                if r <= n:
                    cur += cnter[nums[r - 1]]
                    cnter[nums[r - 1]] += 1
                else:
                    break
            ret += (n - r + 1) if r <= n else 0
            cur -= cnter[nums[l]] - 1
            cnter[nums[l]] -= 1
        return ret


so = Solution()
print(so.countGood(nums=[1, 1, 1, 1, 1], k=10))
