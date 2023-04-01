"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Subsequence With the Minimum Score.py
@time: 20230328
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        suffix = [-1] * len(s)
        j = len(t) - 1
        for i in range(len(s) - 1, -1, -1):
            if 0 <= j and s[i] == t[j]:
                j -= 1
            suffix[i] = j
        ret = j + 1
        j = 0
        for i in range(len(s)):
            ret = min(ret, max(0, suffix[i] - j + 1))
            if j < len(t) and s[i] == t[j]:
                j += 1
        return min(ret, len(t) - j)
