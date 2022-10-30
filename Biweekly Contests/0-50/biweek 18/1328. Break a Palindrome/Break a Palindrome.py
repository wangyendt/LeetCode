#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Break a Palindrome
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/27 15:50
@Desc   ：
=================================================="""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        if all(p == 'a' for p in palindrome): return palindrome[:-1] + 'b'
        if len(palindrome) % 2 == 1 and all(p == 'a' for i, p in enumerate(palindrome) if i != len(palindrome) // 2):
            return palindrome[:-1] + 'b'
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]


so = Solution()
print(so.breakPalindrome(palindrome="abccba"))
print(so.breakPalindrome(palindrome="a"))
print(so.breakPalindrome(palindrome="aaaaaaa"))
print(so.breakPalindrome(palindrome="bbbbabbbb"))
