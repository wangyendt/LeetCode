#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Hexspeak
@time: 2019/12/2 13:49
"""


class Solution:
    def toHexspeak(self, num: str) -> str:
        res = ''
        dic = '0123456789ABCDEF'
        num = int(num)
        while num:
            num, rem = divmod(num, 16)
            res += dic[rem]
        res = res[::-1]
        ret = res.replace('0','O').replace('1','I')
        if any([letter in ret for letter in '23456789']):
            return 'ERROR'
        return ret


so = Solution()
print(so.toHexspeak('257'))
print(so.toHexspeak('3'))
print(so.toHexspeak('29'))
