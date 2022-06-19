#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Numbers With Units Digit K.py 
@time: 2022/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        s = 0
        cnt = 0
        if k == 0:
            if num % 10 == 0:
                return 1
            else:
                return -1
        while True:
            s += k
            cnt += 1
            if s % 10 == num % 10:
                if num // k + 1 >= cnt:
                    return cnt
                else:
                    return -1
            else:
                if s % 10 == k % 10 and cnt > 1:
                    return -1


so = Solution()
print(so.minimumNumbers(num=58, k=9))
print(so.minimumNumbers(5, 1))
