#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Minimum Number of Steps to Make Two Strings Anagram
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:26
@Desc   ：
=================================================="""

import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c_s, c_t = collections.Counter(s), collections.Counter(t)
        ret = 0
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if c_s[letter] < c_t[letter]:
                ret += c_t[letter] - c_s[letter]
        return ret


so = Solution()
print(so.minSteps(s="bab", t="aba"))
print(so.minSteps(s="leetcode", t="practice"))
print(so.minSteps(s="anagram", t="mangaar"))
print(so.minSteps(s="xxyyzz", t="xxyyzz"))
print(so.minSteps(s="friend", t="family"))
