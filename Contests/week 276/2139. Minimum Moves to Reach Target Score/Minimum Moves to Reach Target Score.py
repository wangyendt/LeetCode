#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Moves to Reach Target Score.py 
@time: 2022/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ret = 0
        while target > 1:
            if target & 1:
                ret += 1
                target -= 1
            else:
                if maxDoubles == 0:
                    return ret + (target - 1)
                else:
                    target //= 2
                    maxDoubles -= 1
                    ret += 1
        return ret
