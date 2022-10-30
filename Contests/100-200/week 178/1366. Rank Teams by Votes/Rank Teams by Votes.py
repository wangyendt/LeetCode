#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Rank Teams by Votes
@time: 2020/3/5 14:00
"""


class Solution:
    def rankTeams(self, votes: list) -> str:
        if not votes: return ''
        if len(votes) == 1: return votes[0]
        n = len(votes[0])
        marks = dict()
        # marks.setdefault([0] * n)
        for v in votes:
            for i, v_letter in enumerate(v):
                if v_letter not in marks:
                    marks[v_letter] = [0] * n
                marks[v_letter][i] += 1
        key = [[m] + marks[m] for m in marks]
        print(sorted(key, key=lambda x: (x[1:], x[0]), reverse=True))
        return ''.join([r[0] for r in sorted(key, key=lambda x: (x[1:], -ord(x[0])), reverse=True)])


so = Solution()
print(so.rankTeams(votes=["ABC", "ACB", "ABC", "ACB", "ACB"]))
print(so.rankTeams(votes=["WXYZ", "XYZW"]))
print(so.rankTeams(votes=["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
print(so.rankTeams(votes=["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))
print(so.rankTeams(votes=["M", "M", "M", "M"]))
