#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find First Palindromic String in the Array.py 
@time: 2021/12/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if all(word[i] == word[~i] for i in range(len(word) // 2)):
                return word
        return ''
