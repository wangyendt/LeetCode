#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Collisions on a Road.py 
@time: 2022/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
        ret = 0
        for i, d in enumerate(directions):
            if d != 'S':
                ret += 1
        return ret
