#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Minimum Numbers of Function Calls to Make Target Array.py 
@time: 2020/08/22
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minOperations(self, nums: list) -> int:
        def num_of_ones(n: int) -> int:
            c = 0
            while n:
                c += 1
                n &= n - 1
            return c

        def log(n: int) -> int:
            c = 0
            while n:
                c += 1
                n >>= 1
            return c - 1

        m = max(nums)
        res, ret = 0, 0
        # print(num_of_ones(7), log(7))
        if m == 0: return 0
        for num in nums:
            if num == 0: continue
            res = max(res, log(num))
            ret += num_of_ones(num)
        return ret + res


so = Solution()
print(so.minOperations([1, 5]))
print(so.minOperations([2, 2]))
print(so.minOperations([4, 2, 5]))
print(so.minOperations([3, 2, 2, 4]))
print(so.minOperations([2, 4, 8, 16]))
print(so.minOperations([2, 4, 8, 16, 0]))
