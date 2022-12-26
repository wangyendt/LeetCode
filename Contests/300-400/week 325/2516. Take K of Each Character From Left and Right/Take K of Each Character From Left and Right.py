#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Take K of Each Character From Left and Right.py 
@time: 2022/12/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ra = s.count('a') - k
        rb = s.count('b') - k
        rc = s.count('c') - k

        # if any of them is less than 0, it means there are less than k occurences of a character.
        if any(i < 0 for i in [ra, rb, rc]):
            return -1

        hm = collections.defaultdict(int)
        l = j = res = 0

        for i in s:
            hm[i] += 1
            l += 1

            while hm['a'] > ra or hm['b'] > rb or hm['c'] > rc:
                hm[s[j]] -= 1
                l -= 1
                j += 1

            res = max(res, l)

        return len(s) - res


so = Solution()
# print(so.takeCharacters(s="aabaaaacaabc", k=2))
# print(so.takeCharacters(s="a", k=1))
print(so.takeCharacters(s="abc", k=1))
