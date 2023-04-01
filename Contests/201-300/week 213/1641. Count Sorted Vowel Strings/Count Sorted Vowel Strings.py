#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Sorted Vowel Strings.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(i, last):
            if i == 1:
                if last == 'a':
                    return 5
                if last == 'e':
                    return 4
                if last == 'i':
                    return 3
                if last == 'o':
                    return 2
                if last == 'u':
                    return 1
            else:
                return sum(dp(i - 1, l) for l in 'aeiou' if l >= last)

        return dp(n, 'a')


so = Solution()
print(so.countVowelStrings(1))
print(so.countVowelStrings(2))
print(so.countVowelStrings(33))
