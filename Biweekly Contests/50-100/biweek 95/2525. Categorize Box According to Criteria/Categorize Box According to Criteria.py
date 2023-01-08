#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Categorize Box According to Criteria.py 
@time: 2023/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        res = []
        if max(length, width, height, mass) >= 10 ** 4 or width * height * length >= 10 ** 9:
            res.append('Bulky')
        if mass >= 100:
            res.append("Heavy")
        if len(res) == 2:
            return 'Both'
        if len(res) == 0:
            return 'Neither'
        if len(res) == 1:
            return res[0]
