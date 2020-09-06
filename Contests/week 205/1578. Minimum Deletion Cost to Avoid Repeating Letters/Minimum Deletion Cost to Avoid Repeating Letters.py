#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Minimum Deletion Cost to Avoid Repeating Letters.py 
@time: 2020/09/06
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minCost(self, s: str, cost: list) -> int:
        stack = {}
        ret = 0

        def get_min_cost(A: dict) -> int:
            if not A: return 0
            return sum(A.values()) - max(A.values())

        for i, t in enumerate(s):
            if i and t == s[i - 1]:
                stack[i - 1] = cost[i - 1]
                stack[i] = cost[i]
            else:
                ret += get_min_cost(stack)
                stack = {}
        ret += get_min_cost(stack)
        return ret


so = Solution()
print(so.minCost(s='a', cost=[1]))
