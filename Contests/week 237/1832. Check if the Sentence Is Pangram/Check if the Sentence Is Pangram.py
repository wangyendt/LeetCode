#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if the Sentence Is Pangram.py 
@time: 2021/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""
r

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(set(sentence)) == 26:
            return True
        return False
