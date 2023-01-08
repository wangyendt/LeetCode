#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Make Number of Distinct Characters Equal.py 
@time: 2023/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)
        s1, s2 = set(word1), set(word2)
        for w1 in s1:
            for w2 in s2:
                cnt1[w1] -= 1
                cnt1[w2] += 1
                cnt2[w1] += 1
                cnt2[w2] -= 1
                if cnt1[w1] == 0:
                    cnt1.pop(w1)
                if cnt2[w2] == 0:
                    cnt2.pop(w2)
                if len(cnt1) == len(cnt2):
                    return True
                cnt1[w1] += 1
                cnt1[w2] -= 1
                cnt2[w1] -= 1
                cnt2[w2] += 1
                if cnt1[w2] == 0:
                    cnt1.pop(w2)
                if cnt2[w1] == 0:
                    cnt2.pop(w1)
        return False


so = Solution()
print(so.isItPossible(word1="ac", word2="b"))
print(so.isItPossible(word1="b", word2="ac"))
print(so.isItPossible(word1="abcc", word2="aab"))
print(so.isItPossible("ab", "abcc"))
print(so.isItPossible("a", "bb"))
