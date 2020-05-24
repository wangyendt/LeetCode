#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/24 10:34
@Author:  wang121ye
@File: Check If a Word Occurs As a Prefix of Any Word in a Sentence.py
@Software: PyCharm
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = len(searchWord)
        for i, word in enumerate(sentence.split(' ')):
            if searchWord == word[:l]:
                return i + 1
        return -1


so = Solution()
print(so.isPrefixOfWord(sentence="i love eating burger", searchWord="burg"))
print(so.isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro"))
print(so.isPrefixOfWord(sentence="i am tired", searchWord="you"))
print(so.isPrefixOfWord(sentence="i use triple pillow", searchWord="pill"))
print(so.isPrefixOfWord(sentence="hello from the other side", searchWord="they"))
