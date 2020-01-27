#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Remove Palindromic Subsequences
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/26 10:31
@Desc   ：
=================================================="""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # print(s)
        if not s:
            return 0

        def is_palindrome(s_: str):
            for i in range(len(s_) // 2):
                if s_[i] != s_[~i]: return False
            return True

        if is_palindrome(s): return 1
        return 2


so = Solution()
print(so.removePalindromeSub('ababa'))
print(so.removePalindromeSub('abb'))
print(so.removePalindromeSub('baabb'))
print(so.removePalindromeSub(''))
print(so.removePalindromeSub('ababb'))
print(so.removePalindromeSub("bbaabaaa"))
