#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Groups of Strings
@time: 2022/02/01 02:07
"""

from typing import *
from collections import  defaultdict


class Solution:
    def groupStrings(self, w):
        M = {sum(1 << (ord(i) - ord("a")) for i in word): j for j, word in enumerate(w)}

        G = defaultdict(list)
        masks = defaultdict(list)
        for idx, word in enumerate(w):
            vals = [ord(i) - ord("a") for i in word]
            mask = sum(1 << i for i in vals)
            for i in vals:
                masks[mask - (1 << i) + (1 << 26)].append(idx)
                if mask - (1 << i) not in M: continue
                idx2 = M[mask - (1 << i)]
                G[idx] += [idx2]
                G[idx2] += [idx]

        for x in masks.values():
            for a, b in zip(x, x[1:]):
                G[a] += [b]
                G[b] += [a]

        V, comps, r = set(), 0, 0
        for u in range(len(w)):
            if u in V: continue
            compsize, q = 1, [u]
            V.add(u)
            while q:
                u = q.pop()
                for v in G[u]:
                    if v in V: continue
                    compsize += 1
                    V.add(v)
                    q += [v]
            r = max(r, compsize)
            comps += 1
        return [comps, r]
