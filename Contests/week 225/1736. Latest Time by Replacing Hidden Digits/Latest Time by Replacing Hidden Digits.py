#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Latest Time by Replacing Hidden Digits.py 
@time: 2021/01/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == '?':
            if time[1] in '0123?':
                time[0] = '2'
            else:
                time[0] = '1'
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'
        if time[2] == '?':
            time[2] = ':'
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'
        return ''.join(time)
