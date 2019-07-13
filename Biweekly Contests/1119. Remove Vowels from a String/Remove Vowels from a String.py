#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Remove Vowels from a String.py 
@time: 2019/07/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for v in vowels:
            S = S.replace(v, '')
        return S
