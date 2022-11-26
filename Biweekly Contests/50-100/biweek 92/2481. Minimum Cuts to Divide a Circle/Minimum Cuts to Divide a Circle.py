"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Cuts to Divide a Circle.py
@time: 20221127
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        if n % 2 == 0:
            return n // 2
        else:
            return n
