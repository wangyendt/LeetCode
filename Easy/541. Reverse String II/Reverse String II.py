# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 18:56
# software: PyCharm

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret = ''
        while s:
            if not s: break
            n = len(s)
            if n >= 2 * k:
                ret += s[:k][::-1] + s[k:2 * k]
                s = s[2 * k:]
            else:
                if n < k:
                    ret += s[::-1]
                    break
                else:
                    ret += s[:k][::-1] + s[k:]
                    break
        return ret


so = Solution()
print(so.reverseStr('abcdabcdefg', 2))
