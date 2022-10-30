#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Score of a Good Subarray.py 
@time: 2021/03/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        size = len(nums)
        ret = 0
        heights = [0] + nums + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                if stack[-1] <= k <= i - 2:
                    ret = max(ret, cur_height * cur_width)
            stack.append(i)
        return ret


so = Solution()
print(so.maximumScore([6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872], 5))
