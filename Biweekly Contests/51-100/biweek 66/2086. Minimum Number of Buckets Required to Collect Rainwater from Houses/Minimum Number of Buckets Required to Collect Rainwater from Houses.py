#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Buckets Required to Collect Rainwater from Houses.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumBuckets(self, s: str) -> int:
        return -1 if 'HHH' in s or s[:2] == 'HH' or s[-2:] == 'HH' or s == 'H' else s.count('H') - s.count('H.H')
