#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 10:33
@Author:  wang121ye
@File: Rearrange Words in a Sentence.py
@Software: PyCharm
"""

import collections


class Solution:
    def arrangeWords(self, text: str) -> str:
        dict = collections.defaultdict(list)
        lens = set()
        for t in text.split(' '):
            dict[len(t)].append(t)
            lens.add(len(t))
        ret = []
        for l in sorted(list(lens)):
            for item in dict[l]:
                ret.append(item)
        # print(ret)
        ret = ' '.join(ret).lower()
        ret = ret[0].upper() + ret[1:]
        return ret


so = Solution()
print(so.arrangeWords(text="Leetcode is cool"))
print(so.arrangeWords(text="Keep calm and code on"))
print(so.arrangeWords(text="To be or not to be"))
