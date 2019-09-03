#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: 211. Add and Search Word - Data structure design.py 
@time: 2019/09/04
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = list(self.dict[len(word)])
        for wi, ww in enumerate(word):
            if ww == '.': continue
            stack_ = []
            for s in stack:
                if s[wi] == ww:
                    stack_.append(s)
            stack = stack_[:]
        return True if stack else False
