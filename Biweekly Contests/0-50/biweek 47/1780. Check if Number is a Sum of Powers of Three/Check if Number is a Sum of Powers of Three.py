#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Number is a Sum of Powers of Three.py 
@time: 2021/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(1, 2 ** 15):
            res = 0
            for j in range(15):
                if i & (1 << j):
                    res += 3 ** j
                    if res > n: return False
            if res == n:
                return True
        return False


so = Solution()
print(so.checkPowersOfThree(5867291))
