#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Words That Can Be Formed by Characters
@time: 2019/8/20 15:17
"""

import collections


class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        chars_counter = collections.Counter(chars)
        ret = 0
        for w in words:
            if collections.Counter(w) & chars_counter == collections.Counter(w):
                ret += len(w)
        return ret


so = Solution()
print(so.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print(so.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
