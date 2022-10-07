#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Construct Smallest Number From DI String.py 
@time: 2022/10/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import itertools


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        for item in itertools.permutations(range(1, len(pattern) + 2)):
            # print(item)
            for i, p in enumerate(pattern):
                if p == 'I' and item[i] > item[i + 1]:
                    break
                if p == 'D' and item[i] < item[i + 1]:
                    break
            else:
                return ''.join([str(it) for it in item])


so = Solution()
print(so.smallestNumber(pattern="IIIDIDDD"))
print(so.smallestNumber(pattern="DDDDDDDD"))
