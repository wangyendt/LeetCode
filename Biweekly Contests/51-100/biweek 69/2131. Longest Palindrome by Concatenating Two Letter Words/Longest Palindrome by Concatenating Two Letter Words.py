#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Palindrome by Concatenating Two Letter Words.py 
@time: 2022/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnter = collections.defaultdict(int)
        for word in words:
            cnter[word] += 1
        ret = 0
        rep = False
        cnter_items = list(cnter.items())
        cnter_items.sort(key=lambda x: -x[1])
        # print(cnter_items)
        for k, v in cnter_items:
            # print(ret, k, v, cnter[k[::-1]], k[0] == k[1], v == 1, rep)
            if v > 0 and cnter[k[::-1]] > 0:
                if k[0] == k[1]:
                    if v % 2 == 0:
                        ret += 2 * v
                        cnter[k] = 0
                        continue
                    else:
                        if not rep:
                            ret += 2 * v
                            cnter[k] = 0
                            rep = True
                        else:
                            ret += 2 * v - 2
                            cnter[k] = 1
                        continue
                else:
                    vv = min(cnter[k], cnter[k[::-1]])
                    ret += 4 * vv
                    cnter[k] -= vv
                    cnter[k[::-1]] -= vv
        return ret


so = Solution()
print(so.longestPalindrome(words=["lc", "cl", "gg"]))
print(so.longestPalindrome(words=["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]))
