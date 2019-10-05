#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Number of Valid Words for Each Puzzle.py 
@time: 2019/09/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections
import itertools


class Solution:
    def findNumOfValidWords(self, words, puzzles):
        count = collections.Counter("".join(sorted(set(w))) for w in words)
        res = []
        for p in puzzles:
            cur = 0
            for selector in itertools.product([0, 1], repeat=len(p) - 1):
                s = itertools.compress(p, [1] + list(selector))
                cur += count["".join(sorted(set(s)))]
            res.append(cur)
        return res

    def findNumOfValidWords2(self, words: list, puzzles: list) -> list:
        ret = [0] * len(puzzles)
        mem = dict()
        for pi, p in enumerate(puzzles):
            p_ = tuple(sorted(p))
            if (p_, p[0]) in mem:
                ret[pi] = mem[p_]
            else:
                res = 0
                for w in words:
                    if p[0] not in w: continue
                    w_ = set(w)
                    # print(w_, p)
                    if all([ww in p for ww in w_]): res += 1
                mem[(p_, p[0])] = res
                ret[pi] = res
        return ret


so = Solution()
print(so.findNumOfValidWords(words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                             puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
print(so.findNumOfValidWords(["apple", "pleas", "please"],
                             ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]))
