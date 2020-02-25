#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Number of Steps to Reduce a Number to Zero
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:36
@Desc   ：
=================================================="""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt0, cnt1 = 0, 0
        while num:
            if num % 2 == 0:
                cnt0 += 1
            else:
                cnt1 += 1
            num >>= 1
        return 2 * cnt1 + cnt0 - 1


so = Solution()
print(so.numberOfSteps(14))
print(so.numberOfSteps(8))
print(so.numberOfSteps(123))
print(so.numberOfSteps(1000000))
