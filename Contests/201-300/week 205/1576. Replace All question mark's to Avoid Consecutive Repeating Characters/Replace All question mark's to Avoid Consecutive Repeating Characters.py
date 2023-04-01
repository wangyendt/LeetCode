#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Replace All question mark's to Avoid Consecutive Repeating Characters.py 
@time: 2020/09/06
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def modifyString(self, s: str) -> str:
        cur = '#'
        ret = []
        cnt = 0
        for i, t in enumerate(s):
            if t != '?':
                if i and s[i - 1] == '?':
                    pre = '#'
                    for k in range(cnt):
                        for l in 'abcdefghijklmnopqrstuvwxyz':
                            if l != cur and l != t and l != pre:
                                ret.append(l)
                                pre = l
                                break
                cur = t
                ret.append(t)
                cnt = 0
            else:
                cnt += 1
        if cnt:
            pre = '#'
            for k in range(cnt):
                for l in 'abcdefghijklmnopqrstuvwxyz':
                    if l != cur and l != t and l != pre:
                        ret.append(l)
                        pre = l
                        break
        return ''.join(ret)


so = Solution()
print(so.modifyString(s="j?qg??b"))
print(so.modifyString(s='a?'))
