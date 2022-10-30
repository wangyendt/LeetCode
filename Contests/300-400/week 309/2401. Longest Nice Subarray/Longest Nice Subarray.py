#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Nice Subarray.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        cur = collections.defaultdict(int)
        ret = 0
        left = 0
        bin_res = collections.defaultdict(list)
        for right, n in enumerate(nums):
            bin_n = str(bin(n)[2:])
            for i, b in enumerate(bin_n[::-1]):
                if b == '1':
                    cur[i] += 1
                    bin_res[right].append(i)
            if not all(v <= 1 for k, v in cur.items()):
                while any(v > 1 for k, v in cur.items()) and left < right:
                    one_list = bin_res[left]
                    for one in one_list:
                        cur[one] -= 1
                    left += 1
            ret = max(ret, right - left + 1)
        return ret


so = Solution()
print(so.longestNiceSubarray(nums=[1, 3, 8, 48, 10]))
print(so.longestNiceSubarray([84139415, 693324769, 614626365, 497710833, 615598711, 264, 65552, 50331652, 1, 1048576, 16384, 544, 270532608, 151813349, 221976871, 678178917, 845710321, 751376227, 331656525, 739558112, 267703680]))
print(so.longestNiceSubarray([178830999, 19325904, 844110858, 806734874, 280746028, 64, 256, 33554432, 882197187, 104359873, 453049214, 820924081, 624788281, 710612132, 839991691]))
