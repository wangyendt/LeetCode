# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 15:48
# software: PyCharm

import bisect
import collections


class Solution:
    def numSmallerByFrequency(self, queries: list, words: list) -> list:
        ret = [0] * len(queries)
        f = lambda x: sorted(tuple(collections.Counter(x).items()), key=lambda y: y[0])[0][1]
        n_queries = [f(q) for q in queries]
        n_words = sorted([f(w) for w in words])
        for qi, q in enumerate(n_queries):
            ret[qi] = len(n_words) - bisect.bisect_right(n_words, q)
        return ret


so = Solution()
print(so.numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]))
print(so.numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))
