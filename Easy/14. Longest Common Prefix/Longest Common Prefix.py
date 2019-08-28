# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/28 22:38
# software: PyCharm


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs: return ''
        ret = strs[0]
        while strs:
            s = strs.pop()
            for i in range(min(len(s), len(ret))):
                if s[i] != ret[i]:
                    ret = ret[:i]
                    break
        return ret


so = Solution()
print(so.longestCommonPrefix(["flower", "flow", "flight"]))
