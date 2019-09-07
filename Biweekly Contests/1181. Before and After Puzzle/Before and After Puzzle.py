# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/7 23:35
# software: PyCharm


import collections


class Solution:
    def beforeAndAfterPuzzles(self, phrases: list) -> list:
        d = collections.defaultdict(list)
        ret = set()
        for i, ph in enumerate(phrases):
            phs = ph.split(' ')
            d[phs[0]].append((i, ' '.join(phs[1:])))  # or phs[0]))
        for i, ph in enumerate(phrases):
            phs = ph.split(' ')
            if phs[-1] in d:
                for ii, ph_ in d[phs[-1]]:
                    if i != ii:
                        ret.add((ph + ' ' + ph_).strip(' '))
        return sorted(list(ret))


so = Solution()
print(so.beforeAndAfterPuzzles(["a", "b", "a"]))
print(so.beforeAndAfterPuzzles(["mission statement",
                                "a quick bite to eat",
                                "a chip off the old block",
                                "chocolate bar",
                                "mission impossible",
                                "a man on a mission",
                                "block party",
                                "eat my words",
                                "bar of soap"]))
print(so.beforeAndAfterPuzzles(["writing code", "code rocks"]))
