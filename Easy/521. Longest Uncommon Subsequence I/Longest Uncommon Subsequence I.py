# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 14:39
# software: PyCharm

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


so = Solution()
print(so.findLUSlength('aaa', 'bbb'))
