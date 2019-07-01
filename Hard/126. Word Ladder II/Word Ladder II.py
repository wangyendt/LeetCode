#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Word Ladder II.py 
@time: 2019/07/02
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i + 1:]
                            if neww in wordList:
                                newlayer[neww] += [j + [neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res


so = Solution()
# print(so.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
begin = "qa"
end = "sq"
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci",
            "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
            "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb",
            "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
            "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
            "pa", "he", "lr", "sq", "ye"]
print(so.findLadders(begin, end, wordList))
