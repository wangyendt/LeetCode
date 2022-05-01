#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Total Appeal of A String.py 
@time: 2022/05/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def appealSum(self, s: str) -> int:
        lastSeenMap = {s[0]: 0}
        prev, curr, res = 1, 0, 1

        for i in range(1, len(s)):
            if s[i] in lastSeenMap:
                curr = prev + (i - lastSeenMap[s[i]])
            else:
                curr = prev + (i + 1)
            res += curr
            prev = curr
            lastSeenMap[s[i]] = i
        return res
