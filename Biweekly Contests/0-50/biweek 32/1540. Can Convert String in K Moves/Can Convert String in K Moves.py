#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Can Convert String in K Moves.py 
@time: 2020/08/09
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        cnter = collections.defaultdict(int)

        def dist(la, lb):
            return (ord(lb) - ord(la)) % 26

        for i in range(len(s)):
            d = dist(s[i], t[i])
            if d:
                cnter[d] += 1
        res = sorted(list(cnter.items()), key=lambda x: (-x[1], -x[0]))
        if not res: return True
        r0 = res[0]
        return (r0[1] - 1) * 26 + r0[0] <= k


so = Solution()
print(so.canConvertString(s="input", t="ouput", k=9))
