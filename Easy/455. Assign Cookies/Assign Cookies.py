# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 14:07
# software: PyCharm

class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        if not s or not g: return 0
        g.sort()
        s.sort()
        p, q, ret = 0, 0, 0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                ret += 1
                p += 1
                q += 1
            else:
                q += 1
        return ret


so = Solution()
print(so.findContentChildren([1, 2, 3], [1, 1]))
print(so.findContentChildren([1, 2], [1, 2, 3]))
