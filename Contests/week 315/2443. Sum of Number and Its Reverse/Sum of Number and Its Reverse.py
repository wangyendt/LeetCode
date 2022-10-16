#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Number and Its Reverse.py 
@time: 2022/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            # print(i, str(i)[::-1])
            if i + int(str(i)[::-1]) == num:
                return True
        return False


so = Solution()
print(so.sumOfNumberAndReverse(num=181))
