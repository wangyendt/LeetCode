#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Score From Removing Substrings.py 
@time: 2021/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ret = 0
        for la, lb, va, vb in [('a', 'b', x, y), ('b', 'a', y, x)]:
            stack1 = []
            res = 0
            for i1, s1 in enumerate(s):
                if stack1 and s1 == lb and stack1[-1] == la:
                    res += va
                    stack1.pop()
                    continue
                stack1.append(s1)
            stack2 = []
            for i2, s2 in enumerate(stack1):
                if stack2 and s2 == la and stack2[-1] == lb:
                    res += vb
                    stack2.pop()
                    continue
                stack2.append(s2)
            ret = max(ret, res)
        return ret


so = Solution()
print(so.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
