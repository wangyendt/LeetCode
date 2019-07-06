# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/6 15:27
# software: PyCharm

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        cntBase = Counter(p)
        m, n = len(s), len(p)
        cnt = Counter(s[:n])
        ret = []
        for i in range(m - n+1):
            if cnt == cntBase:
                ret.append(i)
            if i+n<m:
                cnt[s[i + n]] += 1
                cnt[s[i]] -= 1
                cnt += Counter()
        return ret


so = Solution()
print(so.findAnagrams("cbaebabacd", "abc"))
