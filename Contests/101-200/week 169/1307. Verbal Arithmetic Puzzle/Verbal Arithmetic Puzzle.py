#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Verbal Arithmetic Puzzle
@time: 2020/1/3 16:52
"""


class Solution:
    def isSolvable(self, words: list, result: str) -> bool:
        start = set()
        for word in words + [result]:
            if len(word) > 1:
                start.add(word[0])

        n = max(map(len, words + [result]))
        if len(result) < n:
            return False

        def dfs(idx, i, carry, visited, mp):
            if idx == n:
                return carry == 0
            if i == len(words) + 1:
                sums = sum(mp[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
                if sums % 10 == mp[result[-idx - 1]]:
                    carry = sums // 10
                    return dfs(idx + 1, 0, carry, visited, mp)
                return False

            if (i < len(words) and idx >= len(words[i])):
                return dfs(idx, i + 1, carry, visited, mp)
            tmp = words + [result]
            ch = tmp[i][-idx - 1]
            if ch in mp:
                return dfs(idx, i + 1, carry, visited, mp)
            begin = 0
            if ch in start:
                begin = 1
            for x in range(begin, 10):
                if x not in visited:
                    visited.add(x)
                    mp[ch] = x
                    if dfs(idx, i + 1, carry, visited, mp.copy()):
                        return True
                    visited.remove(x)
            return False

        return dfs(0, 0, 0, set(), {})
