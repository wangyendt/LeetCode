"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Pivot Integer.py
@time: 20221127
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        cur = 0
        for i in range(1, n + 1):
            cur += i
            if cur * 2 == s + i:
                return i
        return -1
