#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Create Maximum Number
@time: 2020/6/4 19:30
"""

import functools


class Solution:
    def maxNumber(self, nums1: list, nums2: list, k: int) -> list:
        m, n = len(nums1), len(nums2)

        def max_from_one_array(nums: list, l: int) -> list:
            ret_ = []
            if nums and l > 0:
                for d in range(10)[::-1]:
                    if d in nums and nums.index(d) + l <= len(nums):
                        ret_ = [d] + max_from_one_array(nums[nums.index(d) + 1:], l - 1)
                        break
            return ret_

        def merge(arr1: list, arr2: list) -> tuple:
            ret_ = [max(arr1, arr2).pop(0) for _ in arr1 + arr2]
            return functools.reduce(lambda x, y: 10 * x + y, ret_), ret_

        res, ret = 0, None
        for i in range(k + 1):
            j = k - i
            if i > m or j > n:
                continue
            max1 = max_from_one_array(nums1, i)
            max2 = max_from_one_array(nums2, j)
            # print(i, j, nums1, nums2, max1, max2)
            cur_res, cur_ret = merge(max1, max2)
            if res < cur_res:
                res = cur_res
                ret = cur_ret

        return ret


so = Solution()
print(so.maxNumber(nums1=[3, 4, 6, 5], nums2=[9, 1, 2, 5, 8, 3], k=5))
print(so.maxNumber(nums1=[6, 7], nums2=[6, 0, 4], k=5))
print(so.maxNumber(nums1=[3, 9], nums2=[8, 9], k=3))
