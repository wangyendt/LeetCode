#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Maximum Equal Frequency.py 
@time: 2019/10/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def maxEqualFreq(self, nums: list) -> int:
        cnt = collections.Counter(nums)
        ret = len(cnt)
        s = n = len(nums)
        if n == 1:
            return 1
        for i in range(n - 1, 0, -1):
            if (s - 1) % ret == 0:
                k = (s - 1) // ret
                if all(x == k or x == k + 1 for x in cnt.values()):
                    return i + 1
            if ret != 1 and (s - 1) % (ret - 1) == 0:
                k = (s - 1) // (ret - 1)
                if all(x == k or x == 1 for x in cnt.values()):
                    return i + 1
            num = nums[i]
            s -= 1
            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]
                ret -= 1
        return 1


so = Solution()
print(so.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5]), 7)
print(so.maxEqualFreq([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]), 13)
print(so.maxEqualFreq([1, 1, 1, 2, 2, 2]), 5)
print(so.maxEqualFreq([10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]), 8)
print(so.maxEqualFreq([1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 1, 2, 3, 5, 6]), 13)
print(so.maxEqualFreq(
    [1, 1, 2, 2, 3, 3, 3, 4, 4, 75, 20, 67, 37, 24, 33, 71, 1, 91, 60, 65, 53, 70, 96, 77, 52, 4, 57, 51, 8, 63, 79, 57,
     26, 99, 80, 24, 39, 89, 70, 73, 70, 92, 56, 52, 45, 39, 6, 45, 41, 94, 55, 92, 24, 21, 76, 25, 28, 58, 53, 35, 95,
     98, 94, 85, 35, 60, 25, 85, 29, 66, 25, 38, 22, 77, 54, 85, 100, 65, 30, 7, 8, 49, 66, 38, 79, 4, 99, 49, 63, 63,
     69, 82, 43, 38, 83, 11, 56, 85, 25, 38, 61, 40, 36, 67, 84]))
