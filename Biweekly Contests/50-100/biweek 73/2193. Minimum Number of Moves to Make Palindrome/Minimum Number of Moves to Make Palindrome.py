#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Moves to Make Palindrome.py 
@time: 2022/03/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        left, right = 0, len(s) - 1
        ret = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue

            same_left = right
            while same_left > left and s[same_left] != s[left]:
                same_left -= 1

            if same_left == left:
                s[left], s[left + 1] = s[left + 1], s[left]
                ret += 1
                continue

            for i in range(same_left, right):
                s[i], s[i + 1] = s[i + 1], s[i]
                ret += 1

            left += 1
            right -= 1

        return ret


so = Solution()
print(so.minMovesToMakePalindrome(s="letelt"))
print(so.minMovesToMakePalindrome(
    "rtkkdfeuqvksupbdikjbijsusbpepsiqnmwdwdhdkqfzlvbozjwiyctjfjubvsldsyywddvyxwvdmwoxxwygmtiwzkjkrjdxpyjsjzoqoxysymcmijgkzprajlmlmzqztjilssxixwktmvumdoenzrdohrwsjimnwfmxajvvvouublxwlskueolznmvyycqdrenutsfjusmnaekfbsmcfjigzjbrpzrrivegrcocrrneekcpuydxvgyjtyxprildvjriyxqueuaipbpdvvtwfusswmvippmliqmomgzsnyjcywb"))
