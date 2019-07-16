# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 14:35
# software: PyCharm

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        if word[0].isupper():
            return all([i.isupper() for i in word[1:]]) or all([i.islower() for i in word[1:]])
        else:
            return all([i.islower() for i in word])


so = Solution()
print(so.detectCapitalUse("USA"))
print(so.detectCapitalUse("leetcode"))
print(so.detectCapitalUse("Google"))
print(so.detectCapitalUse("FlaG"))
