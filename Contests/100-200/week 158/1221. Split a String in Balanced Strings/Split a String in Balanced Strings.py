#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Split a String in Balanced Strings.py 
@time: 2019/10/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cur = 0
        ret = 0
        for ss in s:
            if ss == 'L':
                cur += 1
            else:
                cur -= 1
            if cur == 0: ret += 1
        return ret


so = Solution()
print(so.balancedStringSplit("RLRRLLRLRL"))
print(so.balancedStringSplit("RLLLLRRRLR"))
print(so.balancedStringSplit("LLLLRRRR"))
