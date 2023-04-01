#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Print Words Vertically
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/26 19:54
@Desc   ：
=================================================="""


class Solution:
    def printVertically(self, s: str) -> list:
        def pad(s_, n_pad):
            return s_ + ' ' * n_pad

        all_words = s.split(' ')
        n = max([len(aw) for aw in all_words])
        all_words = list(map(pad, all_words, [n - len(l) for l in all_words]))

        ret = list(''.join(z).rstrip() for z in zip(*all_words))
        return ret


so = Solution()
print(so.printVertically(s="HOW ARE YOU"))
print(so.printVertically(s="TO BE OR NOT TO BE"))
print(so.printVertically(s="CONTEST IS COMING"))
