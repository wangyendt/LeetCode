#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Calculate Digit Sum of a String.py 
@time: 2022/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k: return s
        return self.digitSum(''.join(str(sum(int(d) for d in s[i:i + k])) for i in range(0, len(s), k)), k)
