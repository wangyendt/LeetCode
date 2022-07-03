#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Decode the Message.py 
@time: 2022/07/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = collections.defaultdict(str)
        idx = 0
        seen = set()
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(idx, len(key)):
            if key[i] == ' ': continue
            if key[i] not in seen:
                seen.add(key[i])
                res[key[i]] = letters[idx]
                idx += 1
                if idx == 26: break
        ret = []
        for m in message:
            if m == ' ':
                ret.append(' ')
            else:
                ret.append(res[m])
        return ''.join(ret)
