#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Rearrange Spaces Between Words
@time: 2020/09/20 17:17
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spl = text.split(' ')
        n_space = sum(1 for t in text if t == ' ')
        words = [s for s in spl if s]
        n_words = len(words)
        if n_words == 1:
            return words[0] + ' ' * n_space
        d, r = divmod(n_space, n_words - 1)
        return (' ' * d).join(words) + ' ' * r


so = Solution()
print(so.reorderSpaces(text="  this   is  a sentence "))
print(so.reorderSpaces(text=" practice   makes   perfect"))
print(so.reorderSpaces(text="hello   world"))
print(so.reorderSpaces(text="  walks  udp package   into  bar a"))
print(so.reorderSpaces(text="a"))
