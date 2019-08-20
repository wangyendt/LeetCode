#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Swap For Longest Repeated Character Substring
@time: 2019/8/20 13:44
"""


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        stack = []
        for ti, t in enumerate(text):
            if not stack:
                stack.append([t, 0, 1])
            else:
                ch, start, end = stack[-1]
                if t == ch:
                    stack[-1][-1] += 1
                else:
                    stack.append([t, ti, ti + 1])
        ret = 0
        while stack:
            ch, start, end = stack.pop(0)
            if ch in text[:start] + text[end:]:
                ret = max(ret, end - start + 1)
            else:
                ret = max(ret, end - start)
            if len(stack) > 1:
                ch_, start_, end_ = stack[1]
                if ch == ch_ and start_ - end == 1:
                    if ch in text[:start] + text[end_:]:
                        ret = max(ret, end_ - start)
                    else:
                        ret = max(ret, end_ - start - 1)
        return ret


so = Solution()
print(so.maxRepOpt1('aaabaaaca'), 7)
print(so.maxRepOpt1('aaaaa'), 5)
print(so.maxRepOpt1('abcdef'), 1)
print(so.maxRepOpt1("aaabbaaa"), 4)
