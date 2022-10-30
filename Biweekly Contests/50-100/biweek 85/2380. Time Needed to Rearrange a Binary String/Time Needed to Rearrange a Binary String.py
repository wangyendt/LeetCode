#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Time Needed to Rearrange a Binary String.py 
@time: 2022/10/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ret = 0
        while '01' in s:
            s = s.replace('01', '10')
            ret += 1
        return ret


so = Solution()
print(so.secondsToRemoveOccurrences("001011"))
print(so.secondsToRemoveOccurrences("1111000"))
print(so.secondsToRemoveOccurrences("001000011"))
