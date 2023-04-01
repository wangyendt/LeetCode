"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Append Characters to String to Make Subsequence.py
@time: 20221127
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        for i, tt in enumerate(t):
            for q in range(p, len(s)):
                if s[q] == tt:
                    p = q + 1
                    break
            else:
                break
        else:
            return 0
        return len(t) - i
