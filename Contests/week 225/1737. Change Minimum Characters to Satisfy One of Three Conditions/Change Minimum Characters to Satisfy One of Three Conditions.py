#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Change Minimum Characters to Satisfy One of Three Conditions.py 
@time: 2021/01/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'

        def cond3(a, b):
            cnt = collections.Counter(a) + collections.Counter(b)
            return len(a) + len(b) - cnt.most_common(1)[0][1]

        def cond1(a, b):
            cnt_a, cnt_b = collections.Counter(a), collections.Counter(b)
            ret = len(a) + len(b)
            sa = 0
            for let_a in letters[::-1]:
                if let_a in cnt_a:
                    sb = 0
                    for let_b in letters:
                        if let_b not in cnt_b:
                            continue
                        if let_b > let_a:
                            break
                        else:
                            sb += cnt_b[let_b]
                    if let_b > let_a:
                        ret = min(ret, sa + sb)
                    sa += cnt_a[let_a]
                else:
                    continue
            return ret

        # print(cond3(a, b))
        return min(cond3(a, b), cond1(a, b), cond1(b, a))


so = Solution()
print(so.minCharacters('aba', 'caa'))
print(so.minCharacters('aaa', 'bbbb'))
print(so.minCharacters('aaa', 'aaaa'))
print(so.minCharacters('abcba', 'cbacd'))
