#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Reinitialize a Permutation.py 
@time: 2021/03/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = list(range(n))
        ret = 0
        while not all(arr[i] < arr[i + 1] for i in range(n - 1)) or ret == 0:
            ret += 1
            arr2 = []
            for j in range(n):
                if j % 2 == 0:
                    arr2.append(arr[j // 2])
                else:
                    arr2.append(arr[n // 2 + (j - 1) // 2])
            arr = arr2
        return ret
