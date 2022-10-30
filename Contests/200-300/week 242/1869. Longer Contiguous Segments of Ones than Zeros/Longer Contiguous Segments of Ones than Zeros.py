#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longer Contiguous Segments of Ones than Zeros.py 
@time: 2021/05/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def helper(t: str):
            ret = 0
            res = 0
            for tt in s:
                if tt == t:
                    res += 1
                else:
                    ret = max(ret, res)
                    res = 0
            return max(ret, res)

        return helper('1') > helper('0')
