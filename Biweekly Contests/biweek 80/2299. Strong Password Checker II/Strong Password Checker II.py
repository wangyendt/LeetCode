#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Strong Password Checker II.py 
@time: 2022/06/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if (len(password) >= 8 and
                any(c in password for c in letters) and
                any(c in password for c in letters.upper()) and
                any(c in password for c in '0123456789') and
                any(c in password for c in '!@#$%^&*()-+')
        ):
            last = 'shit'
            for p in password:
                if p == last: return False
                last = p
            return True
        return False
