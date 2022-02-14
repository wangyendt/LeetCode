#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Smallest Value of the Rearranged Number.py 
@time: 2022/02/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def smallestNumber(self, num: int) -> int:
        s_num = str(num)
        cnter = collections.Counter(s_num)
        ret = []
        if s_num[0] == '-':
            ret.append('-')
            for n in '9876543210':
                for i in range(cnter[n]):
                    ret.append(n)
        else:
            push_zero = False
            for n in '123456789':
                for i in range(cnter[n]):
                    ret.append(n)
                    if not push_zero and cnter[n] > 0:
                        for i in range(cnter['0']):
                            ret.append('0')
                        push_zero = True
        return int(''.join(ret) or '0')
