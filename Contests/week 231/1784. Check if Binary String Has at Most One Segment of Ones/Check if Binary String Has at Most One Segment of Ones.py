#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Binary String Has at Most One Segment of Ones.py 
@time: 2021/03/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ret1 = True
        for t in s:
            if t == '0':
                ret1 = False
            else:
                if not ret1:
                    return False
        return True
