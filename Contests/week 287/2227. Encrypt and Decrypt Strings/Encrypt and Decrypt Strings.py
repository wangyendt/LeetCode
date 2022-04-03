#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Encrypt and Decrypt Strings.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc = {k: v for k, v in zip(keys, values)}
        self.decrypt = collections.Counter(self.encrypt(w) for w in dictionary).__getitem__

    def encrypt(self, word1: str) -> str:
        return ''.join(self.enc[c] for c in word1)

    def decrypt(self, word2: str) -> int:
        pass
