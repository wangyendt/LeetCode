# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/6 19:07
# software: PyCharm

class Solution:
    def partition(self, s: str) -> list(list()):
        if not s:
            return []

        def isPalindrome(string):
            for i in range(len(string) // 2):
                if string[i] != string[-1 - i]:
                    return False
            return True

        p = 0
        ret = []
        while p < len(s) - 1:
            if isPalindrome(s[:p + 1]):
                [ret.append([s[:p + 1]] + res) for res in self.partition(s[p + 1:])]
            p += 1
        if isPalindrome(s):
            ret.append([s])
        return ret


so = Solution()
print(so.partition("aab"))
print(so.partition(""))
