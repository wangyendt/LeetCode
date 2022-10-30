#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Garden Perimeter to Collect Enough Apples.py 
@time: 2021/08/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        a = int((neededApples * 2) ** (1 / 3.))
        a += a * (a + 1) * (a + 2) / 2 < neededApples
        a += a % 2
        return a * 4
