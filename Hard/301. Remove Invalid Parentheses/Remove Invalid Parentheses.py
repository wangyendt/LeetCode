#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Remove Invalid Parentheses
@time: 2019/8/29 17:40
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        def is_valid(s_):
            s_ = ''.join(list(filter('()'.count, s_)))
            while '()' in s_:
                s_ = s_.replace('()', '')
            return not s_

        stack = {s}
        while True:
            valid = list(filter(is_valid, stack))
            if valid:
                return valid
            stack = {s[:i] + s[i + 1:] for s in stack for i in range(len(s))}

    def removeInvalidParentheses2(self, s: str) -> list:
        if not s: return []
        n1, n2 = sum([1 for ss in s if ss == '(']), sum([1 for ss in s if ss == ')'])
        print(n1, n2)
        # 左括号+1, 右括号-1, 画成折线图, 分段组合计数
        # 如()(())))()())(())), 发现右括号比左括号多4个,
        # 分段点在(8,9),(13,14),(18,)
        # 因此结果为C(5,2)+C(3,1)+C(3,1)
        cnt = 0
        min_val = 0
        gap_point = []
        for si, ss in enumerate(s):
            if ss == '(':
                cnt += 1
            elif ss == ')':
                cnt -= 1
            if cnt < min_val:
                min_val = cnt
                gap_point.append(si)


so = Solution()
print(so.removeInvalidParentheses('a((sdfas'))
print(so.removeInvalidParentheses('()(())))()())(()))'))
