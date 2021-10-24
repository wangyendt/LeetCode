#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Valid Words in a Sentence.py 
@time: 2021/10/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def countValidWords(self, sentence: str) -> int:
        items = sentence.split(' ')
        ret = 0
        for item in items:
            if not item.strip(' '): continue
            if any(d in item for d in '0123456789'):
                continue
            if any(p in item[:-1] for p in '!.,'):
                continue
            if collections.Counter(item)['-'] > 1:
                continue
            elif collections.Counter(item)['-'] == 1:
                if item[0] == '-' or item[-1] == '-': continue
                for i, t in enumerate(item):
                    if t == '-':
                        if i == 0 or i == len(item) - 1:
                            break
                        if item[i - 1] not in 'abcdefghijklmnopqrstuvwxyz' or item[
                            i + 1] not in 'abcdefghijklmnopqrstuvwxyz':
                            break
                else:
                    ret += 1
                continue
            ret += 1
        return ret
