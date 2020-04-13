#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/12 10:33
@Author:  wang121ye
@File: String Matching in an Array.py
@Software: PyCharm
"""


class Solution:
    def stringMatching(self, words: list) -> list:
        words = sorted(words, key=lambda x: len(x))
        ret = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ret.append(words[i])
                    break
        return ret


so = Solution()
print(so.stringMatching(words=["mass", "as", "hero", "superhero"]))
print(so.stringMatching(words=["leetcode", "et", "code"]))
print(so.stringMatching(words=["blue", "green", "bu"]))
