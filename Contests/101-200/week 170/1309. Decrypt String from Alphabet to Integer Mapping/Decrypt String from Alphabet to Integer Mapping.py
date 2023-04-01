#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Decrypt String from Alphabet to Integer Mapping
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/7 14:38
@Desc   ：
=================================================="""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        trans_dict = 'abcdefghijklmnopqrstuvwxyz'
        while True:
            pos = s.find('#')
            if pos == -1:
                break
            else:
                s = s[:pos - 2] + trans_dict[int(s[pos - 2:pos]) - 1] + s[pos + 1:]
        for tdi, td in enumerate(trans_dict):
            s = s.replace(str(tdi + 1), td)
        return s

so = Solution()
print(so.freqAlphabets("10#11#12"))
print(so.freqAlphabets("1326#"))
print(so.freqAlphabets("25#"))
print(so.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
