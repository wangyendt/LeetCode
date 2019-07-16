# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 10:12
# software: PyCharm

class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        ret = []
        for n in nums1:
            i = nums2.index(n)
            for j in range(i + 1, len(nums2)):
                if nums2[j] > n:
                    ret.append(nums2[j])
                    break
            else:
                ret.append(-1)
        return ret


so = Solution()
print(so.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
