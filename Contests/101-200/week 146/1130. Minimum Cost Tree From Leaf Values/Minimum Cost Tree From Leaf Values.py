#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Minimum Cost Tree From Leaf Values.py 
@time: 2019/07/22
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def mctFromLeafValues(self, arr):
        res, n = 0, len(arr)
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


so = Solution()
print(so.mctFromLeafValues([6, 2, 4]))
