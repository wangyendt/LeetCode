#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Wonderful Substrings.py 
@time: 2021/06/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        mask_count = [0] * 1024
        mask_count[mask] += 1
        res = 0

        for letter in word:
            mask ^= 1 << ord(letter) - ord("a")
            res += mask_count[mask]
            for i in range(10):
                res += mask_count[mask ^ 1 << i]
            mask_count[mask] += 1
        return res


so = Solution()
print(so.wonderfulSubstrings(word="aabb"))
