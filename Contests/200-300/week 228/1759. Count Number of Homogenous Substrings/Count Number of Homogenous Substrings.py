# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Count Number of Homogenous Substrings.py
@time: 2021/02/14
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        last = '!'
        ret = res = 0
        s = s + '!'
        for t in s:
            if t == last:
                res += 1
            else:
                ret += res * (res + 1) // 2
                res = 1
            last = t
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.countHomogenous('abbcccaa'))
print(so.countHomogenous('xy'))
print(so.countHomogenous('zzzzz'))
print(so.countHomogenous('z'))
