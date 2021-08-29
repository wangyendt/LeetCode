#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Unique Good Subsequences.py 
@time: 2021/08/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10 ** 9 + 7
        zeros = ones = 0
        for b in binary:
            if b == '1':
                ones += zeros + 1
            else:
                zeros += ones
        return (ones + zeros + (bool(zeros) | (binary[0] == '0'))) % mod


so = Solution()
print(so.numberOfUniqueGoodSubsequences('101'))
print(so.numberOfUniqueGoodSubsequences('001'))
print(so.numberOfUniqueGoodSubsequences("111001101100000001001110110101110001100"))
print(so.numberOfUniqueGoodSubsequences("1110001"))
