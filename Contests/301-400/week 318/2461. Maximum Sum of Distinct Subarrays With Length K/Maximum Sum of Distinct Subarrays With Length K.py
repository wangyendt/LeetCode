#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Sum of Distinct Subarrays With Length K.py 
@time: 2022/11/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = collections.defaultdict(int)
        bad_cnt = 0
        ret = 0
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            cnt[num] += 1
            if cnt[num] > 1:
                bad_cnt += 1
            if i >= k:
                cur -= nums[i - k]
                if cnt[nums[i - k]] > 1:
                    bad_cnt -= 1
                cnt[nums[i - k]] -= 1

            if i >= k-1:
                if bad_cnt == 0:
                    ret = max(ret, cur)
        return ret


so = Solution()
print(so.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
print(so.maximumSubarraySum(nums=[4, 4, 4], k=3))
print(so.maximumSubarraySum([9, 9, 9, 1, 2, 3], 3))
