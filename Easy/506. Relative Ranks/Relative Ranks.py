# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 11:26
# software: PyCharm

class Solution:
    def findRelativeRanks(self, nums: list) -> list:
        rank = sorted(range(len(nums)), key=lambda x: nums[x], reverse=True)
        print(rank)
        ret = ['' for _ in range(len(nums))]
        for ri, r in enumerate(rank):
            if ri == 0:
                ret[r] = 'Gold Medal'
            elif ri == 1:
                ret[r] = 'Silver Medal'
            elif ri == 2:
                ret[r] = 'Bronze Medal'
            else:
                ret[r] = str(ri + 1)
        return ret


so = Solution()
print(so.findRelativeRanks([5, 4, 4, 6, 3, 2, 1]))
print(so.findRelativeRanks([10, 3, 8, 9, 4]))
