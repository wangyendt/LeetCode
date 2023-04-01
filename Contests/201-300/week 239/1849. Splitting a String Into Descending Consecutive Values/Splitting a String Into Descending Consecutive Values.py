#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Splitting a String Into Descending Consecutive Values.py 
@time: 2021/05/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(s, x):
            if x is None:
                for i in range(1, len(s)):
                    if backtrack(s[i:], int(s[:i])):
                        return True
                return False
            else:
                if s == "" or int(s) == x - 1:
                    return True
                for i in range(1, len(s)):
                    if int(s[:i]) == x - 1:
                        return backtrack(s[i:], x - 1)
                return False

        return backtrack(s, None)


so = Solution()
print(so.splitString(s="1234"))
print(so.splitString(s="050043"))
print(so.splitString("2063852321103144212"))
print(so.splitString("4021442107494234334"))
print(so.splitString("1098765432"))
print(so.splitString("4771447713"))
