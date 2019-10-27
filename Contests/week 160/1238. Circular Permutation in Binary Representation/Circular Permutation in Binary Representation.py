# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/27 11:38
# software: PyCharm


class Solution:
    def circularPermutation(self, n: int, start: int) -> list:
        res = []

        def helper(cnt: int):
            if cnt == n + 1: return
            for r in res[::-1]:
                tmp = r[:]
                tmp[-cnt] = '1' if tmp[-cnt] == '0' else '0'
                res.append(tmp[:])
            helper(cnt + 1)

        # if  n == 1:
        #     return [start,s]
        start_str = ['0'] * n
        for i, s in enumerate(bin(start)[2:][::-1]):
            start_str[-1 - i] = s
        res.append(start_str)
        helper(1)
        ret = []
        for r in res:
            cur = 0
            l = len(r)
            for ii, rr in enumerate(r):
                cur += 2 ** (l - ii - 1) * int(rr)
            ret.append(cur)
        return ret


so = Solution()
print(so.circularPermutation(4, 5))
print(so.circularPermutation(3, 2))
print(so.circularPermutation(1, 1))
print(so.circularPermutation(16, 2))
