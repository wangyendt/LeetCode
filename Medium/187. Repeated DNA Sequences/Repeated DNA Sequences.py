# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 19:05
# software: PyCharm


class Tree:
    def __init__(self):
        self.dna = {}

    def has_chain(self, chain: str) -> bool:
        if chain and chain[0] in self.dna:
            if len(chain) == 1:
                return True
            else:
                return self.dna[chain[0]].has_chain(chain[1:])
        else:
            return False

    def add_chain(self, chain: str):
        if chain:
            if not (chain[0] in self.dna):
                self.dna[chain[0]] = Tree()
            self.dna[chain[0]].add_chain(chain[1:])

    def print_chains(self, chain=[]):
        if not self.dna: print(' -> '.join(chain))
        for dna_k, dna_v in self.dna.items():
            chain.append(dna_k)
            dna_v.print_chains(chain)
            chain.pop()


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list:
        root = Tree()
        ret = set()
        n_seq = 10
        for i in range(len(s) - n_seq + 1):
            ss = s[i:i + n_seq]
            if root.has_chain(ss):
                ret.add(ss)
            else:
                root.add_chain(ss)
            # root.print_chains()
        return list(ret)


so = Solution()
print(so.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
