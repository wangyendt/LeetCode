#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/18 22:55
@Author:  wang121ye
@File: The k-th Lexicographical String of All Happy Strings of Length n.py
@Software: PyCharm
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * 2 ** (n - 1)
        if total < k: return ''
        if n == 1:
            if k == 1:
                return 'a'
            elif k == 2:
                return 'b'
            elif k == 3:
                return 'c'
        rest = [3] + [2] * (n - 1)
        ret = ''
        last = 'x'
        k -= 1
        for r in rest:
            total = total // r
            d, re = divmod(k, total)
            k = re
            # print(k,total,r,d,re)
            if r == 3:
                ret = ret + 'abc'[d]
                last = 'abc'[d]
            else:
                if last == 'a':
                    choice = 'bc'
                elif last == 'b':
                    choice = 'ac'
                elif last == 'c':
                    choice = 'ab'
                ret = ret + choice[d]
                last = choice[d]
        return ret


so = Solution()
print(so.getHappyString(1, 3))
print(so.getHappyString(1, 4))
print(so.getHappyString(3, 9))
print(so.getHappyString(2, 7))
print(so.getHappyString(10, 100))
# for i in range(13):
#     print(i,so.getHappyString(3,i))
