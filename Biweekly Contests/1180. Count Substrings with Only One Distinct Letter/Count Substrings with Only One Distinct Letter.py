# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/7 23:30
# software: PyCharm


class Solution:
    def countLetters(self, S: str) -> int:
        prev = '_'
        ret = 0
        cnt = 0
        for s in S:
            if prev == s:
                cnt += 1
            else:
                cnt = 1
            ret += cnt
            prev = s
        return ret


so = Solution()
print(so.countLetters("aaaaaaaaaa"))
print(so.countLetters("aaaba"))
