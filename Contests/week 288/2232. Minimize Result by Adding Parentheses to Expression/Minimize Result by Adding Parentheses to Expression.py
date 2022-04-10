#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize Result by Adding Parentheses to Expression.py 
@time: 2022/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split('+')
        res_m = float('inf')
        ret = ''
        for i in range(len(num1)):
            for j in range(len(num2)):
                a1 = num1[:i] or '1'
                a2 = num1[i:]
                a3 = num2[:j + 1]
                a4 = num2[j + 1:] or '1'
                res = int(a1) * (int(a2) + int(a3)) * int(a4)
                if res < res_m:
                    res_m = res
                    ret = f'{num1[:i]}({num1[i:]}+{num2[:j + 1]}){num2[j + 1:]}'
                res_m = min(res_m, res)
        return ret


so = Solution()
print(so.minimizeResult(expression="247+38"))
