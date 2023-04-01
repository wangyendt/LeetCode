#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Remove All Occurrences of a Substring.py 
@time: 2021/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            s_ = s.replace(part, '', 1)
            print(f'{s_=}')
            if s_ == s: break
            s = s_
        return s


so = Solution()
print(so.removeOccurrences(s="axxxxyyyyb", part="xy"))
print(so.removeOccurrences(s="axxxxyyyyb" * 100, part="xy"))
