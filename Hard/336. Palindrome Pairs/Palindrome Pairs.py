#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Palindrome Pairs
@time: 2020/07/10 19:52
"""

import collections


class Trie:
    def __init__(self):
        self.child = collections.defaultdict(Trie)
        self.is_end = False

    def add(self, word):
        if word:
            self.child[word[0]].add(word[1:])
        else:
            self.is_end = True

    def get(self) -> list:
        if not self.child: return ['']
        ret = []
        for k, v in self.child.items():
            for res in v.get():
                ret.append(k + res)
        if self.is_end:
            ret.append('')
        return ret

    def find(self, word):
        if not self.child:
            if not word: return ['']
            return []
        if not word: return self.get()
        if word[0] in self.child:
            return self.child[word[0]].find(word[1:])
        return []


class Solution:
    def palindromePairs(self, words: list) -> list(list()):
        is_pal = collections.defaultdict(bool)

        def is_palindrome(s: str):
            is_pal[s] = all(s[i] == s[~i] for i in range(len(s) // 2))
            return is_pal[s]

        trie1, trie2 = Trie(), Trie()
        word_ind = collections.defaultdict(int)
        all_palindrome_ind = []
        for wi, word in enumerate(words):
            trie1.add(word)
            trie2.add(word[::-1])
            word_ind[word] = wi
            if is_palindrome(word):
                all_palindrome_ind.append(wi)

        ret = set()
        for wi, word in enumerate(words):
            if not word:
                for pi in all_palindrome_ind:
                    if wi != pi:
                        ret.add((wi, pi))
                        ret.add((pi, wi))
                continue
            for res in trie2.find(word):
                if res in is_pal and is_pal[res] or is_palindrome(res):
                    p = (word + res)[::-1]
                    if p in word_ind and word_ind[p] != wi:
                        ret.add((wi, word_ind[p]))
            for res in trie1.find(word[::-1]):
                if res in is_pal and is_pal[res] or is_palindrome(res):
                    p = (word[::-1] + res)
                    if p in word_ind and word_ind[p] != wi:
                        ret.add((word_ind[p], wi))

        # print(trie1.find(''))
        return [list(a) for a in ret]


so = Solution()
# print(so.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
# print(so.palindromePairs(["bat", "tab", "cat"]))
print(so.palindromePairs(["a", "b", "c", "ab", "ac", "aa"]))
