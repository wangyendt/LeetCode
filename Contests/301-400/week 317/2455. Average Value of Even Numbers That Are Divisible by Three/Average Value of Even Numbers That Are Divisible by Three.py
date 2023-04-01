#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Average Value of Even Numbers That Are Divisible by Three.py 
@time: 2022/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ret = 0
        cnt = 0
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                ret += n
                cnt += 1
        if cnt == 0: return 0
        return ret // cnt
