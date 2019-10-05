#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Stepping Numbers.py 
@time: 2019/10/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import bisect


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list:
        ret = []

        def dfs(l, h, step_num):
            if l <= step_num <= h:
                bisect.insort(ret, step_num)
            if step_num == 0 or step_num > h:
                return
            last_digit = step_num % 10
            step_a = 10 * step_num + last_digit - 1
            step_b = 10 * step_num + last_digit + 1
            if last_digit == 0:
                dfs(l, h, step_b)
            elif last_digit == 9:
                dfs(l, h, step_a)
            else:
                dfs(l, h, step_a)
                dfs(l, h, step_b)

        for i in range(10):
            dfs(low, high, i)
        return ret


so = Solution()
print(so.countSteppingNumbers(low=0, high=100000000))
