"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Using a Robot to Print the Lexicographically Smallest String.py
@time: 20221009
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections


class Solution:
    def robotWithString(self, s: str) -> str:
        cnter = collections.Counter(s)
        p, t = [], []
        for ch in s:
            t.append(ch)
            if cnter[ch] == 1:
                cnter.pop(ch)
            else:
                cnter[ch] -= 1
            while cnter and t and min(cnter) >= t[-1]:
                p.append(t.pop())
        return ''.join(p + t[::-1])


so = Solution()
print(so.robotWithString('bac'))
