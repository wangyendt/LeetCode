#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Remove Letter To Equalize Frequency.py 
@time: 2022/10/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnter = collections.Counter(word)
        for w in word:
            cnter[w] -= 1
            if not cnter[w]: cnter.pop(w)
            if len(set(cnter.values())) == 1: return True
            cnter[w] += 1
        return False


so = Solution()
print(so.equalFrequency("bac"))
print(so.equalFrequency("abbcc"))
print(so.equalFrequency("cbccca"))
