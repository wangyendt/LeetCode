# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 11:38
# software: PyCharm


class Solution:
    def equalSubstring(self, s: str, t: str, cost: int) -> int:
        arr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        arr.insert(0, 0)
        res, ret, p, q = 0, 0, 0, 1
        while q < len(arr):
            res += arr[q]
            while p <= q and res > cost:
                res -= arr[p]
                p += 1
            ret = max(ret, q + 1 - max(p, 1))  # if p==0, ret = max(ret, q)
            q += 1
        return ret


so = Solution()
print(so.equalSubstring(s="abcd", t="bcdf", cost=3))
print(so.equalSubstring(s="abcd", t="cdef", cost=3))
print(so.equalSubstring(s="abcd", t="acde", cost=0))
print(so.equalSubstring("abcd", "cdef", 1))
print(so.equalSubstring("krrgw", "zjxss", 19))
