"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Odd String Difference.py
@time: 20221030
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def oddString(self, words: List[str]) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        res = {l: i for i, l in enumerate(letters)}

        def get_diff_word(word: str):
            ret = []
            for i in range(len(word)):
                if i:
                    ret.append(res[word[i]] - res[word[i - 1]])
            return ret

        cnt = collections.defaultdict(int)
        tmp = collections.defaultdict(str)
        for j, w in enumerate(words):
            cur = get_diff_word(w)
            cnt[tuple(cur)] += 1
            tmp[tuple(cur)] = w
        for k, v in cnt.items():
            if v == 1:
                return tmp[tuple(k)]


so = Solution()
print(so.oddString(words=["adc", "wzy", "abc"]))
