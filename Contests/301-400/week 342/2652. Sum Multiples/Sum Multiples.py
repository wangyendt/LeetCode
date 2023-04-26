"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Sum Multiples.py
@time: 20230425
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ret = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                ret += i
        return ret
